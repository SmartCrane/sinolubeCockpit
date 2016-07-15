# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand, CommandError
from OCEtl.models import TOcHostorderheader, TOcLogisticsorderheader,TOcHostorderline
from cockpit.models import TOcHostorder, TOcLogisticsorder,TWcsInVoucher, TWcsOutVouche, TWcsSLedger,TAlarmRecord,TTcEvaluation
from WCSEtl.models import WcsSLedger,WcsSLedgerdetaill,WcsInVoucherhead,WcsOutVoucherhead
from ALARMEtl.models import TAcAlarmRecord,TAcAlarmDefine,TAcAlarmSteps
from TCEtl.models import TcConsignorderheader,TcEvaluation
import datetime,logging,time
from django.db import transaction, connection

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    def handle(self, *args, **options):
        #抽取订单预警
        alarmFlag = getAlarmRecord('1')
        print alarmFlag
        if alarmFlag == False:
            print 'pro_orderalarm_deal未执行'
        elif alarmFlag == False:
            print 'pro_orderalarm_deal未执行'
        else:
            first = 1
            s1 = ''
            cursor = connection.cursor()
            cursor.callproc('pro_orderalarm_deal', (first, s1))
            #获取存储过程的返回第一个返回值"_1"
            cursor.execute('select @_pro_orderalarm_deal_1')
            data = cursor.fetchall()
            # 存储过程返回值
            s1 = data[0][0]
            print 'return000:%s' % s1

#抽取区间：1小时
period = 1
starttime = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:00:00"),'%Y-%m-%d %H:%M:%S') \
            - datetime.timedelta(hours=period)
endtime = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:00:00"),'%Y-%m-%d %H:%M:%S')

#订单预警
def getAlarmRecord(self):
    flag = True
    tagnoList = ['BJ003','BJ004','BJ007','BJ008','BJ011','BJ012','BJ015','BJ016','BJ019','BJ020']
    alarmRecords = TAcAlarmRecord.objects.filter(alarmdate__range=(starttime, endtime), tagno__in=tagnoList)

    for alarmRecord in alarmRecords:
        alarmid = alarmRecord.id
        alarmdate = alarmRecord.alarmdate
        alarmstatus = alarmRecord.alarmstatus
        tagno = alarmRecord.tagno
        for hostorder in TOcHostorderheader.objects.filter(hostorderno=alarmRecord.alarmstatus):
            tenantid = hostorder.tenantid
            ownerid = hostorder.ownerid
            for alarm_define in TAcAlarmDefine.objects.filter(tagno=alarmRecord.tagno):
                tagname = alarm_define.tagname
                alarmclass = alarm_define.alarmclass
                for alarm_step in TAcAlarmSteps.objects.filter(stepno=alarm_define.alarmclass):
                    stepname = alarm_step.stepname
                    alarm_savecommit(alarmid, alarmdate, alarmstatus, tagno, tagname, alarmclass, stepname, tenantid,
                                     ownerid)
                    # try:
                    #     alarm_savecommit(alarmid,alarmdate,alarmstatus,tagno,tagname,alarmclass,stepname,tenantid,ownerid)
                    # except Exception:
                    #     flag = False
                    #     logging.error(
                    #         '订单预警数据插入失败,预警ID：' + '%d' % id )
    return flag
# 保存订单预警 To
def alarm_savecommit(alarmid,alarmdate,alarmstatus,tagno,tagname,alarmclass,stepname,tenantid,ownerid):
    alarmRecord = TAlarmRecord()
    alarmRecord.alarmid = alarmid
    alarmRecord.alarmdate = alarmdate
    alarmRecord.alarmstatus = alarmstatus
    alarmRecord.tagno = tagno
    alarmRecord.tagname = tagname
    alarmRecord.alarmclass = alarmclass
    alarmRecord.stepname = stepname
    alarmRecord.etltime = datetime.datetime.now()
    alarmRecord.tenantid = tenantid
    alarmRecord.ownerid = ownerid
    alarmRecord.save()

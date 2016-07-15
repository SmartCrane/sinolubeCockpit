# -*- coding: UTF-8 -*-
'''
抽取用户对装运单的评价星级
'''
from django.core.management.base import BaseCommand, CommandError
from cockpit.models import TTcEvaluation
from TCEtl.models import TcConsignorderheader
from evalEtl.models import TEcShipmenteval
import datetime,logging,time
from django.db import transaction, connection

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    def handle(self, *args, **options):
        # 抽取物流服务商
        evaFlag = getEvaluation('1')
        print evaFlag
        if evaFlag == False:
            print 'pro_log_start_deal未执行'
        elif evaFlag == False:
            print 'pro_log_start_deal未执行'
        else:
            first = 1
            s1 = ''
            cursor = connection.cursor()
            cursor.callproc('pro_log_start_deal', (first, s1))
            # 获取存储过程的返回第一个返回值"_1"
            cursor.execute('select @_pro_log_start_deal_1')
            data = cursor.fetchall()
            # 存储过程返回值
            s1 = data[0][0]
            print 'return000:%s' % s1

#抽取区间：1小时
period = 1
starttime = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:00:00"),'%Y-%m-%d %H:%M:%S') \
            - datetime.timedelta(hours=period)
endtime = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:00:00"),'%Y-%m-%d %H:%M:%S')

#物流商评价
def getEvaluation(self):
    carrierEvaluations = TcConsignorderheader.objects.filter(createdtime__range=(starttime,endtime))
    # print carrierEvaluations.query
    flag = True
    for carrierEvaluation in carrierEvaluations:
        #委托单Head信息
        id = carrierEvaluation.id
        tenantid = carrierEvaluation.tenantid
        ownerid = 0
        carrierid = carrierEvaluation.carrierid
        carriername = carrierEvaluation.carriername
        createdtime = carrierEvaluation.createdtime
        # todo 评价中心里的t_ec_shipmenteval，里面有一个ShipmentCode，对应的是TC_ConsignOrderHeader中的ErpCoNo
        # todo satisfactionStated,满意度字段，值就是星级：1就是一星，2就是二星，3就是三星如此等等

        #评价信息
        for evaluation in TEcShipmenteval.objects.filter(shipmentcode=carrierEvaluation.erpcono):
            evaluationid = evaluation.id
            shipmentcode = evaluation.shipmentcode
            satisfactionstate = evaluation.satisfactionstate
            try:
                TTcEvaluation(id=id,tenantid=tenantid,ownerid=ownerid,carrierid=carrierid,carriername=carriername,createdtime=createdtime,
                              evaluationid=evaluationid,shipmentcode=shipmentcode,satisfactionstate=satisfactionstate).save()
            except Exception:
                flag = False
                logging.error(
                    '物流商评价数据插入失败,预警ID：' + '%d' % id)

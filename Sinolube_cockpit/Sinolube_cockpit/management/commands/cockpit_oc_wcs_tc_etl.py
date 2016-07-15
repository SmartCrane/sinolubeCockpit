# -*- coding: UTF-8 -*-
'''
抽取销售订单、物流订单、库存、入库、出库以及调运的信息。
'''
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
        #抽取销售订单
        o1 = getorderstatics('1')
        #抽取物流订单
        o2 = getlogistics('1')
        # 现在的逻辑是save有错，存储过程不执行
        if o1 == False:
            print 'pro_hostorders_deal未执行'
        elif o2 == False:
            print 'pro_hostorders_deal未执行'
        else:
            first = 1
            s1 = ''
            cursor = connection.cursor()
            cursor.callproc('pro_hostorders_deal',(first,s1))
            cursor.execute('select @_pro_hostorders_deal_1')
            data=cursor.fetchall()
            # 存储过程返回值
            s1 = data[0][0]
            print 'return000:%s'%s1
        #抽取仓储
        f1 = getSLedger('1')
        #抽取仓储入库数据
        f2 = getWcsInVoucherhead('1')
        #抽取仓储出库数据
        f3 = getWcsOutVoucherhead('1')
        #仓储存储过程调用
        # 现在的逻辑是save操作有错，存储过程不执行
        if f1 == False:
            print '1'
        elif f2 == False:
            print '1'
        elif f3 ==False:
            print '1'
        else:
            first = 1
            s1 = ''
            cursor = connection.cursor()
            #有一个输出参数，这里也需要传递进去
            cursor.callproc('pro_warehouse_statistics',(first,s1))
            #获取输出参数格式@_存储过程名_参数位置
            cursor.execute('select @_pro_warehouse_statistics_1')
            data=cursor.fetchall()
            #获取方式，data是一个结构，第一个0是取结构中的第一个成员，第二个0是成员中的第一个值
            s1 = data[0][0]
            print 'return111:%s'%s1

        #抽取调运,直接调用存储过程抽取物流订单表（t_oc_logisticsorder）待委托（consignstatus=10）的交货单量以
        # 及出库表（t_wcs_out_vouche）中的出库量
        first = 1
        s1 = ''
        cursor = connection.cursor()
        cursor.callproc('pro_transform_deal', (first, s1))
        #获取存储过程的返回第一个返回值"_1"
        cursor.execute('select @_pro_transform_deal_1')
        data = cursor.fetchall()
        # 存储过程返回值
        s1 = data[0][0]
        print 'return000:%s' % s1

#抽取区间：1小时
period = 1
starttime = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:00:00"),'%Y-%m-%d %H:%M:%S') \
            - datetime.timedelta(hours=period)
endtime = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:00:00"),'%Y-%m-%d %H:%M:%S')
# 获取销售订单Header及Line数据
def getorderstatics(self):
    hostorders = TOcHostorderheader.objects.filter(createdtime__range=(starttime, endtime), closestatus='10')
    flag = True
    
    #获取Header
    for hostorder in hostorders:
        id1 = hostorder.id
        tenantid = hostorder.tenantid
        hostorderno = hostorder.hostorderno
        hostordercategory = hostorder.hostordercategory
        hostordertype = hostorder.hostordertype
        ownerid = hostorder.ownerid
        sporgcode = hostorder.sporgcode
        dccode = hostorder.dccode
        # 获取销售订单line
        for orderline in hostorder.tochostorderline_set.all():
            seqno = orderline.seqno
            itemcode = orderline.itemcode
            itemname = orderline.itemname
            itemspec = orderline.itemspec
            grossweight = orderline.grossweight
            createdtime = orderline.createdtime
            lotno = orderline.lotno
            # 保存销售订单Header & line TO Table t_oc_hostorder
            try:
                ho_savecommit(id1, tenantid, hostorderno, hostordercategory, hostordertype, ownerid, sporgcode, dccode, \
                           seqno, itemcode, itemname, itemspec, grossweight, createdtime, endtime, lotno)
            except Exception,e:
                flag = False
                logging.error('订单数据插入失败,订单抬头ID：'+'%d'%id1+',  租户ID：'+ '%d'%tenantid + ',  行项目ID：'+'%d'%seqno)

    return flag

# 保存销售订单Header & line TO Table t_oc_hostorder
def ho_savecommit(id1, tenantid, hostorderno, hostordercategory, hostordertype, ownerid, sporgcode, dccode, \
               seqno, itemcode, itemname, itemspec, grossweight, createdtime, etltime, lotno):
    ths = TOcHostorder()
    ths.tid = id1
    ths.tenantid = tenantid
    ths.hostorderno = hostorderno
    ths.hostordercategory = hostordercategory
    ths.hostordertype = hostordertype
    ths.ownerid = ownerid
    ths.sporgcode = sporgcode
    ths.dccode = dccode

    ths.seqno = seqno
    ths.itemcode = itemcode
    ths.itemname = itemname
    ths.itemspec = itemspec
    ths.grossweight = grossweight
    ths.createdtime = createdtime
    ths.etltime = etltime + datetime.timedelta(hours=8)
    ths.lotno = lotno
    ths.save()

# 获取物流订单信息
def getlogistics(self):
    logisticsorders = TOcLogisticsorderheader.objects.filter(createdtime__range=(starttime, endtime))
    flag = True

    for logisticsorder in logisticsorders:
        id1 = logisticsorder.id
        tenantid = logisticsorder.tenantid
        loorderno = logisticsorder.loorderno
        hostorderno = logisticsorder.hostorderno
        docdate = logisticsorder.docdate
        ownerid = logisticsorder.ownerid
        sporgcode = logisticsorder.sporgcode
        dccode = logisticsorder.dccode
        spdeptcode = logisticsorder.spdeptcode
        spgroupcode = logisticsorder.spgroupcode
        salesofficecode = logisticsorder.salesofficecode
        startdate = logisticsorder.startdate
        enddate = logisticsorder.enddate
        createdtime = logisticsorder.createdtime
        #loadstatus 发运状态,10=未发运 50=部分发运 90=全部发运
        loadstatus = logisticsorder.loadstatus
        # 委托状态，lo_consign_status，10=未委托；50=部分委托；90=全部委托
        consignstatus = logisticsorder.consignstatus
        
        # he = logisticsorder.tochostorderline_set.all()
        for logisticsorderline in logisticsorder.toclogisticsorderline_set.all():
            seqno = logisticsorderline.seqno
            itemid = logisticsorderline.itemid
            itemcode = logisticsorderline.itemcode
            itemname = logisticsorderline.itemname
            itemspec = logisticsorderline.itemspec
            grossweight = logisticsorderline.grossweight
            lotno = logisticsorderline.lotno

            lo_savecommit(id1, tenantid, loorderno, hostorderno, docdate, ownerid, sporgcode, dccode, spdeptcode, \
                          spgroupcode, salesofficecode, startdate, enddate, \
                          createdtime, loadstatus, consignstatus, seqno, itemid, itemcode, itemname, itemspec,
                          grossweight, lotno, endtime)
            # try:
            #     lo_savecommit(id1, tenantid, loorderno, hostorderno, docdate, ownerid, sporgcode, dccode, spdeptcode,\
            #                 spgroupcode, salesofficecode, startdate, enddate, \
            #                 createdtime, loadstatus,consignstatus, seqno, itemid, itemcode, itemname, itemspec, grossweight, lotno, endtime)
            # except Exception,e:
            #     flag = False
            #     logging.error('订单数据插入失败,订单抬头ID：'+'%d'%id1+',  租户ID：'+ '%d'%tenantid + ',  行项目ID：'+'%d'%seqno)
    return flag

def lo_savecommit(id1, tenantid, loorderno, hostorderno, docdate, ownerid, sporgcode, dccode, spdeptcode, spgroupcode,\
                salesofficecode, startdate, enddate, \
                createdtime, loadstatus,consignstatus, seqno, itemid, itemcode, itemname, itemspec, grossweight, lotno, endtime):
    ths = TOcLogisticsorder()

    ths.lid = id1
    ths.tenantid = tenantid
    ths.loorderno = loorderno
    ths.hostorderno = hostorderno
    ths.docdate = docdate
    ths.ownerid = ownerid
    ths.sporgcode = sporgcode
    ths.dccode = dccode
    ths.spdeptcode = spdeptcode
    ths.spgroupcode = spgroupcode
    ths.salesofficecode = salesofficecode
    ths.startdate = startdate
    ths.enddate = enddate
    ths.createdtime = createdtime
    ths.loadstatus = loadstatus
    ths.consignstatus = consignstatus

    ths.seqno = seqno
    ths.itemid = itemid
    ths.itemcode = itemcode
    ths.itemname = itemname
    ths.itemspec = itemspec
    ths.grossweight = grossweight
    ths.lotno = lotno
    ths.etltime = endtime + datetime.timedelta(hours=8)

    ths.save()

#获取仓储数据
def getSLedger(self):
    sledgers = WcsSLedger.objects.filter(createdtime__range=(starttime, endtime))
    flag = True

    for sledger in sledgers:
        id1 = sledger.id
        tenantid = sledger.tenantid
        ownerid = sledger.ownerid
        factorycode = sledger.factorycode
        stockaddressid = sledger.stockaddressid
        materielid = sledger.materielid
        for sledgerDetail in sledger.wcssledgerdetaill_set.all():
            lotno = sledgerDetail.lotno
            sagrossweight = sledgerDetail.sagrossweight
            createtime = sledgerDetail.createdtime
            
            try:
                sledger_savecommit(id1, tenantid, ownerid, factorycode, stockaddressid, materielid, lotno,
                                   sagrossweight, createtime)
            except Exception:
                flag = False
                logging.error('订单数据插入失败,订单抬头ID：'+'%d'%id1+',  租户ID：'+ '%d'%tenantid + ',  仓库ID：'+'%d'%stockaddressid)

    return flag
   
#保存库存台账
def sledger_savecommit(id1, tenantid, ownerid, factorycode, stockaddressid, materielid, lotno,
                                   sagrossweight,createtime):
    dw_sledger = TWcsSLedger()
    dw_sledger.leid = id1
    dw_sledger.tenantid = tenantid
    dw_sledger.ownerid = ownerid
    dw_sledger.factorycode = factorycode
    dw_sledger.stockaddressid = stockaddressid
    dw_sledger.materielid = materielid
    dw_sledger.lotno = lotno
    dw_sledger.sagrossweight = sagrossweight
    dw_sledger.etltime = datetime.datetime.now()
    dw_sledger.createdtime = createtime
    dw_sledger.save()
    
#获取仓储入库数据
def getWcsInVoucherhead(self):
    wivheads = WcsInVoucherhead.objects.filter(createdtime__range=(starttime, endtime))
    flag = True
    
    for wivhead in wivheads:
        inid = wivhead.id
        tenantid = wivhead.tenantid
        biztype = wivhead.biztype
        specialstock = wivhead.specialstock
        
        for wivline in wivhead.wcsinvoucherline_set.all():
            seqno = wivline.seqno
            itemid = wivline.itemid
            movetype = wivline.movetype
            grossweight = wivline.grossweight
            lotno = wivline.lotno
            stockaddressid = wivline.stockaddressid
            createdtime = wivline.createdtime
            
            try:
                wiv_savecommit(inid, tenantid, biztype, specialstock, seqno, itemid, movetype, grossweight, lotno, stockaddressid, createdtime)
            except Exception:
                flag = False
                logging.error('订单数据插入失败,订单抬头ID：'+'%d'%inid+',  租户ID：'+ '%d'%tenantid + ',  仓库ID：'+'%d'%stockaddressid)
    return flag
    
def wiv_savecommit(inid, tenantid, biztype, specialstock, seqno, itemid, movetype, grossweight, lotno, stockaddressid, createdtime):
    ths = TWcsInVoucher()
    ths.inid = inid
    ths.tenantid = tenantid
    ths.biztype = biztype
    ths.specialstock = specialstock
    ths.seqno = seqno
    ths.itemid = itemid
    ths.movetype = movetype
    ths.grossweight = grossweight
    ths.lotno = lotno
    ths.stockaddressid = stockaddressid
    ths.createdtime = createdtime
    ths.etltime = endtime + datetime.timedelta(hours=8)
    
    ths.save()
    
def getWcsOutVoucherhead(self):
    wovheads = WcsOutVoucherhead.objects.filter(createdtime__range=(starttime, endtime))
    flag = True
    
    for wovhead in wovheads:
        outid = wovhead.id
        tenantid = wovhead.tenantid
        
        for wovline in wovhead.wcsoutvoucherline_set.all():
            seqno = wovline.seqno
            matreialvoucherno = wovline.matreialvoucherno
            itemid = wovline.itemid
            grossweight = wovline.grossweight
            stockaddressid = wovline.stockaddressid
            lotno = wovline.lotno
            lotnoactualoutqty = wovline.lotnoactualoutqty
            specialstockmark = wovline.specialstockmark
            createdtime = wovline.createdtime
            
            try:
                wov_savecommit(outid, tenantid, seqno, matreialvoucherno, itemid, grossweight, stockaddressid, lotno, lotnoactualoutqty, specialstockmark, createdtime)
            except Exception:
                flag = False
                logging.error('订单数据插入失败,订单抬头ID：'+'%d'%outid+',  租户ID：'+ '%d'%tenantid + ',  仓库ID：'+'%d'%stockaddressid)

    return flag

def wov_savecommit(outid, tenantid, seqno, matreialvoucherno, itemid, grossweight, stockaddressid, lotno, lotnoactualoutqty, specialstockmark, createdtime):
    ths = TWcsOutVouche()
    ths.outid = outid
    ths.tenantid = tenantid
    ths.seqno = seqno
    ths.matreialvoucherno = matreialvoucherno
    ths.itemid = itemid
    ths.grossweight = grossweight
    ths.stockaddressid = stockaddressid
    ths.lotno = lotno
    ths.lotnoactualoutqty = lotnoactualoutqty
    ths.specialstockmark = specialstockmark
    ths.createdtime = createdtime
    ths.etltime = endtime
    
    ths.save()

#订单预警
# 保存订单预警 To

# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from OCEtl.models import TOcHostorderheader, TOcLogisticsorderheader,TOcHostorderline
from cockpit.models import TOcHostorder, TOcLogisticsorder
import datetime, os,logging
from django.db import connection,transaction
from Sinolube_cockpit.settings import BASE_DIR

period = 24


def getorderstatics(self):
    starttime = datetime.datetime.now() - datetime.timedelta(hours=period)
    endtime = datetime.datetime.now()

    hostorders = TOcHostorderheader.objects.filter(createdtime__range=(starttime, endtime), closestatus='10')
    print starttime, endtime
    num = 0
    flag = True

    logging.info("开始抽取订单数据")
   
    for hs in hostorders:
        id1 = hs.id
        tenantid = hs.tenantid
        hostorderno = hs.hostorderno
        hostordercategory = hs.hostordercategory
        hostordertype = hs.hostordertype
        ownerid = hs.ownerid
        sporgcode = hs.sporgcode
        dccode = hs.dccode
        
        # he = hs.tochostorderline_set.all()
        for he in hs.tochostorderline_set.all():
            seqno = he.seqno
            itemcode = he.itemcode
            itemname = he.itemname
            itemspec = he.itemspec
            grossweight = he.grossweight
            createdtime = he.createdtime
            print '抬头:%s'%createdtime
            lotno = he.lotno

            try:
                savecommit(id1, tenantid, hostorderno, hostordercategory, hostordertype, ownerid, sporgcode, dccode, \
                           seqno, itemcode, itemname, itemspec, grossweight, createdtime, endtime, lotno)
            except Exception,e:
                flag = False
                logging.error('订单数据插入失败,订单抬头ID：'+'%d'%id1+',  租户ID：'+ '%d'%tenantid + ',  行项目ID：'+'%d'%seqno)

            logging.info("订单数据抽取成功")
            f1 = getlogistics('1')
            num += 1
            print "------------抬头", num, "------------"
    #print num1
    #print "good by"

    if flag == False:
        return
    elif f1 == False:
        return
    else:

        first = 1
        s1 = ''
        cursor = connection.cursor()
        #有一个输出参数，这里也需要传递进去
        cursor.callproc('pro_hostorders_deal',(first,s1))
        #获取输出参数格式@_存储过程名_参数位置
        cursor.execute('select @_pro_hostorders_deal_1')
        data=cursor.fetchall()
        #获取方式，data是一个结构，第一个0是取结构中的第一个成员，第二个0是成员中的第一个值
        s1 = data[0][0]
        print '存储过程返回值：%s'%s1
   

    # call shell
    # cmdstr = "dir"
    # f = os.popen2(cmdstr)
    # res = f.read()



def savecommit(id1, tenantid, hostorderno, hostordercategory, hostordertype, ownerid, sporgcode, dccode, \
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
    print createdtime
    ths.etltime = etltime + datetime.timedelta(hours=8)
    ths.lotno = lotno
    ths.save()
    

def getlogistics(self):
    starttime = datetime.datetime.now() - datetime.timedelta(hours=period)
    endtime = datetime.datetime.now()

    logisticsorders = TOcLogisticsorderheader.objects.filter(createdtime__range=(starttime, endtime))
    print starttime, endtime
    num = 0
    num1 = 0

    #logging.info("��ʼ��ȡ��������")

    for hs in logisticsorders:
        id1 = hs.id
        tenantid = hs.tenantid
        loorderno = hs.loorderno
        hostorderno = hs.hostorderno
        docdate = hs.docdate
        ownerid = hs.ownerid
        sporgcode = hs.sporgcode
        dccode = hs.dccode
        spdeptcode = hs.spdeptcode
        spgroupcode = hs.spgroupcode
        salesofficecode = hs.salesofficecode
        startdate = hs.startdate
        enddate = hs.enddate
        createdtime = hs.createdtime
        # he = hs.tochostorderline_set.all()
        for he in hs.toclogisticsorderline_set.all():
            seqno = he.seqno
            itemid = he.itemid
            itemcode = he.itemcode
            itemname = he.itemname
            itemspec = he.itemspec
            grossweight = he.grossweight
            # createdtime = he.createdtime
            lotno = he.lotno

            try:
                savecommit1(id1, tenantid, loorderno, hostorderno, docdate, ownerid, sporgcode, dccode, spdeptcode,
                            spgroupcode, salesofficecode, startdate, enddate, \
                            createdtime, seqno, itemid, itemcode, itemname, itemspec, grossweight, lotno, endtime)
            except Exception,e:
                f1 = False
                logging.error('订单数据插入失败,订单抬头ID：'+'%d'%id1+',  租户ID：'+ '%d'%tenantid + ',  行项目ID：'+'%d'%seqno)

            num += 1
            print "------------行项目", num, "------------"

    # call shell
    # cmdstr = "dir"
    # f = os.popen2(cmdstr)
    # res = f.read()
    return f1

def savecommit1(id1, tenantid, loorderno, hostorderno, docdate, ownerid, sporgcode, dccode, spdeptcode, spgroupcode,
                salesofficecode, startdate, enddate, \
                createdtime, seqno, itemid, itemcode, itemname, itemspec, grossweight, lotno, endtime):
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

    ths.seqno = seqno
    ths.itemid = itemid
    ths.itemcode = itemcode
    ths.itemname = itemname
    ths.itemspec = itemspec
    ths.grossweight = grossweight
    ths.lotno = lotno
    ths.etltime = endtime + datetime.timedelta(hours=8)

    ths.save()
    
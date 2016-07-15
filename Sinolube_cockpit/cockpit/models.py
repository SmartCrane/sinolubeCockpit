# -*- coding: UTF-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

#from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
class BiCommonPagesu(models.Model):
#class BI_COMMON_PAGESU(models.Model):
    mstrid = models.CharField(primary_key=True, max_length=32)
    
    mstrname = models.CharField(max_length=64, blank=True)
    
    mstraddr = models.CharField(max_length=250, blank=True)
    urladdr = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
            return self.mstrname
    class Meta:
        managed = True
        #db_table = 'tab_bdata_common_pagesu'
        db_table ='bi_common_pagesu'
#         db_table ='tab_bdata_common_pagesu'
        verbose_name = '页面配置'
        verbose_name_plural = '页面配置' 
        
class PagesuDocID(models.Model):
    pageid = models.CharField(primary_key=True, max_length=32)
    
    documentname = models.CharField(max_length=64, blank=True)
    docid=models.CharField(max_length=50, blank=True)
    
    def __unicode__(self):
            return self.documentname
    class Meta:
        managed = True
        #db_table = 'tab_bdata_common_pagesu'
        db_table ='bi__pagesu_docid'
#         db_table ='tab_bdata_common_pagesu'
        verbose_name = '文档配置'
        verbose_name_plural = '文档配置'

class TOcHostorder(models.Model):
    tid = models.IntegerField(db_column='tID')  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID', blank=True, null=True)  # Field name made lowercase.
    hostorderno = models.CharField(db_column='HostOrderNo', max_length=40, blank=True)  # Field name made lowercase.
    hostordercategory = models.CharField(db_column='HostOrderCategory', max_length=40, blank=True)  # Field name made lowercase.
    hostordertype = models.CharField(db_column='HostOrderType', max_length=40, blank=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID', blank=True, null=True)  # Field name made lowercase.
    sporgcode = models.CharField(db_column='SpOrgCode', max_length=40, blank=True)  # Field name made lowercase.
    dccode = models.CharField(db_column='DcCode', max_length=40, blank=True)  # Field name made lowercase.
    seqno = models.CharField(db_column='SeqNo', max_length=40, blank=True)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=40, blank=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=100, blank=True)  # Field name made lowercase.
    itemspec = models.CharField(db_column='ItemSpec', max_length=100, blank=True)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    etltime = models.DateTimeField(db_column='EtlTime', blank=True, null=True)  # Field name made lowercase.
    lotno = models.CharField(db_column='LotNo',max_length=200,blank=True)

    class Meta:
        managed = False
        db_table = 't_oc_hostorder'

class TOcLogisticsorder(models.Model):
    lid = models.IntegerField(db_column='LID')  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID', blank=True, null=True)  # Field name made lowercase.
    loorderno = models.CharField(db_column='LoOrderNo', max_length=40)  # Field name made lowercase.
    hostorderno = models.CharField(db_column='HostOrderNo', max_length=40)  # Field name made lowercase.
    docdate = models.DateField(db_column='DocDate', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='OwnerID', max_length=40, blank=True)  # Field name made lowercase.
    sporgcode = models.CharField(db_column='SpOrgCode', max_length=40, blank=True)  # Field name made lowercase.
    dccode = models.CharField(db_column='DcCode', max_length=40, blank=True)  # Field name made lowercase.
    spdeptcode = models.CharField(db_column='SpDeptCode', max_length=40, blank=True)  # Field name made lowercase.
    spgroupcode = models.CharField(db_column='SpGroupCode', max_length=40, blank=True)  # Field name made lowercase.
    salesofficecode = models.CharField(db_column='SalesOfficeCode', max_length=40, blank=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    loadstatus = models.CharField(db_column='LoadStatus',max_length=40, blank=True) # Field name made lowercase.
    consignstatus = models.CharField(db_column='ConsignStatus', max_length=40)  # Field name made lowercase.
    seqno = models.CharField(db_column='SeqNo', max_length=40, blank=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=40, blank=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=100, blank=True)  # Field name made lowercase.
    itemspec = models.CharField(db_column='ItemSpec', max_length=100, blank=True)  # Field name made lowercase.
    lotno = models.CharField(db_column='LotNo', max_length=200, blank=True)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    etltime = models.DateTimeField(db_column='EtlTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_oc_logisticsorder'

class TWcsInVoucher(models.Model):
    inid = models.IntegerField(db_column='inID')  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    biztype = models.CharField(db_column='BizType', max_length=40)  # Field name made lowercase.
    specialstock = models.CharField(db_column='SpecialStock', max_length=1)  # Field name made lowercase.
    seqno = models.CharField(db_column='SeqNo', max_length=40, blank=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    movetype = models.CharField(db_column='MoveType', max_length=40)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lotno = models.CharField(db_column='LotNo', max_length=200, blank=True)  # Field name made lowercase.
    stockaddressid = models.IntegerField(db_column='StockAddressID')  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    etltime = models.DateTimeField(db_column='EtlTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_wcs_in_voucher'


class TWcsOutVouche(models.Model):
    outid = models.IntegerField(db_column='outID')  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    seqno = models.CharField(db_column='SeqNo', max_length=40, blank=True)  # Field name made lowercase.
    matreialvoucherno = models.CharField(db_column='MatreialVoucherNo', max_length=40, blank=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    stockaddressid = models.IntegerField(db_column='StockAddressID')  # Field name made lowercase.
    lotno = models.CharField(db_column='LotNo', max_length=200, blank=True)  # Field name made lowercase.
    lotnoactualoutqty = models.DecimalField(db_column='LotNoActualOutQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    specialstockmark = models.CharField(db_column='SpecialStockMark', max_length=1, blank=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    etltime = models.DateTimeField(db_column='EtlTime')  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 't_wcs_out_vouche'


class TWcsSLedger(models.Model):
    leid = models.IntegerField(db_column='leID')  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID')  # Field name made lowercase.
    factorycode = models.CharField(db_column='FactoryCode', max_length=40)  # Field name made lowercase.
    sagrossweight = models.DecimalField(db_column='SAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    stockaddressid = models.IntegerField(db_column='StockAddressID')  # Field name made lowercase.
    materielid = models.IntegerField(db_column='MaterielID')  # Field name made lowercase.
    lotno = models.CharField(db_column='LotNo', max_length=200)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    etltime = models.DateTimeField(db_column='EtlTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_wcs_s_ledger'

class TAlarmRecord(models.Model):
    alarmid = models.IntegerField(db_column='ID')  # Field name made lowercase.
    alarmdate = models.DateTimeField(db_column='AlarmDate', blank=True, null=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID')  # Field name made lowercase.
    alarmstatus = models.CharField(db_column='AlarmStatus', max_length=50, blank=True)  # Field name made lowercase.
    tagno = models.CharField(db_column='TagNo', max_length=50, blank=True)  # Field name made lowercase.
    tagname = models.CharField(db_column='TagName', max_length=50, blank=True)  # Field name made lowercase.
    alarmclass = models.CharField(db_column='AlarmClass', max_length=50, blank=True)  # Field name made lowercase.
    stepname = models.CharField(max_length=50, blank=True)
    etltime = models.DateTimeField(db_column='EtlTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_alarm_record'

class FLogisticsStartStatistics(models.Model):
    daydate = models.DateField(db_column='DayDate', blank=True, null=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID', blank=True, null=True)  # Field name made lowercase.
    tenantcode = models.CharField(db_column='TenantCode', max_length=40, blank=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID', blank=True, null=True)  # Field name made lowercase.
    ownercode = models.CharField(db_column='OwnerCode', max_length=100, blank=True)  # Field name made lowercase.
    logisticsproviderid = models.CharField(db_column='LogisticsProviderID', max_length=40, blank=True)  # Field name made lowercase.
    logisticsprovidername = models.CharField(db_column='LogisticsProviderName', max_length=120, blank=True)  # Field name made lowercase.
    statnum = models.IntegerField(db_column='StatNum', blank=True, null=True)  # Field name made lowercase.
    starlevelid = models.IntegerField(db_column='StarLevelID', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'f_logistics_start_statistics'

#物流商评价
class TTcEvaluation(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID', blank=True, null=True)  # Field name made lowercase.
    carrierid = models.IntegerField(db_column='CarrierID', blank=True, null=True)  # Field name made lowercase.
    carriername = models.CharField(db_column='CarrierName', max_length=100, blank=True)  # Field name made lowercase.
    evaluationid = models.CharField(db_column='EvaluationID', max_length=4000, blank=True)  # Field name made lowercase.
    shipmentcode = models.CharField(db_column='ShipmentCode', max_length=40, blank=True)  # Field name made lowercase.
    satisfactionstate = models.CharField(db_column='SatisfactionState', max_length=40, blank=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_tc_evaluation'
class LuOwner(models.Model):
    tenantid = models.IntegerField(db_column='TenantID', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID', primary_key=True)  # Field name made lowercase.
    ownercode = models.CharField(db_column='OwnerCode', max_length=100, blank=True)  # Field name made lowercase.
    ownername = models.CharField(db_column='OwnerName', max_length=200, blank=True)  # Field name made lowercase.
    ownershortname = models.CharField(db_column='OwnerShortName', max_length=200, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lu_owner'


class LuPlant(models.Model):
    plantid = models.IntegerField(db_column='PlantID', primary_key=True)  # Field name made lowercase.
    plantcode = models.CharField(db_column='PlantCode', max_length=40, blank=True)  # Field name made lowercase.
    plantname = models.CharField(db_column='PlantName', max_length=200, blank=True)  # Field name made lowercase.
    plantshortname = models.CharField(db_column='PlantShortName', max_length=200, blank=True)  # Field name made lowercase.
    headerid = models.IntegerField(db_column='HeaderID')  # Field name made lowercase.
    ownercode = models.CharField(db_column='OwnerCode', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lu_plant'

class LuTenant(models.Model):
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    tenantcode = models.CharField(db_column='TenantCode', max_length=40, blank=True)  # Field name made lowercase.
    tenantname = models.CharField(db_column='TenantName', max_length=120, blank=True)  # Field name made lowercase.
    tenantshortname = models.CharField(db_column='TenantShortName', max_length=60, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lu_tenant'


class LuWarehouse(models.Model):
    warehouseid = models.IntegerField(db_column='WarehouseID', blank=True, null=True)  # Field name made lowercase.
    warehousecode = models.CharField(db_column='WarehouseCode', max_length=10, blank=True)  # Field name made lowercase.
    warehousename = models.CharField(db_column='WarehouseName', max_length=100, blank=True)  # Field name made lowercase.
    warehouseshortname = models.CharField(db_column='WarehouseShortName', max_length=100, blank=True)  # Field name made lowercase.
    plantcode = models.CharField(db_column='PlantCode', max_length=40, blank=True)  # Field name made lowercase.
    maxwarncapacity = models.DecimalField(db_column='MaxWarnCapacity', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    minwarncapacity = models.DecimalField(db_column='MinWarnCapacity', max_digits=10, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lu_warehouse'
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

from django.db import models


class TcCaips(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    salesorderid = models.IntegerField(db_column='SalesOrderID', blank=True, null=True)  # Field name made lowercase.
    infodetail = models.CharField(db_column='InfoDetail', max_length=1000, blank=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=20, blank=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=20, blank=True)  # Field name made lowercase.
    hostdeliveryqty = models.DecimalField(db_column='HostDeliveryQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    stagetime = models.DateTimeField(db_column='StageTime', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=1000, blank=True)  # Field name made lowercase.
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tc_caips'


class TcConsignitemlot(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    colid = models.IntegerField(db_column='ColID')  # Field name made lowercase.
    lotno = models.CharField(db_column='LotNo', max_length=200, blank=True)  # Field name made lowercase.
    consignqty = models.DecimalField(db_column='ConsignQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loadqty = models.DecimalField(db_column='LoadQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    valuationtype = models.CharField(db_column='ValuationType', max_length=200, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tc_consignitemlot'


class TcConsignorderdriver(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    consignid = models.IntegerField(db_column='ConsignID')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=6, blank=True)  # Field name made lowercase.
    driverid = models.IntegerField(db_column='DriverID')  # Field name made lowercase.
    drivername = models.CharField(db_column='DriverName', max_length=20, blank=True)  # Field name made lowercase.
    drivercode = models.CharField(db_column='DriverCode', max_length=20, blank=True)  # Field name made lowercase.
    drivertel = models.CharField(db_column='DriverTel', max_length=15, blank=True)  # Field name made lowercase.
    truckid = models.IntegerField(db_column='TruckID')  # Field name made lowercase.
    carno = models.CharField(db_column='CarNo', max_length=15, blank=True)  # Field name made lowercase.
    loadvalue = models.IntegerField(db_column='LoadValue', blank=True, null=True)  # Field name made lowercase.
    supercargoid = models.IntegerField(db_column='SuperCargoID', blank=True, null=True)  # Field name made lowercase.
    disptime = models.DateTimeField(db_column='DispTime', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tc_consignorderdriver'


class TcConsignorderheader(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    consignorderno = models.CharField(db_column='ConsignOrderNo', max_length=40, blank=True)  # Field name made lowercase.
    consignordertypecode = models.CharField(db_column='ConsignOrderTypeCode', max_length=40)  # Field name made lowercase.
    erpcono = models.CharField(db_column='ErpCoNo', max_length=40, blank=True)  # Field name made lowercase.
    iserpco = models.CharField(db_column='IsErpCo', max_length=1, blank=True)  # Field name made lowercase.
    statuscode = models.CharField(db_column='StatusCode', max_length=40, blank=True)  # Field name made lowercase.
    orderstatusid = models.IntegerField(db_column='OrderStatusID', blank=True, null=True)  # Field name made lowercase.
    deliverymodecode = models.CharField(db_column='DeliveryModeCode', max_length=40)  # Field name made lowercase.
    carrierid = models.IntegerField(db_column='CarrierID', blank=True, null=True)  # Field name made lowercase.
    carriername = models.CharField(db_column='CarrierName', max_length=100, blank=True)  # Field name made lowercase.
    carriernamenext = models.CharField(db_column='CarrierNameNext', max_length=100, blank=True)  # Field name made lowercase.
    loadstatus = models.CharField(db_column='LoadStatus', max_length=40, blank=True)  # Field name made lowercase.
    delayremark = models.CharField(db_column='DelayRemark', max_length=1000, blank=True)  # Field name made lowercase.
    dischargestatus = models.CharField(db_column='DischargeStatus', max_length=40, blank=True)  # Field name made lowercase.
    bidstatus = models.CharField(db_column='BidStatus', max_length=40)  # Field name made lowercase.
    bidid = models.IntegerField(db_column='BidID', blank=True, null=True)  # Field name made lowercase.
    ispassed = models.CharField(db_column='IsPassed', max_length=1, blank=True)  # Field name made lowercase.
    ispost = models.CharField(db_column='IsPost', max_length=1, blank=True)  # Field name made lowercase.
    transmode = models.CharField(db_column='TransMode', max_length=40, blank=True)  # Field name made lowercase.
    emptybucketnum = models.IntegerField(db_column='EmptyBucketNum', blank=True, null=True)  # Field name made lowercase.
    containernum = models.IntegerField(db_column='ContainerNum', blank=True, null=True)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    netweight = models.DecimalField(db_column='NetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    weightuomcode = models.CharField(db_column='WeightUomCode', max_length=40, blank=True)  # Field name made lowercase.
    shipingtypecode = models.CharField(db_column='ShipingTypeCode', max_length=40, blank=True)  # Field name made lowercase.
    shipmenttypecode = models.CharField(db_column='ShipmentTypeCode', max_length=40, blank=True)  # Field name made lowercase.
    shipmentroutecode = models.CharField(db_column='ShipmentRouteCode', max_length=40, blank=True)  # Field name made lowercase.
    shippingpointcode = models.CharField(db_column='ShippingPointCode', max_length=40)  # Field name made lowercase.
    fromprovinceid = models.IntegerField(db_column='FromProvinceID', blank=True, null=True)  # Field name made lowercase.
    fromcityid = models.IntegerField(db_column='FromCityID', blank=True, null=True)  # Field name made lowercase.
    fromdistrictid = models.IntegerField(db_column='FromDistrictID', blank=True, null=True)  # Field name made lowercase.
    additionalcharge = models.CharField(db_column='AdditionalCharge', max_length=1000, blank=True)  # Field name made lowercase.
    planningpointcode = models.CharField(db_column='PlanningPointCode', max_length=40)  # Field name made lowercase.
    reqloaddate = models.DateField(db_column='ReqLoadDate', blank=True, null=True)  # Field name made lowercase.
    reqdischargedate = models.DateField(db_column='ReqDischargeDate', blank=True, null=True)  # Field name made lowercase.
    actualloaddate = models.DateField(db_column='ActualLoadDate', blank=True, null=True)  # Field name made lowercase.
    actualdischargedate = models.DateField(db_column='ActualDischargeDate', blank=True, null=True)  # Field name made lowercase.
    stage = models.IntegerField(db_column='Stage', blank=True, null=True)  # Field name made lowercase.
    isselect = models.CharField(db_column='IsSelect', max_length=1, blank=True)  # Field name made lowercase.
    isupdate = models.CharField(db_column='IsUpdate', max_length=1, blank=True)  # Field name made lowercase.
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1)  # Field name made lowercase.
    evaluationid = models.CharField(db_column='EvaluationID', max_length=50, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    consigntime = models.DateTimeField(db_column='ConsignTime', blank=True, null=True)  # Field name made lowercase.
    scheduletime = models.DateTimeField(db_column='ScheduleTime', blank=True, null=True)  # Field name made lowercase.
    loadstarttime = models.DateTimeField(db_column='LoadStartTime', blank=True, null=True)  # Field name made lowercase.
    loadendtime = models.DateTimeField(db_column='LoadEndTime', blank=True, null=True)  # Field name made lowercase.
    receiptdate = models.DateField(db_column='ReceiptDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tc_consignorderheader'


class TcConsignorderline(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    headerid = models.IntegerField(db_column='HeaderID')  # Field name made lowercase.
    loconsignid = models.CharField(db_column='LoConsignID', max_length=10, blank=True)  # Field name made lowercase.
    dono = models.CharField(db_column='DoNo', max_length=40, blank=True)  # Field name made lowercase.
    lolid = models.IntegerField(db_column='LolID')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=60, blank=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=60, blank=True)  # Field name made lowercase.
    itemspec = models.CharField(db_column='ItemSpec', max_length=60, blank=True)  # Field name made lowercase.
    seqno = models.CharField(db_column='SeqNo', max_length=40, blank=True)  # Field name made lowercase.
    plantcode = models.CharField(db_column='PlantCode', max_length=60, blank=True)  # Field name made lowercase.
    fromwarehouseid = models.IntegerField(db_column='FromWarehouseID', blank=True, null=True)  # Field name made lowercase.
    loadstatus = models.CharField(db_column='LoadStatus', max_length=40, blank=True)  # Field name made lowercase.
    dischargestatus = models.CharField(db_column='DischargeStatus', max_length=40, blank=True)  # Field name made lowercase.
    consignqty = models.DecimalField(db_column='ConsignQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loadqty = models.DecimalField(db_column='LoadQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    dischargeqty = models.DecimalField(db_column='DischargeQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    uomcode = models.CharField(db_column='UomCode', max_length=40, blank=True)  # Field name made lowercase.
    consignqty2 = models.DecimalField(db_column='ConsignQty2', max_digits=18, decimal_places=6)  # Field name made lowercase.
    consignuomcode2 = models.CharField(db_column='ConsignUomCode2', max_length=40, blank=True)  # Field name made lowercase.
    loadqty2 = models.DecimalField(db_column='LoadQty2', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loaduomcode2 = models.CharField(db_column='LoadUomCode2', max_length=40, blank=True)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loadnetweight = models.DecimalField(db_column='LoadNetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    weightuomcode = models.CharField(db_column='WeightUomCode', max_length=40)  # Field name made lowercase.
    consignpiece = models.DecimalField(db_column='ConsignPiece', max_digits=10, decimal_places=0)  # Field name made lowercase.
    loadpiece = models.DecimalField(db_column='LoadPiece', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dischargepiece = models.DecimalField(db_column='DischargePiece', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lostpiece = models.DecimalField(db_column='LostPiece', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    damagepiece = models.DecimalField(db_column='DamagePiece', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lostqty = models.DecimalField(db_column='LostQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    damageqty = models.DecimalField(db_column='DamageQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1)  # Field name made lowercase.
    valuationtype = models.CharField(db_column='ValuationType', max_length=200, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tc_consignorderline'


class TcConsignorderlo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    headerid = models.IntegerField(db_column='HeaderID')  # Field name made lowercase.
    logisticsid = models.IntegerField(db_column='LogisticsID')  # Field name made lowercase.
    erporderno = models.CharField(db_column='ErpOrderNo', max_length=10, blank=True)  # Field name made lowercase.
    dono = models.CharField(db_column='DoNo', max_length=40, blank=True)  # Field name made lowercase.
    shippingpoint = models.CharField(db_column='ShippingPoint', max_length=40, blank=True)  # Field name made lowercase.
    deliverymodecode = models.CharField(db_column='DeliveryModeCode', max_length=40)  # Field name made lowercase.
    pickupperson = models.CharField(db_column='PickupPerson', max_length=40, blank=True)  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WarehouseID')  # Field name made lowercase.
    pickuptruckno = models.CharField(db_column='PickupTruckNo', max_length=40, blank=True)  # Field name made lowercase.
    shiptoid = models.IntegerField(db_column='ShipToID', blank=True, null=True)  # Field name made lowercase.
    soldtoid = models.IntegerField(db_column='SoldToID', blank=True, null=True)  # Field name made lowercase.
    toprovinceid = models.IntegerField(db_column='ToProvinceID', blank=True, null=True)  # Field name made lowercase.
    tocityid = models.IntegerField(db_column='ToCityID', blank=True, null=True)  # Field name made lowercase.
    todistrictid = models.IntegerField(db_column='ToDistrictID', blank=True, null=True)  # Field name made lowercase.
    totownid = models.IntegerField(db_column='ToTownID', blank=True, null=True)  # Field name made lowercase.
    towarehouseid = models.IntegerField(db_column='ToWarehouseID', blank=True, null=True)  # Field name made lowercase.
    receiver = models.CharField(db_column='Receiver', max_length=40, blank=True)  # Field name made lowercase.
    receiverphoneno = models.CharField(db_column='ReceiverPhoneNo', max_length=40, blank=True)  # Field name made lowercase.
    toaddress = models.CharField(db_column='ToAddress', max_length=250, blank=True)  # Field name made lowercase.
    reqloaddate = models.DateField(db_column='ReqLoadDate', blank=True, null=True)  # Field name made lowercase.
    actualloaddate = models.DateField(db_column='ActualLoadDate', blank=True, null=True)  # Field name made lowercase.
    reqdischargedate = models.DateField(db_column='ReqDischargeDate', blank=True, null=True)  # Field name made lowercase.
    actualdischargedate = models.DateField(db_column='ActualDischargeDate', blank=True, null=True)  # Field name made lowercase.
    tozipcode = models.CharField(db_column='ToZipCode', max_length=10, blank=True)  # Field name made lowercase.
    consignqty = models.DecimalField(db_column='ConsignQty', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loadqty = models.DecimalField(db_column='LoadQty', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dischargeqty = models.DecimalField(db_column='DischargeQty', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    uomcode = models.CharField(db_column='UomCode', max_length=255, blank=True)  # Field name made lowercase.
    consignqty2 = models.DecimalField(db_column='ConsignQty2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    consignuomcode2 = models.CharField(db_column='ConsignUomCode2', max_length=255, blank=True)  # Field name made lowercase.
    loadqty2 = models.DecimalField(db_column='LoadQty2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loaduomcode2 = models.CharField(db_column='LoadUomCode2', max_length=255, blank=True)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loadnetweight = models.DecimalField(db_column='LoadNetWeight', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    weightuomcode = models.CharField(db_column='WeightUomCode', max_length=255, blank=True)  # Field name made lowercase.
    consignpiece = models.DecimalField(db_column='ConsignPiece', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loadpiece = models.DecimalField(db_column='LoadPiece', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dischargepiece = models.DecimalField(db_column='DischargePiece', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lostpiece = models.DecimalField(db_column='LostPiece', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    damagepiece = models.DecimalField(db_column='DamagePiece', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lostqty = models.DecimalField(db_column='LostQty', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    damageqty = models.DecimalField(db_column='DamageQty', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    loadstatus = models.CharField(db_column='LoadStatus', max_length=255, blank=True)  # Field name made lowercase.
    dischargestatus = models.CharField(db_column='DischargeStatus', max_length=255, blank=True)  # Field name made lowercase.
    soldtocode = models.CharField(db_column='SoldToCode', max_length=255, blank=True)  # Field name made lowercase.
    soldtoname = models.CharField(db_column='SoldToName', max_length=255, blank=True)  # Field name made lowercase.
    shiptocode = models.CharField(db_column='ShipToCode', max_length=255, blank=True)  # Field name made lowercase.
    shiptoname = models.CharField(db_column='ShipToName', max_length=255, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tc_consignorderlo'


class TcConsignstatus(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    consignid = models.IntegerField(db_column='ConsignID')  # Field name made lowercase.
    statusno = models.CharField(db_column='StatusNo', max_length=40, blank=True)  # Field name made lowercase.
    statustime = models.DateTimeField(db_column='StatusTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tc_consignstatus'


class TcEvaluation(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    coid = models.IntegerField(db_column='CoID', blank=True, null=True)  # Field name made lowercase.
    erpcono = models.CharField(db_column='ErpCoNo', max_length=40, blank=True)  # Field name made lowercase.
    evaluationcontent = models.CharField(db_column='EvaluationContent', max_length=4000, blank=True)  # Field name made lowercase.
    evaluationgrade = models.IntegerField(db_column='EvaluationGrade', blank=True, null=True)  # Field name made lowercase.
    evaluationdate = models.DateTimeField(db_column='EvaluationDate', blank=True, null=True)  # Field name made lowercase.
    consignid = models.IntegerField(db_column='ConsignID')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=40, blank=True)  # Field name made lowercase.
    statedesc = models.CharField(db_column='StateDesc', max_length=200, blank=True)  # Field name made lowercase.
    appealstate = models.CharField(db_column='AppealState', max_length=3, blank=True)  # Field name made lowercase.
    satisfactionstate = models.CharField(db_column='SatisfactionState', max_length=3, blank=True)  # Field name made lowercase.
    satisfactionstatedesc = models.CharField(db_column='SatisfactionStateDesc', max_length=10, blank=True)  # Field name made lowercase.
    complaintsitem = models.CharField(db_column='ComplaintsItem', max_length=3, blank=True)  # Field name made lowercase.
    complaintscontent = models.CharField(db_column='ComplaintsContent', max_length=200, blank=True)  # Field name made lowercase.
    complaintsitemdesc = models.CharField(db_column='ComplaintsItemDesc', max_length=10, blank=True)  # Field name made lowercase.
    receiptdate = models.DateTimeField(db_column='ReceiptDate', blank=True, null=True)  # Field name made lowercase.
    evaluatedate = models.DateTimeField(db_column='EvaluateDate', blank=True, null=True)  # Field name made lowercase.
    receiptuser = models.CharField(db_column='ReceiptUser', max_length=50, blank=True)  # Field name made lowercase.
    receiptunitcode = models.CharField(db_column='ReceiptUnitCode', max_length=50, blank=True)  # Field name made lowercase.
    receiptunitname = models.CharField(db_column='ReceiptUnitName', max_length=50, blank=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tc_evaluation'


class TcWaybillheader(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    consignorderid = models.IntegerField(db_column='ConsignOrderID')  # Field name made lowercase.
    consignorderno = models.CharField(db_column='ConsignOrderNo', max_length=20)  # Field name made lowercase.
    dischargestatus = models.CharField(db_column='DischargeStatus', max_length=40, blank=True)  # Field name made lowercase.
    waybillno = models.CharField(db_column='WaybillNo', max_length=40, blank=True)  # Field name made lowercase.
    statuscode = models.CharField(db_column='StatusCode', max_length=40, blank=True)  # Field name made lowercase.
    waybillstatusid = models.IntegerField(db_column='WaybillStatusID')  # Field name made lowercase.
    carrierid = models.IntegerField(db_column='CarrierID')  # Field name made lowercase.
    drivername = models.CharField(db_column='DriverName', max_length=20)  # Field name made lowercase.
    driverid = models.IntegerField(db_column='DriverID')  # Field name made lowercase.
    supercargoid = models.IntegerField(db_column='SupercargoID')  # Field name made lowercase.
    truckid = models.IntegerField(db_column='TruckID')  # Field name made lowercase.
    platenumber = models.CharField(db_column='PlateNumber', max_length=60, blank=True)  # Field name made lowercase.
    shipingtypecode = models.CharField(db_column='ShipingTypeCode', max_length=40, blank=True)  # Field name made lowercase.
    shipmenttypecode = models.CharField(db_column='ShipmentTypeCode', max_length=40, blank=True)  # Field name made lowercase.
    shipmentroutecode = models.CharField(db_column='ShipmentRouteCode', max_length=40, blank=True)  # Field name made lowercase.
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1)  # Field name made lowercase.
    loadgrossweight = models.DecimalField(db_column='LoadGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loadnetweight = models.DecimalField(db_column='LoadNetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    weightuomcode = models.CharField(db_column='WeightUomCode', max_length=40, blank=True)  # Field name made lowercase.
    consignqty = models.DecimalField(db_column='ConsignQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loadqty = models.DecimalField(db_column='LoadQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    dischargeqty = models.DecimalField(db_column='DischargeQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    damageqty = models.DecimalField(db_column='DamageQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lostqty = models.DecimalField(db_column='LostQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    uomcode = models.CharField(db_column='UomCode', max_length=40, blank=True)  # Field name made lowercase.
    qty2 = models.DecimalField(db_column='Qty2', max_digits=18, decimal_places=6)  # Field name made lowercase.
    uomcode2 = models.CharField(db_column='UomCode2', max_length=40, blank=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tc_waybillheader'


class TcWaybillitemlot(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    cilid = models.IntegerField(db_column='CILID')  # Field name made lowercase.
    colid = models.IntegerField(db_column='COLID')  # Field name made lowercase.
    lotno = models.CharField(db_column='LotNo', max_length=200, blank=True)  # Field name made lowercase.
    consignqty = models.DecimalField(db_column='ConsignQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loadqty = models.DecimalField(db_column='LoadQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    valuationtype = models.CharField(db_column='ValuationType', max_length=200, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tc_waybillitemlot'


class TcWaybillline(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    headerid = models.IntegerField(db_column='HeaderID')  # Field name made lowercase.
    dono = models.CharField(db_column='DoNo', max_length=40, blank=True)  # Field name made lowercase.
    lowaybillid = models.IntegerField(db_column='LoWaybillID')  # Field name made lowercase.
    consignorderlineid = models.IntegerField(db_column='ConsignOrderLineID')  # Field name made lowercase.
    lolid = models.IntegerField(db_column='LolID')  # Field name made lowercase.
    dischargestatus = models.CharField(db_column='DischargeStatus', max_length=40, blank=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=60)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=60, blank=True)  # Field name made lowercase.
    itemspec = models.CharField(db_column='ItemSpec', max_length=60, blank=True)  # Field name made lowercase.
    plantcode = models.CharField(db_column='PlantCode', max_length=60, blank=True)  # Field name made lowercase.
    seqno = models.CharField(db_column='SeqNo', max_length=40, blank=True)  # Field name made lowercase.
    loadgrossweight = models.DecimalField(db_column='LoadGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loadnetweight = models.DecimalField(db_column='LoadNetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    weightuomcode = models.CharField(db_column='WeightUomCode', max_length=40, blank=True)  # Field name made lowercase.
    consignqty = models.DecimalField(db_column='ConsignQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loadqty = models.DecimalField(db_column='LoadQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    dischargeqty = models.DecimalField(db_column='DischargeQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    damageqty = models.DecimalField(db_column='DamageQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lostqty = models.DecimalField(db_column='LostQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    uomcode = models.CharField(db_column='UomCode', max_length=40, blank=True)  # Field name made lowercase.
    qty2 = models.DecimalField(db_column='Qty2', max_digits=18, decimal_places=6)  # Field name made lowercase.
    uomcode2 = models.CharField(db_column='UomCode2', max_length=40, blank=True)  # Field name made lowercase.
    paymentinstruction = models.CharField(db_column='PaymentInstruction', max_length=1000, blank=True)  # Field name made lowercase.
    posttime = models.DateTimeField(db_column='PostTime', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tc_waybillline'


class TcWaybilllo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    logisticsid = models.IntegerField(db_column='LogisticsID')  # Field name made lowercase.
    headerid = models.IntegerField(db_column='HeaderID')  # Field name made lowercase.
    erporderno = models.CharField(db_column='ErpOrderNo', max_length=40, blank=True)  # Field name made lowercase.
    dono = models.CharField(db_column='DoNo', max_length=40, blank=True)  # Field name made lowercase.
    dischargestatus = models.CharField(db_column='DischargeStatus', max_length=40, blank=True)  # Field name made lowercase.
    shippingpoint = models.CharField(db_column='ShippingPoint', max_length=40, blank=True)  # Field name made lowercase.
    deliverymodecode = models.CharField(db_column='DeliveryModeCode', max_length=40)  # Field name made lowercase.
    pickupperson = models.CharField(db_column='PickupPerson', max_length=40, blank=True)  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WarehouseID')  # Field name made lowercase.
    pickuptruckno = models.CharField(db_column='PickupTruckNo', max_length=40, blank=True)  # Field name made lowercase.
    shiptoid = models.IntegerField(db_column='ShipToID')  # Field name made lowercase.
    soldtoid = models.IntegerField(db_column='SoldToID', blank=True, null=True)  # Field name made lowercase.
    toprovinceid = models.IntegerField(db_column='ToProvinceID')  # Field name made lowercase.
    tocityid = models.IntegerField(db_column='ToCityID')  # Field name made lowercase.
    todistrictid = models.IntegerField(db_column='ToDistrictID')  # Field name made lowercase.
    totownid = models.IntegerField(db_column='ToTownID')  # Field name made lowercase.
    towarehouseid = models.IntegerField(db_column='ToWarehouseID', blank=True, null=True)  # Field name made lowercase.
    receiver = models.CharField(db_column='Receiver', max_length=40, blank=True)  # Field name made lowercase.
    receiverphoneno = models.CharField(db_column='ReceiverPhoneNo', max_length=40, blank=True)  # Field name made lowercase.
    toaddress = models.CharField(db_column='ToAddress', max_length=250, blank=True)  # Field name made lowercase.
    tozipcode = models.CharField(db_column='ToZipCode', max_length=10, blank=True)  # Field name made lowercase.
    compensation = models.CharField(db_column='Compensation', max_length=1000, blank=True)  # Field name made lowercase.
    reqloaddate = models.DateField(db_column='ReqLoadDate', blank=True, null=True)  # Field name made lowercase.
    actualloaddate = models.DateField(db_column='ActualLoadDate', blank=True, null=True)  # Field name made lowercase.
    reqdischargedate = models.DateField(db_column='ReqDischargeDate', blank=True, null=True)  # Field name made lowercase.
    actualdischargedate = models.DateField(db_column='ActualDischargeDate', blank=True, null=True)  # Field name made lowercase.
    billingtime = models.DateTimeField(db_column='BillingTime', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    loadgrossweight = models.DecimalField(db_column='LoadGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loadnetweight = models.DecimalField(db_column='LoadNetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    weightuomcode = models.CharField(db_column='WeightUomCode', max_length=40, blank=True)  # Field name made lowercase.
    consignqty = models.DecimalField(db_column='ConsignQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loadqty = models.DecimalField(db_column='LoadQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    dischargeqty = models.DecimalField(db_column='DischargeQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    damageqty = models.DecimalField(db_column='DamageQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lostqty = models.DecimalField(db_column='LostQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    uomcode = models.CharField(db_column='UomCode', max_length=40, blank=True)  # Field name made lowercase.
    qty2 = models.DecimalField(db_column='Qty2', max_digits=18, decimal_places=6)  # Field name made lowercase.
    uomcode2 = models.CharField(db_column='UomCode2', max_length=40, blank=True)  # Field name made lowercase.
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tc_waybilllo'


class TcWaybillstatus(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    waybillid = models.IntegerField(db_column='WaybillID')  # Field name made lowercase.
    statusno = models.CharField(db_column='StatusNo', max_length=40, blank=True)  # Field name made lowercase.
    statustime = models.DateTimeField(db_column='StatusTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tc_waybillstatus'

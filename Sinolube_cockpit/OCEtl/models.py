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

class TOcHostorderheader(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID', blank=True, null=True)  # Field name made lowercase.
    hostsystemno = models.CharField(db_column='HostSystemNo', max_length=40, blank=True)  # Field name made lowercase.
    hostorderno = models.CharField(db_column='hostOrderNo', max_length=40)  # Field name made lowercase.
    hostordercategory = models.CharField(db_column='HostOrderCategory', max_length=40, blank=True)  # Field name made lowercase.
    hostordertype = models.CharField(db_column='HostOrderType', max_length=40, blank=True)  # Field name made lowercase.
    docdate = models.DateField(db_column='DocDate', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID')  # Field name made lowercase.
    sporgcode = models.CharField(db_column='SpOrgCode', max_length=40, blank=True)  # Field name made lowercase.
    dccode = models.CharField(db_column='DcCode', max_length=40, blank=True)  # Field name made lowercase.
    spdeptcode = models.CharField(db_column='SpDeptCode', max_length=40, blank=True)  # Field name made lowercase.
    spgroupcode = models.CharField(db_column='SpGroupCode', max_length=40, blank=True)  # Field name made lowercase.
    salesofficecode = models.CharField(db_column='SalesOfficeCode', max_length=40, blank=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    deliverymodecode = models.CharField(db_column='DeliveryModeCode', max_length=40, blank=True)  # Field name made lowercase.
    expecttransmode = models.CharField(db_column='ExpectTransMode', max_length=40, blank=True)  # Field name made lowercase.
    fromwarehousecode = models.CharField(db_column='FromWarehouseCode', max_length=40, blank=True)  # Field name made lowercase.
    shippingpoint = models.CharField(db_column='ShippingPoint', max_length=40, blank=True)  # Field name made lowercase.
    routine = models.CharField(db_column='Routine', max_length=40, blank=True)  # Field name made lowercase.
    soldtoid = models.IntegerField(db_column='SoldToID', blank=True, null=True)  # Field name made lowercase.
    soldtocode = models.CharField(db_column='SoldToCode', max_length=40, blank=True)  # Field name made lowercase.
    soldtoname = models.CharField(db_column='SoldToName', max_length=255, blank=True)  # Field name made lowercase.
    soldtocontact = models.CharField(db_column='SoldToContact', max_length=40, blank=True)  # Field name made lowercase.
    soldtophoneno = models.CharField(db_column='SoldToPhoneNo', max_length=40, blank=True)  # Field name made lowercase.
    shiptoid = models.IntegerField(db_column='ShipToID', blank=True, null=True)  # Field name made lowercase.
    shiptocode = models.CharField(db_column='ShipToCode', max_length=40, blank=True)  # Field name made lowercase.
    shiptoname = models.CharField(db_column='ShipToName', max_length=100, blank=True)  # Field name made lowercase.
    toprovinceid = models.IntegerField(db_column='ToProvinceID')  # Field name made lowercase.
    tocityid = models.IntegerField(db_column='ToCityID')  # Field name made lowercase.
    todistrictid = models.IntegerField(db_column='ToDistrictID', blank=True, null=True)  # Field name made lowercase.
    totownid = models.IntegerField(db_column='ToTownID', blank=True, null=True)  # Field name made lowercase.
    toprovincecode = models.CharField(db_column='ToProvinceCode', max_length=40, blank=True)  # Field name made lowercase.
    tocitycode = models.CharField(db_column='ToCityCode', max_length=40, blank=True)  # Field name made lowercase.
    todistrictcode = models.CharField(db_column='ToDistrictCode', max_length=40, blank=True)  # Field name made lowercase.
    totowncode = models.CharField(db_column='ToTownCode', max_length=40, blank=True)  # Field name made lowercase.
    towarehouseid = models.IntegerField(db_column='ToWarehouseID', blank=True, null=True)  # Field name made lowercase.
    receiver = models.CharField(db_column='Receiver', max_length=40, blank=True)  # Field name made lowercase.
    receiverphoneno = models.CharField(db_column='ReceiverPhoneNo', max_length=40, blank=True)  # Field name made lowercase.
    toaddress = models.CharField(db_column='ToAddress', max_length=250, blank=True)  # Field name made lowercase.
    tozipcode = models.CharField(db_column='ToZipCode', max_length=10, blank=True)  # Field name made lowercase.
    pickupperson = models.CharField(db_column='PickupPerson', max_length=40, blank=True)  # Field name made lowercase.
    pickuptruckno = models.CharField(db_column='PickupTruckNo', max_length=40, blank=True)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=40, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    tostationid = models.IntegerField(db_column='ToStationID', blank=True, null=True)  # Field name made lowercase.
    toprivateline = models.CharField(db_column='ToPrivateLine', max_length=100, blank=True)  # Field name made lowercase.
    loadportid = models.IntegerField(db_column='LoadPortID', blank=True, null=True)  # Field name made lowercase.
    dischargeportid = models.IntegerField(db_column='DischargePortID', blank=True, null=True)  # Field name made lowercase.
    orderqty = models.DecimalField(db_column='OrderQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    netweight = models.DecimalField(db_column='NetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    weightuomcode = models.CharField(db_column='WeightUomCode', max_length=40, blank=True)  # Field name made lowercase.
    carrierid = models.IntegerField(db_column='CarrierID', blank=True, null=True)  # Field name made lowercase.
    deliverygenstatus = models.CharField(db_column='DeliveryGenStatus', max_length=10)  # Field name made lowercase.
    specialflag = models.CharField(db_column='SpecialFlag', max_length=40, blank=True)  # Field name made lowercase.
    releasestatus = models.CharField(db_column='ReleaseStatus', max_length=40)  # Field name made lowercase.
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1)  # Field name made lowercase.
    hostapprovestatus = models.CharField(db_column='HostApproveStatus', max_length=40, blank=True)  # Field name made lowercase.
    hostsummarystatus = models.CharField(db_column='HostSummaryStatus', max_length=100, blank=True)  # Field name made lowercase.
    hostpono = models.CharField(db_column='HostPoNo', max_length=40, blank=True)  # Field name made lowercase.
    hostintltrterm1 = models.CharField(db_column='HostIntlTrTerm1', max_length=40, blank=True)  # Field name made lowercase.
    hostintltrterm2 = models.CharField(db_column='HostIntlTrTerm2', max_length=40, blank=True)  # Field name made lowercase.
    hostreqdeliverydate = models.DateField(db_column='HostReqDeliveryDate', blank=True, null=True)  # Field name made lowercase.
    hostordercause = models.CharField(db_column='HostOrderCause', max_length=40, blank=True)  # Field name made lowercase.
    hostspecialflag = models.CharField(db_column='HostSpecialFlag', max_length=40, blank=True)  # Field name made lowercase.
    isspit = models.CharField(db_column='IsSpit', max_length=10, blank=True)  # Field name made lowercase.
    hostsalesarea = models.CharField(db_column='HostSalesArea', max_length=40, blank=True)  # Field name made lowercase.
    issuedbycode = models.CharField(db_column='IssuedByCode', max_length=40, blank=True)  # Field name made lowercase.
    issuedbyname = models.CharField(db_column='IssuedByName', max_length=40, blank=True)  # Field name made lowercase.
    issuedtime = models.DateTimeField(db_column='IssuedTime', blank=True, null=True)  # Field name made lowercase.
    closestatus = models.CharField(db_column='CloseStatus', max_length=40)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    expectarrivaldate = models.DateTimeField(db_column='ExpectArrivalDate', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    def  __unicode__(self):
        return unicode(self.id) or u''
    class Meta:
        managed = False
        db_table = 't_oc_hostorderheader'


class TOcHostorderline(models.Model):
    id = models.BigIntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    headerid = models.ForeignKey(TOcHostorderheader, 'id',db_column='HeaderID')  # Field name made lowercase.
    refid = models.BigIntegerField(db_column='RefID', blank=True, null=True)  # Field name made lowercase.
    seqno = models.CharField(db_column='SeqNo', max_length=40, blank=True)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=40, blank=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=100, blank=True)  # Field name made lowercase.
    itemspec = models.CharField(db_column='ItemSpec', max_length=100, blank=True)  # Field name made lowercase.
    shiptoid = models.IntegerField(db_column='ShipToID', blank=True, null=True)  # Field name made lowercase.
    receiver = models.CharField(db_column='Receiver', max_length=40, blank=True)  # Field name made lowercase.
    receiverphoneno = models.CharField(db_column='ReceiverPhoneNo', max_length=40, blank=True)  # Field name made lowercase.
    toaddress = models.CharField(db_column='ToAddress', max_length=250, blank=True)  # Field name made lowercase.
    tozipcode = models.CharField(db_column='ToZipCode', max_length=10, blank=True)  # Field name made lowercase.
    lotno = models.CharField(db_column='LotNo', max_length=200, blank=True)  # Field name made lowercase.
    lotno1 = models.CharField(db_column='LotNo1', max_length=200, blank=True)  # Field name made lowercase.
    lotno2 = models.CharField(db_column='LotNo2', max_length=200, blank=True)  # Field name made lowercase.
    lotno3 = models.CharField(db_column='LotNo3', max_length=200, blank=True)  # Field name made lowercase.
    lotno4 = models.CharField(db_column='LotNo4', max_length=200, blank=True)  # Field name made lowercase.
    lotno5 = models.CharField(db_column='LotNo5', max_length=200, blank=True)  # Field name made lowercase.
    lotno6 = models.CharField(db_column='LotNo6', max_length=200, blank=True)  # Field name made lowercase.
    lotno7 = models.CharField(db_column='LotNo7', max_length=200, blank=True)  # Field name made lowercase.
    lotno8 = models.CharField(db_column='LotNo8', max_length=200, blank=True)  # Field name made lowercase.
    lotno9 = models.CharField(db_column='LotNo9', max_length=200, blank=True)  # Field name made lowercase.
    lotno10 = models.CharField(db_column='LotNo10', max_length=200, blank=True)  # Field name made lowercase.
    lotno11 = models.CharField(db_column='LotNo11', max_length=200, blank=True)  # Field name made lowercase.
    lotno12 = models.CharField(db_column='LotNo12', max_length=200, blank=True)  # Field name made lowercase.
    lotno13 = models.CharField(db_column='LotNo13', max_length=200, blank=True)  # Field name made lowercase.
    lotno14 = models.CharField(db_column='LotNo14', max_length=200, blank=True)  # Field name made lowercase.
    lotno15 = models.CharField(db_column='LotNo15', max_length=200, blank=True)  # Field name made lowercase.
    lotno16 = models.CharField(db_column='LotNo16', max_length=200, blank=True)  # Field name made lowercase.
    lotno17 = models.CharField(db_column='LotNo17', max_length=200, blank=True)  # Field name made lowercase.
    lotno18 = models.CharField(db_column='LotNo18', max_length=200, blank=True)  # Field name made lowercase.
    lotno19 = models.CharField(db_column='LotNo19', max_length=200, blank=True)  # Field name made lowercase.
    lotno20 = models.CharField(db_column='LotNo20', max_length=200, blank=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    uomcode = models.CharField(db_column='UomCode', max_length=40, blank=True)  # Field name made lowercase.
    qty2 = models.DecimalField(db_column='Qty2', max_digits=18, decimal_places=6)  # Field name made lowercase.
    uomcode2 = models.CharField(db_column='UomCode2', max_length=40, blank=True)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    netweight = models.DecimalField(db_column='NetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    specialqty1 = models.DecimalField(db_column='SpecialQty1', max_digits=18, decimal_places=6)  # Field name made lowercase.
    specialqty2 = models.DecimalField(db_column='SpecialQty2', max_digits=18, decimal_places=6)  # Field name made lowercase.
    specialqty3 = models.DecimalField(db_column='SpecialQty3', max_digits=18, decimal_places=6)  # Field name made lowercase.
    weightuomcode = models.CharField(db_column='WeightUomCode', max_length=40, blank=True)  # Field name made lowercase.
    tolerancelower = models.DecimalField(db_column='ToleranceLower', max_digits=18, decimal_places=6)  # Field name made lowercase.
    toleranceupper = models.DecimalField(db_column='ToleranceUpper', max_digits=18, decimal_places=6)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    fromwarehouseid = models.IntegerField(db_column='FromWarehouseID', blank=True, null=True)  # Field name made lowercase.
    toprovinceid = models.IntegerField(db_column='ToProvinceID', blank=True, null=True)  # Field name made lowercase.
    tocityid = models.IntegerField(db_column='ToCityID', blank=True, null=True)  # Field name made lowercase.
    todistrictid = models.IntegerField(db_column='ToDistrictID', blank=True, null=True)  # Field name made lowercase.
    totownid = models.IntegerField(db_column='ToTownID', blank=True, null=True)  # Field name made lowercase.
    towarehouseid = models.IntegerField(db_column='ToWarehouseID', blank=True, null=True)  # Field name made lowercase.
    expectdeliveydate = models.DateField(db_column='ExpectDeliveyDate', blank=True, null=True)  # Field name made lowercase.
    hostshippingpoint = models.CharField(db_column='HostShippingPoint', max_length=40, blank=True)  # Field name made lowercase.
    hostrejectcause = models.CharField(db_column='HostRejectCause', max_length=40, blank=True)  # Field name made lowercase.
    hostroute = models.CharField(db_column='HostRoute', max_length=40, blank=True)  # Field name made lowercase.
    hostdeliveryfrozenstatus = models.CharField(db_column='HostDeliveryFrozenStatus', max_length=40, blank=True)  # Field name made lowercase.
    hostshipmenttype = models.CharField(db_column='HostShipmentType', max_length=40, blank=True)  # Field name made lowercase.
    spotqty = models.DecimalField(db_column='SpotQty', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    deliveryqty = models.DecimalField(db_column='DeliveryQty', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    futureqty = models.DecimalField(db_column='FutureQty', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    future2spotqty = models.DecimalField(db_column='Future2SpotQty', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    demandqty = models.DecimalField(db_column='DemandQty', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 't_oc_hostorderline'


class TOcLogisticsorderheader(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    loorderno = models.CharField(db_column='LoOrderNo', max_length=40, blank=True)  # Field name made lowercase.
    hostsystemno = models.CharField(db_column='HostSystemNo', max_length=40, blank=True)  # Field name made lowercase.
    hostorderno = models.CharField(db_column='HostOrderNo', max_length=40, blank=True)  # Field name made lowercase.
    hostordercategory = models.CharField(db_column='HostOrderCategory', max_length=40, blank=True)  # Field name made lowercase.
    hostordertype = models.CharField(db_column='HostOrderType', max_length=40, blank=True)  # Field name made lowercase.
    relatedorderno = models.CharField(db_column='RelatedOrderNo', max_length=40, blank=True)  # Field name made lowercase.
    docdate = models.DateField(db_column='DocDate', blank=True, null=True)  # Field name made lowercase.
    movementtypecode = models.CharField(db_column='MovementTypeCode', max_length=40, blank=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID')  # Field name made lowercase.
    sporgcode = models.CharField(db_column='SpOrgCode', max_length=40, blank=True)  # Field name made lowercase.
    dccode = models.CharField(db_column='DcCode', max_length=40, blank=True)  # Field name made lowercase.
    spdeptcode = models.CharField(db_column='SpDeptCode', max_length=40, blank=True)  # Field name made lowercase.
    spgroupcode = models.CharField(db_column='SpGroupCode', max_length=40, blank=True)  # Field name made lowercase.
    salesofficecode = models.CharField(db_column='SalesOfficeCode', max_length=40, blank=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    deliverymodecode = models.CharField(db_column='DeliveryModeCode', max_length=40)  # Field name made lowercase.
    expecttransmode = models.CharField(db_column='ExpectTransMode', max_length=40, blank=True)  # Field name made lowercase.
    plantcode = models.CharField(db_column='PlantCode', max_length=40, blank=True)  # Field name made lowercase.
    fromwarehouseid = models.IntegerField(db_column='FromWarehouseID')  # Field name made lowercase.
    shippingpoint = models.CharField(db_column='ShippingPoint', max_length=40, blank=True)  # Field name made lowercase.
    routine = models.CharField(db_column='Routine', max_length=40, blank=True)  # Field name made lowercase.
    fromprovinceid = models.IntegerField(db_column='FromProvinceID', blank=True, null=True)  # Field name made lowercase.
    fromcityid = models.IntegerField(db_column='FromCityID', blank=True, null=True)  # Field name made lowercase.
    fromdistrictid = models.IntegerField(db_column='FromDistrictID', blank=True, null=True)  # Field name made lowercase.
    fromtownid = models.IntegerField(db_column='FromTownID', blank=True, null=True)  # Field name made lowercase.
    fromaddress = models.CharField(db_column='FromAddress', max_length=250, blank=True)  # Field name made lowercase.
    soldtoid = models.IntegerField(db_column='SoldToID', blank=True, null=True)  # Field name made lowercase.
    soldtocode = models.CharField(db_column='SoldToCode', max_length=40, blank=True)  # Field name made lowercase.
    soldtoname = models.CharField(db_column='SoldToName', max_length=100, blank=True)  # Field name made lowercase.
    soldtocontact = models.CharField(db_column='SoldToContact', max_length=40, blank=True)  # Field name made lowercase.
    soldtophoneno = models.CharField(db_column='SoldToPhoneNo', max_length=40, blank=True)  # Field name made lowercase.
    shiptoid = models.IntegerField(db_column='ShipToID', blank=True, null=True)  # Field name made lowercase.
    shiptocode = models.CharField(db_column='ShipToCode', max_length=40, blank=True)  # Field name made lowercase.
    shiptoname = models.CharField(db_column='ShipToName', max_length=100, blank=True)  # Field name made lowercase.
    toprovinceid = models.IntegerField(db_column='ToProvinceID', blank=True, null=True)  # Field name made lowercase.
    tocityid = models.IntegerField(db_column='ToCityID', blank=True, null=True)  # Field name made lowercase.
    todistrictid = models.IntegerField(db_column='ToDistrictID', blank=True, null=True)  # Field name made lowercase.
    totownid = models.IntegerField(db_column='ToTownID', blank=True, null=True)  # Field name made lowercase.
    toprovincecode = models.CharField(db_column='ToProvinceCode', max_length=40, blank=True)  # Field name made lowercase.
    tocitycode = models.CharField(db_column='ToCityCode', max_length=40, blank=True)  # Field name made lowercase.
    todistrictcode = models.CharField(db_column='ToDistrictCode', max_length=40, blank=True)  # Field name made lowercase.
    totowncode = models.CharField(db_column='ToTownCode', max_length=40, blank=True)  # Field name made lowercase.
    towarehouseid = models.IntegerField(db_column='ToWarehouseID', blank=True, null=True)  # Field name made lowercase.
    receiver = models.CharField(db_column='Receiver', max_length=40, blank=True)  # Field name made lowercase.
    receiverphoneno = models.CharField(db_column='ReceiverPhoneNo', max_length=40, blank=True)  # Field name made lowercase.
    toaddress = models.CharField(db_column='ToAddress', max_length=250, blank=True)  # Field name made lowercase.
    tozipcode = models.CharField(db_column='ToZipCode', max_length=10, blank=True)  # Field name made lowercase.
    pickupperson = models.CharField(db_column='PickupPerson', max_length=40, blank=True)  # Field name made lowercase.
    pickuptruckno = models.CharField(db_column='PickupTruckNo', max_length=40, blank=True)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=40, blank=True)  # Field name made lowercase.
    poststatus = models.CharField(db_column='PostStatus', max_length=40)  # Field name made lowercase.
    consignstatus = models.CharField(db_column='ConsignStatus', max_length=40)  # Field name made lowercase.
    loadstatus = models.CharField(db_column='LoadStatus', max_length=40)  # Field name made lowercase.
    trackstatus = models.CharField(db_column='TrackStatus', max_length=40)  # Field name made lowercase.
    dischargestatus = models.CharField(db_column='DischargeStatus', max_length=40)  # Field name made lowercase.
    signstatus = models.CharField(db_column='SignStatus', max_length=40)  # Field name made lowercase.
    dostatus = models.CharField(db_column='DoStatus', max_length=40, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    fromstationid = models.IntegerField(db_column='FromStationID', blank=True, null=True)  # Field name made lowercase.
    tostationid = models.IntegerField(db_column='ToStationID', blank=True, null=True)  # Field name made lowercase.
    toprivateline = models.CharField(db_column='ToPrivateLine', max_length=100, blank=True)  # Field name made lowercase.
    loadportid = models.IntegerField(db_column='LoadPortID', blank=True, null=True)  # Field name made lowercase.
    dischargeportid = models.IntegerField(db_column='DischargePortID', blank=True, null=True)  # Field name made lowercase.
    hosttransmodecode = models.CharField(db_column='HostTransModeCode', max_length=40, blank=True)  # Field name made lowercase.
    hostspecialflag = models.CharField(db_column='HostSpecialFlag', max_length=40, blank=True)  # Field name made lowercase.
    actualmovedate = models.DateField(db_column='ActualMoveDate', blank=True, null=True)  # Field name made lowercase.
    bizrange = models.CharField(db_column='BizRange', max_length=40, blank=True)  # Field name made lowercase.
    biztype1 = models.CharField(db_column='BizType1', max_length=40, blank=True)  # Field name made lowercase.
    biztype2 = models.CharField(db_column='BizType2', max_length=40, blank=True)  # Field name made lowercase.
    bizdetail = models.CharField(db_column='BizDetail', max_length=40, blank=True)  # Field name made lowercase.
    orderqty = models.DecimalField(db_column='OrderQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    uomcode = models.CharField(db_column='UomCode', max_length=40, blank=True)  # Field name made lowercase.
    orderqty2 = models.DecimalField(db_column='OrderQty2', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    uomcode2 = models.CharField(db_column='UomCode2', max_length=40, blank=True)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    netweight = models.DecimalField(db_column='NetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    weightuomcode = models.CharField(db_column='WeightUomCode', max_length=40, blank=True)  # Field name made lowercase.
    consignqty = models.DecimalField(db_column='ConsignQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    consignpiece = models.DecimalField(db_column='ConsignPiece', max_digits=10, decimal_places=0)  # Field name made lowercase.
    loadqty = models.DecimalField(db_column='LoadQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loadpiece = models.DecimalField(db_column='LoadPiece', max_digits=10, decimal_places=0)  # Field name made lowercase.
    dischargeqty = models.DecimalField(db_column='DischargeQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    dischargepiece = models.DecimalField(db_column='DischargePiece', max_digits=10, decimal_places=0)  # Field name made lowercase.
    damageqty = models.DecimalField(db_column='DamageQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    damagepiece = models.DecimalField(db_column='DamagePiece', max_digits=10, decimal_places=0)  # Field name made lowercase.
    lostqty = models.DecimalField(db_column='LostQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lostpiece = models.DecimalField(db_column='LostPiece', max_digits=10, decimal_places=0)  # Field name made lowercase.
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1, blank=True)  # Field name made lowercase.
    issuedbycode = models.CharField(db_column='IssuedByCode', max_length=40, blank=True)  # Field name made lowercase.
    issuedbyname = models.CharField(db_column='IssuedByName', max_length=40, blank=True)  # Field name made lowercase.
    issuedtime = models.DateTimeField(db_column='IssuedTime', blank=True, null=True)  # Field name made lowercase.
    releaseperson = models.CharField(db_column='ReleasePerson', max_length=60, blank=True)  # Field name made lowercase.
    releasetime = models.DateTimeField(db_column='ReleaseTime', blank=True, null=True)  # Field name made lowercase.
    consignperson = models.CharField(db_column='ConsignPerson', max_length=60, blank=True)  # Field name made lowercase.
    consigntime = models.DateTimeField(db_column='ConsignTime', blank=True, null=True)  # Field name made lowercase.
    postperson = models.CharField(db_column='PostPerson', max_length=60, blank=True)  # Field name made lowercase.
    posttime = models.DateTimeField(db_column='PostTime', blank=True, null=True)  # Field name made lowercase.
    trackperson = models.CharField(db_column='TrackPerson', max_length=60, blank=True)  # Field name made lowercase.
    tracktime = models.DateTimeField(db_column='TrackTime', blank=True, null=True)  # Field name made lowercase.
    signperson = models.CharField(db_column='SignPerson', max_length=60, blank=True)  # Field name made lowercase.
    signdate = models.DateTimeField(db_column='SignDate', blank=True, null=True)  # Field name made lowercase.
    cancelperson = models.CharField(db_column='CancelPerson', max_length=60, blank=True)  # Field name made lowercase.
    canceltime = models.DateTimeField(db_column='CancelTime', blank=True, null=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_oc_logisticsorderheader'


class TOcLogisticsorderline(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    headerid = models.ForeignKey(TOcLogisticsorderheader, db_column='HeaderID')  # Field name made lowercase.
    refid = models.BigIntegerField(db_column='RefID', blank=True, null=True)  # Field name made lowercase.
    seqno = models.CharField(db_column='SeqNo', max_length=40, blank=True)  # Field name made lowercase.
    vgpos = models.CharField(db_column='VGPOS', max_length=10, blank=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=40, blank=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=100, blank=True)  # Field name made lowercase.
    itemspec = models.CharField(db_column='ItemSpec', max_length=40, blank=True)  # Field name made lowercase.
    movementtypecode = models.CharField(db_column='MovementTypeCode', max_length=40, blank=True)  # Field name made lowercase.
    shiptoid = models.IntegerField(db_column='ShipToID', blank=True, null=True)  # Field name made lowercase.
    receiver = models.CharField(db_column='Receiver', max_length=40, blank=True)  # Field name made lowercase.
    toaddress = models.CharField(db_column='ToAddress', max_length=250, blank=True)  # Field name made lowercase.
    tozipcode = models.CharField(db_column='ToZipCode', max_length=10, blank=True)  # Field name made lowercase.
    lotno = models.CharField(db_column='LotNo', max_length=200, blank=True)  # Field name made lowercase.
    lotno1 = models.CharField(db_column='LotNo1', max_length=200, blank=True)  # Field name made lowercase.
    lotno2 = models.CharField(db_column='LotNo2', max_length=200, blank=True)  # Field name made lowercase.
    lotno3 = models.CharField(db_column='LotNo3', max_length=200, blank=True)  # Field name made lowercase.
    lotno4 = models.CharField(db_column='LotNo4', max_length=200, blank=True)  # Field name made lowercase.
    lotno5 = models.CharField(db_column='LotNo5', max_length=200, blank=True)  # Field name made lowercase.
    lotno6 = models.CharField(db_column='LotNo6', max_length=200, blank=True)  # Field name made lowercase.
    lotno7 = models.CharField(db_column='LotNo7', max_length=200, blank=True)  # Field name made lowercase.
    lotno8 = models.CharField(db_column='LotNo8', max_length=200, blank=True)  # Field name made lowercase.
    lotno9 = models.CharField(db_column='LotNo9', max_length=200, blank=True)  # Field name made lowercase.
    lotno10 = models.CharField(db_column='LotNo10', max_length=200, blank=True)  # Field name made lowercase.
    lotno11 = models.CharField(db_column='LotNo11', max_length=200, blank=True)  # Field name made lowercase.
    lotno12 = models.CharField(db_column='LotNo12', max_length=200, blank=True)  # Field name made lowercase.
    lotno13 = models.CharField(db_column='LotNo13', max_length=200, blank=True)  # Field name made lowercase.
    lotno14 = models.CharField(db_column='LotNo14', max_length=200, blank=True)  # Field name made lowercase.
    lotno15 = models.CharField(db_column='LotNo15', max_length=200, blank=True)  # Field name made lowercase.
    lotno16 = models.CharField(db_column='LotNo16', max_length=200, blank=True)  # Field name made lowercase.
    lotno17 = models.CharField(db_column='LotNo17', max_length=200, blank=True)  # Field name made lowercase.
    lotno18 = models.CharField(db_column='LotNo18', max_length=200, blank=True)  # Field name made lowercase.
    lotno19 = models.CharField(db_column='LotNo19', max_length=200, blank=True)  # Field name made lowercase.
    lotno20 = models.CharField(db_column='LotNo20', max_length=200, blank=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    uomcode = models.CharField(db_column='UomCode', max_length=40, blank=True)  # Field name made lowercase.
    qty2 = models.DecimalField(db_column='Qty2', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    uomcode2 = models.CharField(db_column='UomCode2', max_length=40, blank=True)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    netweight = models.DecimalField(db_column='NetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    weightuomcode = models.CharField(db_column='WeightUomCode', max_length=40, blank=True)  # Field name made lowercase.
    tolerancelower = models.DecimalField(db_column='ToleranceLower', max_digits=18, decimal_places=6)  # Field name made lowercase.
    toleranceupper = models.DecimalField(db_column='ToleranceUpper', max_digits=18, decimal_places=6)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    fromwarehouseid = models.IntegerField(db_column='FromWarehouseID', blank=True, null=True)  # Field name made lowercase.
    shippingpoint = models.CharField(db_column='ShippingPoint', max_length=40, blank=True)  # Field name made lowercase.
    fromprovinceid = models.IntegerField(db_column='FromProvinceID', blank=True, null=True)  # Field name made lowercase.
    fromcityid = models.IntegerField(db_column='FromCityID', blank=True, null=True)  # Field name made lowercase.
    fromdistrictid = models.IntegerField(db_column='FromDistrictID', blank=True, null=True)  # Field name made lowercase.
    fromtownid = models.IntegerField(db_column='FromTownID', blank=True, null=True)  # Field name made lowercase.
    toprovinceid = models.IntegerField(db_column='ToProvinceID', blank=True, null=True)  # Field name made lowercase.
    tocityid = models.IntegerField(db_column='ToCityID', blank=True, null=True)  # Field name made lowercase.
    todistrictid = models.IntegerField(db_column='ToDistrictID', blank=True, null=True)  # Field name made lowercase.
    totownid = models.IntegerField(db_column='ToTownID', blank=True, null=True)  # Field name made lowercase.
    towarehouseid = models.IntegerField(db_column='ToWarehouseID', blank=True, null=True)  # Field name made lowercase.
    consignqty = models.DecimalField(db_column='ConsignQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    consignpiece = models.DecimalField(db_column='ConsignPiece', max_digits=10, decimal_places=0)  # Field name made lowercase.
    loadqty = models.DecimalField(db_column='LoadQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loadpiece = models.DecimalField(db_column='LoadPiece', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loadgrossweight = models.DecimalField(db_column='LoadGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loadnetweight = models.DecimalField(db_column='LoadNetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    dischargeqty = models.DecimalField(db_column='DischargeQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    dischargepiece = models.DecimalField(db_column='DischargePiece', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    damageqty = models.DecimalField(db_column='DamageQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    damagepiece = models.DecimalField(db_column='DamagePiece', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lostqty = models.DecimalField(db_column='LostQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lostpiece = models.DecimalField(db_column='LostPiece', max_digits=10, decimal_places=0)  # Field name made lowercase.
    consignstatus = models.CharField(db_column='ConsignStatus', max_length=40)  # Field name made lowercase.
    loadstatus = models.CharField(db_column='LoadStatus', max_length=40)  # Field name made lowercase.
    dischargestatus = models.CharField(db_column='DischargeStatus', max_length=40)  # Field name made lowercase.
    hostdeliveryqty = models.DecimalField(db_column='HostDeliveryQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    receiverphoneno = models.CharField(db_column='ReceiverPhoneNo', max_length=40, blank=True)  # Field name made lowercase.
    fromaddress = models.CharField(db_column='FromAddress', max_length=255, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_oc_logisticsorderline'


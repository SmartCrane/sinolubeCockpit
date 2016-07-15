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


class WcsInVoucherhead(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    voucherno = models.CharField(db_column='VoucherNo', max_length=40)  # Field name made lowercase.
    deorderno = models.CharField(db_column='DeOrderNo', max_length=40, blank=True)  # Field name made lowercase.
    biztype = models.CharField(db_column='BizType', max_length=40)  # Field name made lowercase.
    vendorno = models.CharField(db_column='VendorNo', max_length=40)  # Field name made lowercase.
    vendorid = models.IntegerField(db_column='VendorID')  # Field name made lowercase.
    vendortel = models.CharField(db_column='VendorTel', max_length=100, blank=True)  # Field name made lowercase.
    carrierid = models.IntegerField(db_column='CarrierID')  # Field name made lowercase.
    transportmodecode = models.CharField(db_column='TransportModeCode', max_length=40)  # Field name made lowercase.
    movetype = models.CharField(db_column='MoveType', max_length=40)  # Field name made lowercase.
    specialstock = models.CharField(db_column='SpecialStock', max_length=40, blank=True)  # Field name made lowercase.
    planintime = models.DateTimeField(db_column='PlanInTime', blank=True, null=True)  # Field name made lowercase.
    relatedorderno = models.CharField(db_column='RelatedOrderNo', max_length=40, blank=True)  # Field name made lowercase.
    docdate = models.DateField(db_column='DocDate', blank=True, null=True)  # Field name made lowercase.
    ordertotalqty = models.DecimalField(db_column='OrderTotalQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    orderfinishedlqty = models.DecimalField(db_column='OrderFinishedlQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    netweight = models.DecimalField(db_column='NetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1)  # Field name made lowercase.
    postingstatus = models.CharField(db_column='PostingStatus', max_length=40, blank=True)  # Field name made lowercase.
    voucherstatus = models.CharField(db_column='VoucherStatus', max_length=40, blank=True)  # Field name made lowercase.
    isoffset = models.CharField(db_column='IsOffset', max_length=1)  # Field name made lowercase.
    purvoucherno = models.CharField(db_column='PurVoucherNo', max_length=40, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_in_voucherhead'


class WcsInVoucherline(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    headerid = models.ForeignKey(WcsInVoucherhead,db_column='HeaderID')  # Field name made lowercase.
    matreialvoucherno = models.CharField(db_column='MatreialVoucherNo', max_length=40, blank=True)  # Field name made lowercase.
    seqno = models.CharField(db_column='SeqNo', max_length=40, blank=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    uomcode = models.CharField(db_column='UomCode', max_length=40)  # Field name made lowercase.
    orderqty = models.DecimalField(db_column='OrderQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    finishedlqty = models.DecimalField(db_column='FinishedlQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    waitlnqty = models.DecimalField(db_column='WaitlnQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    actualinqty = models.DecimalField(db_column='ActualInQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    netweight = models.DecimalField(db_column='NetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    movetype = models.CharField(db_column='MoveType', max_length=40)  # Field name made lowercase.
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
    orderstatus = models.CharField(db_column='OrderStatus', max_length=40, blank=True)  # Field name made lowercase.
    stockaddressid = models.IntegerField(db_column='StockAddressID')  # Field name made lowercase.
    postingstatus = models.CharField(db_column='PostingStatus', max_length=40, blank=True)  # Field name made lowercase.
    postinttime = models.DateTimeField(db_column='PostintTime', blank=True, null=True)  # Field name made lowercase.
    isoffset = models.CharField(db_column='IsOffset', max_length=255)  # Field name made lowercase.
    specialstockmark = models.CharField(db_column='SpecialStockMark', max_length=40, blank=True)  # Field name made lowercase.
    vouchelineid = models.IntegerField(db_column='VoucheLineID', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_in_voucherline'


class WcsInVouchervehicle(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineID')  # Field name made lowercase.
    tructid = models.IntegerField(db_column='TructID')  # Field name made lowercase.
    vehicleno = models.CharField(db_column='VehicleNo', max_length=40)  # Field name made lowercase.
    drivername = models.CharField(db_column='DriverName', max_length=40)  # Field name made lowercase.
    driveridno = models.CharField(db_column='DriverIDNo', max_length=40)  # Field name made lowercase.
    driverphoneno = models.CharField(db_column='DriverPhoneNo', max_length=100, blank=True)  # Field name made lowercase.
    deadweight = models.DecimalField(db_column='DeadWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loaduomid = models.IntegerField(db_column='LoadUomID')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=18, decimal_places=6)  # Field name made lowercase.
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
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_in_vouchervehicle'


class WcsOutCardread(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    drivername = models.CharField(db_column='DriverName', max_length=40)  # Field name made lowercase.
    driveridno = models.CharField(db_column='DriverIDNo', max_length=40)  # Field name made lowercase.
    driverid = models.IntegerField(db_column='DriverID', blank=True, null=True)  # Field name made lowercase.
    consignid = models.IntegerField(db_column='ConsignID', blank=True, null=True)  # Field name made lowercase.
    drivertel = models.CharField(db_column='DriverTel', max_length=100, blank=True)  # Field name made lowercase.
    carrierid = models.IntegerField(db_column='CarrierID', blank=True, null=True)  # Field name made lowercase.
    carriername = models.CharField(db_column='CarrierName', max_length=200, blank=True)  # Field name made lowercase.
    transportmodecode = models.CharField(db_column='TransportModeCode', max_length=40, blank=True)  # Field name made lowercase.
    tructid = models.IntegerField(db_column='TructID')  # Field name made lowercase.
    vehicleno = models.CharField(db_column='VehicleNo', max_length=40)  # Field name made lowercase.
    transporttimes = models.IntegerField(db_column='TransportTimes')  # Field name made lowercase.
    readtime = models.DateTimeField(db_column='ReadTime')  # Field name made lowercase.
    clientip = models.CharField(db_column='ClientIP', max_length=15)  # Field name made lowercase.
    cilenthost = models.CharField(db_column='CilentHost', max_length=80, blank=True)  # Field name made lowercase.
    clientos = models.CharField(db_column='ClientOS', max_length=80, blank=True)  # Field name made lowercase.
    carddeviceno = models.CharField(db_column='CardDeviceNo', max_length=40, blank=True)  # Field name made lowercase.
    recordstatus = models.CharField(db_column='RecordStatus', max_length=40, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_out_cardread'


class WcsOutCardreadsvoucher(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recordid = models.IntegerField(db_column='RecordID')  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    voucherno = models.CharField(db_column='VoucherNo', max_length=40, blank=True)  # Field name made lowercase.
    smallvoucherno = models.CharField(db_column='SmallVoucherNo', max_length=40, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_out_cardreadsvoucher'


class WcsOutVoucherdeorder(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    deorderno = models.CharField(db_column='DeOrderNo', max_length=40)  # Field name made lowercase.
    headerid = models.IntegerField(db_column='HeaderID')  # Field name made lowercase.
    orderno = models.CharField(db_column='OrderNo', max_length=40, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_out_voucherdeorder'


class WcsOutVoucherhead(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    voucherno = models.CharField(db_column='VoucherNo', max_length=40)  # Field name made lowercase.
    smallvoucherno = models.CharField(db_column='SmallVoucherNo', max_length=40)  # Field name made lowercase.
    shipmentroute = models.CharField(db_column='ShipmentRoute', max_length=40)  # Field name made lowercase.
    carrierid = models.IntegerField(db_column='CarrierID')  # Field name made lowercase.
    tructid = models.IntegerField(db_column='TructID')  # Field name made lowercase.
    vehicleno = models.CharField(db_column='VehicleNo', max_length=40)  # Field name made lowercase.
    drivername = models.CharField(db_column='DriverName', max_length=40)  # Field name made lowercase.
    driveridno = models.CharField(db_column='DriverIDNo', max_length=40)  # Field name made lowercase.
    driverphoneno = models.CharField(db_column='DriverPhoneNo', max_length=100, blank=True)  # Field name made lowercase.
    deadweight = models.DecimalField(db_column='DeadWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loaduomid = models.IntegerField(db_column='LoadUomID')  # Field name made lowercase.
    cardreadid = models.IntegerField(db_column='CardReadID')  # Field name made lowercase.
    planouttime = models.DateTimeField(db_column='PlanOutTime', blank=True, null=True)  # Field name made lowercase.
    relatedorderno = models.CharField(db_column='RelatedOrderNo', max_length=40, blank=True)  # Field name made lowercase.
    docdate = models.DateField(db_column='DocDate', blank=True, null=True)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    netweight = models.DecimalField(db_column='NetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1)  # Field name made lowercase.
    voucherstatus = models.CharField(db_column='VoucherStatus', max_length=40, blank=True)  # Field name made lowercase.
    isoffset = models.CharField(db_column='IsOffset', max_length=1, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_out_voucherhead'


class WcsOutVoucherline(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    headerid = models.ForeignKey(WcsOutVoucherhead,db_column='HeaderID')  # Field name made lowercase.
    seqno = models.CharField(db_column='SeqNo', max_length=40, blank=True)  # Field name made lowercase.
    deorderno = models.CharField(db_column='DeOrderNo', max_length=40)  # Field name made lowercase.
    matreialvoucherno = models.CharField(db_column='MatreialVoucherNo', max_length=40, blank=True)  # Field name made lowercase.
    movetype = models.CharField(db_column='MoveType', max_length=40)  # Field name made lowercase.
    ordertotalqty = models.DecimalField(db_column='OrderTotalQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    deordertotalqty = models.DecimalField(db_column='DeOrderTotalQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    biztype = models.CharField(db_column='BizType', max_length=40)  # Field name made lowercase.
    deliverymodecode = models.CharField(db_column='DeliveryModeCode', max_length=40)  # Field name made lowercase.
    transportmodecode = models.CharField(db_column='TransportModeCode', max_length=40)  # Field name made lowercase.
    fromwarehouseid = models.IntegerField(db_column='FromWarehouseID')  # Field name made lowercase.
    towarehouseid = models.IntegerField(db_column='ToWarehouseID', blank=True, null=True)  # Field name made lowercase.
    soldtoid = models.IntegerField(db_column='SoldToID', blank=True, null=True)  # Field name made lowercase.
    soldtono = models.CharField(db_column='SoldToNo', max_length=40, blank=True)  # Field name made lowercase.
    soldtocontacts = models.CharField(db_column='SoldToContacts', max_length=60, blank=True)  # Field name made lowercase.
    slodtophoneno = models.CharField(db_column='SlodToPhoneNo', max_length=100, blank=True)  # Field name made lowercase.
    deliverytoid = models.IntegerField(db_column='DeliveryToID', blank=True, null=True)  # Field name made lowercase.
    receivercontacts = models.CharField(db_column='ReceiverContacts', max_length=60, blank=True)  # Field name made lowercase.
    receiverphoneno = models.CharField(db_column='ReceiverPhoneNo', max_length=100, blank=True)  # Field name made lowercase.
    toaddress = models.CharField(db_column='ToAddress', max_length=250, blank=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    uomcode = models.CharField(db_column='UomCode', max_length=40)  # Field name made lowercase.
    orderqty = models.DecimalField(db_column='OrderQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    deorderqty = models.DecimalField(db_column='DeOrderQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    finishedlqty = models.DecimalField(db_column='FinishedlQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    waitoutqty = models.DecimalField(db_column='WaitOutQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    actualoutqty = models.DecimalField(db_column='ActualOutQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    actualoutqty2 = models.DecimalField(db_column='ActualOutQty2', max_digits=18, decimal_places=6)  # Field name made lowercase.
    uom2code = models.CharField(db_column='Uom2Code', max_length=40)  # Field name made lowercase.
    netweight = models.DecimalField(db_column='NetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    stockaddressid = models.IntegerField(db_column='StockAddressID')  # Field name made lowercase.
    lotno = models.CharField(db_column='LotNo', max_length=200, blank=True)  # Field name made lowercase.
    lotnoactualoutqty = models.DecimalField(db_column='LotNoActualOutQty', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    lotnoplanqty = models.DecimalField(db_column='LotNoPlanQty', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    specialstockmark = models.CharField(db_column='SpecialStockMark', max_length=40, blank=True)  # Field name made lowercase.
    customerno = models.CharField(db_column='CustomerNo', max_length=40, blank=True)  # Field name made lowercase.
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
    orderstatus = models.CharField(db_column='OrderStatus', max_length=40, blank=True)  # Field name made lowercase.
    postingstatus = models.CharField(db_column='PostingStatus', max_length=40, blank=True)  # Field name made lowercase.
    billingdate = models.DateField(db_column='BillingDate')  # Field name made lowercase.
    postinttime = models.DateTimeField(db_column='PostintTime', blank=True, null=True)  # Field name made lowercase.
    isoffset = models.CharField(db_column='IsOffset', max_length=1, blank=True)  # Field name made lowercase.
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1)  # Field name made lowercase.
    vouchelineid = models.IntegerField(db_column='VoucheLineID', blank=True, null=True)  # Field name made lowercase.
    vouchelinelastwrittentime = models.DateTimeField(db_column='VoucheLineLastWrittenTime', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_out_voucherline'


class WcsOutVouchervehicle(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineID')  # Field name made lowercase.
    smallvoucherno = models.CharField(db_column='SmallVoucherNo', max_length=40)  # Field name made lowercase.
    tructid = models.IntegerField(db_column='TructID')  # Field name made lowercase.
    vehicleno = models.CharField(db_column='VehicleNo', max_length=40)  # Field name made lowercase.
    drivername = models.CharField(db_column='DriverName', max_length=40)  # Field name made lowercase.
    driveridno = models.CharField(db_column='DriverIDNo', max_length=40)  # Field name made lowercase.
    driverphoneno = models.CharField(db_column='DriverPhoneNo', max_length=100, blank=True)  # Field name made lowercase.
    deadweight = models.DecimalField(db_column='DeadWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loaduomid = models.IntegerField(db_column='LoadUomID')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=18, decimal_places=6)  # Field name made lowercase.
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
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_out_vouchervehicle'


class WcsSAjusthead(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    voucherno = models.CharField(db_column='VoucherNo', max_length=40)  # Field name made lowercase.
    biztype = models.CharField(db_column='BizType', max_length=40)  # Field name made lowercase.
    movetype = models.CharField(db_column='MoveType', max_length=40)  # Field name made lowercase.
    docdate = models.DateField(db_column='DocDate', blank=True, null=True)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    netweight = models.DecimalField(db_column='NetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1)  # Field name made lowercase.
    postingstatus = models.CharField(db_column='PostingStatus', max_length=40, blank=True)  # Field name made lowercase.
    voucherstatus = models.CharField(db_column='VoucherStatus', max_length=40, blank=True)  # Field name made lowercase.
    isoffset = models.CharField(db_column='IsOffset', max_length=1, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_s_ajusthead'


class WcsSAjustline(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    headerid = models.IntegerField(db_column='HeaderID')  # Field name made lowercase.
    matreialvoucherno = models.CharField(db_column='MatreialVoucherNo', max_length=40, blank=True)  # Field name made lowercase.
    seqno = models.CharField(db_column='SeqNo', max_length=40, blank=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    movetype = models.CharField(db_column='MoveType', max_length=40)  # Field name made lowercase.
    uomcode = models.CharField(db_column='UomCode', max_length=40)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    netweight = models.DecimalField(db_column='NetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lotno = models.CharField(db_column='LotNo', max_length=200)  # Field name made lowercase.
    lotno1 = models.CharField(db_column='LotNo1', max_length=200)  # Field name made lowercase.
    lotno2 = models.CharField(db_column='LotNo2', max_length=200)  # Field name made lowercase.
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
    orderstatus = models.CharField(db_column='OrderStatus', max_length=40, blank=True)  # Field name made lowercase.
    stockaddressid = models.IntegerField(db_column='StockAddressID')  # Field name made lowercase.
    postingstatus = models.CharField(db_column='PostingStatus', max_length=40, blank=True)  # Field name made lowercase.
    postinttime = models.DateTimeField(db_column='PostintTime', blank=True, null=True)  # Field name made lowercase.
    loanmark = models.CharField(db_column='LoanMark', max_length=1)  # Field name made lowercase.
    isoffset = models.CharField(db_column='IsOffset', max_length=1, blank=True)  # Field name made lowercase.
    specialstockmark = models.CharField(db_column='SpecialStockMark', max_length=40, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_s_ajustline'


class WcsSBiztypeChangetype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    vouchertype = models.CharField(db_column='VoucherType', max_length=40)  # Field name made lowercase.
    biztypecode = models.CharField(db_column='BizTypeCode', max_length=40)  # Field name made lowercase.
    biztypename = models.CharField(db_column='BizTypeName', max_length=200, blank=True)  # Field name made lowercase.
    shelvestype = models.CharField(db_column='ShelvesType', max_length=40, blank=True)  # Field name made lowercase.
    lockedtype = models.CharField(db_column='LockedType', max_length=40, blank=True)  # Field name made lowercase.
    periodtype = models.CharField(db_column='PeriodType', max_length=40, blank=True)  # Field name made lowercase.
    holdtype = models.CharField(db_column='HoldType', max_length=40, blank=True)  # Field name made lowercase.
    inwaytype = models.CharField(db_column='InWayType', max_length=40, blank=True)  # Field name made lowercase.
    qctype = models.CharField(db_column='QCType', max_length=40, blank=True)  # Field name made lowercase.
    frozentype = models.CharField(db_column='FrozenType', max_length=40, blank=True)  # Field name made lowercase.
    consigntype = models.CharField(db_column='ConsignType', max_length=40, blank=True)  # Field name made lowercase.
    othernatype = models.CharField(db_column='OtherNAType', max_length=40, blank=True)  # Field name made lowercase.
    movetypecode = models.CharField(db_column='MoveTypeCode', max_length=40)  # Field name made lowercase.
    movetypename = models.CharField(db_column='MoveTypeName', max_length=200, blank=True)  # Field name made lowercase.
    pstyp = models.CharField(db_column='Pstyp', max_length=40, blank=True)  # Field name made lowercase.
    moveflag = models.CharField(db_column='MoveFlag', max_length=40, blank=True)  # Field name made lowercase.
    purchasetype = models.CharField(db_column='PurchaseType', max_length=40, blank=True)  # Field name made lowercase.
    shkzg = models.CharField(db_column='Shkzg', max_length=40)  # Field name made lowercase.
    assessmenttype = models.CharField(db_column='AssessmentType', max_length=40, blank=True)  # Field name made lowercase.
    available = models.CharField(db_column='Available', max_length=1)  # Field name made lowercase.
    itemflag = models.CharField(db_column='ItemFlag', max_length=1)  # Field name made lowercase.
    reverseflag = models.CharField(db_column='ReverseFlag', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60, blank=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_s_biztype_changetype'


class WcsSHoldamount(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    materielid = models.IntegerField(db_column='MaterielID')  # Field name made lowercase.
    stockaddressid = models.IntegerField(db_column='StockAddressID')  # Field name made lowercase.
    holdamount = models.DecimalField(db_column='HoldAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
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
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_s_holdamount'


class WcsSHoldamountAdjusthead(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    stockaddressid = models.IntegerField(db_column='StockAddressID')  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID')  # Field name made lowercase.
    factorycode = models.CharField(db_column='FactoryCode', max_length=40)  # Field name made lowercase.
    voucherno = models.CharField(db_column='VoucherNo', max_length=40)  # Field name made lowercase.
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1)  # Field name made lowercase.
    adjustreason = models.CharField(db_column='AdjustReason', max_length=400, blank=True)  # Field name made lowercase.
    vouchermonth = models.CharField(db_column='VoucherMonth', max_length=6)  # Field name made lowercase.
    monthadjustorder = models.IntegerField(db_column='MonthAdjustOrder')  # Field name made lowercase.
    materiels = models.IntegerField(db_column='Materiels', blank=True, null=True)  # Field name made lowercase.
    voucherstatus = models.CharField(db_column='VoucherStatus', max_length=40, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    commiteduser = models.CharField(db_column='CommitedUser', max_length=60)  # Field name made lowercase.
    commitedtime = models.DateTimeField(db_column='CommitedTime')  # Field name made lowercase.
    approvaluser = models.CharField(db_column='ApprovalUser', max_length=60)  # Field name made lowercase.
    approvaltime = models.DateTimeField(db_column='ApprovalTime')  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_s_holdamount_adjusthead'


class WcsSHoldamountAdjustitem(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    headerid = models.IntegerField(db_column='HeaderID')  # Field name made lowercase.
    factorycode = models.CharField(db_column='FactoryCode', max_length=40)  # Field name made lowercase.
    materielid = models.IntegerField(db_column='MaterielID', blank=True, null=True)  # Field name made lowercase.
    seqno = models.CharField(db_column='SeqNo', max_length=40, blank=True)  # Field name made lowercase.
    oldholdamount = models.DecimalField(db_column='OldHoldAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    newholdamount = models.DecimalField(db_column='NewHoldAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    takeeffecttime = models.DateTimeField(db_column='TakeEffectTime', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_s_holdamount_adjustitem'


class WcsSLedger(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID')  # Field name made lowercase.
    factorycode = models.CharField(db_column='FactoryCode', max_length=40)  # Field name made lowercase.
    materielid = models.IntegerField(db_column='MaterielID')  # Field name made lowercase.
    materielgroupcode = models.CharField(db_column='MaterielGroupCode', max_length=40)  # Field name made lowercase.
    stockaddressid = models.IntegerField(db_column='StockAddressID')  # Field name made lowercase.
    uomcode = models.CharField(db_column='UomCode', max_length=40)  # Field name made lowercase.
    shelvesamount = models.DecimalField(db_column='ShelvesAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    sagrossweight = models.DecimalField(db_column='SAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    sanetweight = models.DecimalField(db_column='SANetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lockedamount = models.DecimalField(db_column='LockedAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lagrossweight = models.DecimalField(db_column='LAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lanetweight = models.DecimalField(db_column='LANetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    periodamount = models.DecimalField(db_column='PeriodAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    pagrossweight = models.DecimalField(db_column='PAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    panetweight = models.DecimalField(db_column='PANetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    holdamount = models.DecimalField(db_column='HoldAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    hagrossweight = models.DecimalField(db_column='HAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    hanetweight = models.DecimalField(db_column='HANetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    inwayamount = models.DecimalField(db_column='InWayAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    wagrossweight = models.DecimalField(db_column='WAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    wanetweight = models.DecimalField(db_column='WANetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    qcamount = models.DecimalField(db_column='QCAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    qcagrossweight = models.DecimalField(db_column='QCAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    qcnetweight = models.DecimalField(db_column='QCNetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    frozenamount = models.DecimalField(db_column='FrozenAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    fagrossweight = models.DecimalField(db_column='FAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    fnetweight = models.DecimalField(db_column='FNetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    consignamount = models.DecimalField(db_column='ConsignAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    cagrossweight = models.DecimalField(db_column='CAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    cnetweight = models.DecimalField(db_column='CNetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    othernaamount = models.DecimalField(db_column='OtherNAAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    onaagrossweight = models.DecimalField(db_column='ONAAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    onaanetweight = models.DecimalField(db_column='ONAANetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lotnotimes = models.IntegerField(db_column='LotNoTimes', blank=True, null=True)  # Field name made lowercase.
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
    isdeleted = models.CharField(db_column='IsDeleted', max_length=1)  # Field name made lowercase.
    deductionmonth6 = models.DecimalField(db_column='DeductionMonth6', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_s_ledger'


class WcsSLedgerChangelog(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineID')  # Field name made lowercase.
    changetime = models.DateTimeField(db_column='ChangeTime')  # Field name made lowercase.
    changetype = models.CharField(db_column='ChangeType', max_length=40)  # Field name made lowercase.
    driveorderno = models.CharField(db_column='DriveOrderNo', max_length=40)  # Field name made lowercase.
    orderlineid = models.CharField(db_column='OrderLineID', max_length=40)  # Field name made lowercase.
    oldamount = models.DecimalField(db_column='OldAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    newamount = models.DecimalField(db_column='NewAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_s_ledger_changelog'


class WcsSLedgerdetaill(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    # headerid = models.IntegerField(db_column='HeaderID')  # Field name made lowercase.
    headerid = models.ForeignKey(WcsSLedger,db_column='HeaderID') # Field name made lowercase.
    factorycode = models.CharField(db_column='FactoryCode', max_length=40)  # Field name made lowercase.
    intime = models.DateTimeField(db_column='InTime')  # Field name made lowercase.
    expirationdate = models.DateField(db_column='ExpirationDate', blank=True, null=True)  # Field name made lowercase.
    lotno = models.CharField(db_column='LotNo', max_length=200)  # Field name made lowercase.
    uomcode = models.CharField(db_column='UomCode', max_length=40)  # Field name made lowercase.
    shelvesamount = models.DecimalField(db_column='ShelvesAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    sagrossweight = models.DecimalField(db_column='SAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    sanetweight = models.DecimalField(db_column='SANetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lockedamount = models.DecimalField(db_column='LockedAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lagrossweight = models.DecimalField(db_column='LAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lanetweight = models.DecimalField(db_column='LANetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    periodamount = models.DecimalField(db_column='PeriodAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    pagrossweight = models.DecimalField(db_column='PAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    panetweight = models.DecimalField(db_column='PANetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    holdamount = models.DecimalField(db_column='HoldAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    hagrossweight = models.DecimalField(db_column='HAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    hanetweight = models.DecimalField(db_column='HANetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    inwayamount = models.DecimalField(db_column='InWayAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    wagrossweight = models.DecimalField(db_column='WAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    wanetweight = models.DecimalField(db_column='WANetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    qcamount = models.DecimalField(db_column='QCAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    qcagrossweight = models.DecimalField(db_column='QCAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    qcnetweight = models.DecimalField(db_column='QCNetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    frozenamount = models.DecimalField(db_column='FrozenAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    fagrossweight = models.DecimalField(db_column='FAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    fnetweight = models.DecimalField(db_column='FNetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    consignamount = models.DecimalField(db_column='ConsignAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    cagrossweight = models.DecimalField(db_column='CAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    cnetweight = models.DecimalField(db_column='CNetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    othernaamount = models.DecimalField(db_column='OtherNAAmount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    onaagrossweight = models.DecimalField(db_column='ONAAGrossWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    onaanetweight = models.DecimalField(db_column='ONAANetWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
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
    postingstatus = models.CharField(db_column='PostingStatus', max_length=40, blank=True)  # Field name made lowercase.
    postinttime = models.DateTimeField(db_column='PostintTime', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_s_ledgerdetaill'


class WcsTVoucherdatatrack(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    batchcode = models.CharField(db_column='BatchCode', max_length=100, blank=True)  # Field name made lowercase.
    plsh = models.CharField(db_column='PLSH', max_length=40, blank=True)  # Field name made lowercase.
    erp_wlpzh = models.CharField(db_column='ERP_WLPZH', max_length=20, blank=True)  # Field name made lowercase.
    erp_pzrq = models.CharField(db_column='ERP_PZRQ', max_length=8, blank=True)  # Field name made lowercase.
    erp_gzrq = models.CharField(db_column='ERP_GZRQ', max_length=8, blank=True)  # Field name made lowercase.
    erp_ydlx = models.CharField(db_column='ERP_YDLX', max_length=10, blank=True)  # Field name made lowercase.
    erp_gcdm = models.CharField(db_column='ERP_GCDM', max_length=10, blank=True)  # Field name made lowercase.
    erp_kwdm = models.CharField(db_column='ERP_KWDM', max_length=10, blank=True)  # Field name made lowercase.
    erp_wldm = models.CharField(db_column='ERP_WLDM', max_length=20, blank=True)  # Field name made lowercase.
    erp_pch = models.CharField(db_column='ERP_PCH', max_length=10, blank=True)  # Field name made lowercase.
    erp_pglx = models.CharField(db_column='ERP_PGLX', max_length=10, blank=True)  # Field name made lowercase.
    erp_jdbj = models.CharField(db_column='ERP_JDBJ', max_length=1, blank=True)  # Field name made lowercase.
    erp_jldmdm = models.CharField(db_column='ERP_JLDMDM', max_length=20, blank=True)  # Field name made lowercase.
    erp_sl = models.DecimalField(db_column='ERP_SL', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    wlpz_bm = models.CharField(db_column='WLPZ_BM', max_length=40, blank=True)  # Field name made lowercase.
    wlpz_hxmid = models.IntegerField(db_column='WLPZ_HXMID', blank=True, null=True)  # Field name made lowercase.
    wlpz_hxmms = models.CharField(db_column='WLPZ_HXMMS', max_length=4096, blank=True)  # Field name made lowercase.
    tztt_id = models.IntegerField(db_column='TZTT_ID', blank=True, null=True)  # Field name made lowercase.
    tztt_ms = models.CharField(db_column='TZTT_MS', max_length=4096, blank=True)  # Field name made lowercase.
    tztz_cz = models.CharField(db_column='TZTZ_CZ', max_length=10, blank=True)  # Field name made lowercase.
    tztt_ysl = models.DecimalField(db_column='TZTT_YSL', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    tztt_xsl = models.DecimalField(db_column='TZTT_XSL', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    tzhxm_id = models.IntegerField(db_column='TZHXM_ID', blank=True, null=True)  # Field name made lowercase.
    tzhxm_ms = models.CharField(db_column='TZHXM_MS', max_length=4096, blank=True)  # Field name made lowercase.
    tzhxm_cz = models.CharField(db_column='TZHXM_CZ', max_length=10, blank=True)  # Field name made lowercase.
    tzhxm_ysl = models.DecimalField(db_column='TZHXM_YSL', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    tzhxm_xsl = models.DecimalField(db_column='TZHXM_XSL', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    bdrz_id = models.IntegerField(db_column='BDRZ_ID', blank=True, null=True)  # Field name made lowercase.
    bdrz_tzid = models.IntegerField(db_column='BDRZ_TZID', blank=True, null=True)  # Field name made lowercase.
    bdrz_bdlx = models.CharField(db_column='BDRZ_BDLX', max_length=40, blank=True)  # Field name made lowercase.
    bdrz_qddjh = models.CharField(db_column='BDRZ_QDDJH', max_length=4096, blank=True)  # Field name made lowercase.
    ddrz_ysl = models.DecimalField(db_column='DDRZ_YSL', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    bdrz_xsl = models.DecimalField(db_column='BDRZ_XSL', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    vouchertype = models.CharField(db_column='VoucherType', max_length=40, blank=True)  # Field name made lowercase.
    biztypecode = models.CharField(db_column='BizTypeCode', max_length=40, blank=True)  # Field name made lowercase.
    movetypecode = models.CharField(db_column='MoveTypeCode', max_length=40, blank=True)  # Field name made lowercase.
    pstyp = models.CharField(db_column='Pstyp', max_length=40, blank=True)  # Field name made lowercase.
    moveflag = models.CharField(db_column='MoveFlag', max_length=40, blank=True)  # Field name made lowercase.
    purchasetype = models.CharField(db_column='PurchaseType', max_length=40, blank=True)  # Field name made lowercase.
    shkzg = models.CharField(db_column='Shkzg', max_length=40, blank=True)  # Field name made lowercase.
    assessmenttype = models.CharField(db_column='AssessmentType', max_length=40, blank=True)  # Field name made lowercase.
    itemflag = models.CharField(db_column='ItemFlag', max_length=40, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wcs_t_voucherdatatrack'

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


class TEcEvalattach(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    headerid = models.ForeignKey('TEcShipmenteval', db_column='HeaderID')  # Field name made lowercase.
    tenantid = models.BigIntegerField(db_column='TenantID')  # Field name made lowercase.
    leid = models.BigIntegerField(db_column='LeID', blank=True, null=True)  # Field name made lowercase.
    identificationtype = models.CharField(db_column='IdentificationType', max_length=40, blank=True)  # Field name made lowercase.
    identificationno = models.CharField(db_column='IdentificationNo', max_length=50, blank=True)  # Field name made lowercase.
    fileformat = models.CharField(db_column='FileFormat', max_length=40, blank=True)  # Field name made lowercase.
    fileurl = models.CharField(db_column='FileUrl', max_length=200, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ec_evalattach'


class TEcShipmenteval(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.BigIntegerField(db_column='TenantID', blank=True, null=True)  # Field name made lowercase.
    leid = models.BigIntegerField(db_column='LeID', blank=True, null=True)  # Field name made lowercase.
    shipmentcode = models.CharField(db_column='ShipmentCode', max_length=40, blank=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=40)  # Field name made lowercase.
    statedesc = models.CharField(db_column='StateDesc', max_length=100, blank=True)  # Field name made lowercase.
    satisfactionstate = models.CharField(db_column='SatisfactionState', max_length=40, blank=True)  # Field name made lowercase.
    satisfactionstatedesc = models.CharField(db_column='SatisfactionStateDesc', max_length=50, blank=True)  # Field name made lowercase.
    complaintsitem = models.CharField(db_column='ComplaintsItem', max_length=40, blank=True)  # Field name made lowercase.
    complaintscontent = models.CharField(db_column='ComplaintsContent', max_length=200, blank=True)  # Field name made lowercase.
    complaintsitemdesc = models.CharField(db_column='ComplaintsItemDesc', max_length=40, blank=True)  # Field name made lowercase.
    receiptdate = models.DateTimeField(db_column='ReceiptDate', blank=True, null=True)  # Field name made lowercase.
    evaluatedate = models.DateTimeField(db_column='EvaluateDate', blank=True, null=True)  # Field name made lowercase.
    receiptuser = models.CharField(db_column='ReceiptUser', max_length=80, blank=True)  # Field name made lowercase.
    receiptunitcode = models.CharField(db_column='ReceiptUnitCode', max_length=80, blank=True)  # Field name made lowercase.
    receiptunitname = models.CharField(db_column='ReceiptUnitName', max_length=80, blank=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ec_shipmenteval'

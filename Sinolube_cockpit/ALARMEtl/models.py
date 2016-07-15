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


class TAcAlarm(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    alarmno = models.CharField(db_column='AlarmNo', max_length=50)  # Field name made lowercase.
    alarmname = models.CharField(db_column='AlarmName', max_length=50, blank=True)  # Field name made lowercase.
    alarmtype = models.IntegerField(db_column='AlarmType', blank=True, null=True)  # Field name made lowercase.
    ararmtarget = models.CharField(db_column='ArarmTarget', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ac_alarm'


class TAcAlarmDefine(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tagno = models.CharField(db_column='TagNo', max_length=50)  # Field name made lowercase.
    tagname = models.CharField(db_column='TagName', max_length=50, blank=True)  # Field name made lowercase.
    alarmtype = models.CharField(db_column='AlarmType', max_length=50, blank=True)  # Field name made lowercase.
    alarmclass = models.CharField(db_column='AlarmClass', max_length=50, blank=True)  # Field name made lowercase.
    alarmrelationno = models.CharField(db_column='AlarmRelationNo', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ac_alarm_define'


class TAcAlarmOvday(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderno = models.CharField(db_column='OrderNo', max_length=50, blank=True)  # Field name made lowercase.
    ordercreatetime = models.DateTimeField(db_column='OrderCreateTime', blank=True, null=True)  # Field name made lowercase.
    orderweight = models.DecimalField(db_column='OrderWeight', max_digits=22, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    ovdaytype = models.IntegerField(db_column='OvdayType', blank=True, null=True)  # Field name made lowercase.
    ovitemno = models.CharField(db_column='OvItemNo', max_length=50, blank=True)  # Field name made lowercase.
    ovitemweight = models.DecimalField(db_column='OvItemWeight', max_digits=22, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    tstarttime = models.DateTimeField(db_column='TStartTime', blank=True, null=True)  # Field name made lowercase.
    tendtime = models.DateTimeField(db_column='TEndTIme', blank=True, null=True)  # Field name made lowercase.
    tday = models.IntegerField(db_column='TDay', blank=True, null=True)  # Field name made lowercase.
    alarm_stepno = models.CharField(max_length=50, blank=True)
    parentitemno = models.CharField(db_column='parentItemNo', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ac_alarm_ovday'


class TAcAlarmRecord(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recordno = models.CharField(db_column='RecordNo', max_length=50, blank=True)  # Field name made lowercase.
    alarmdate = models.DateTimeField(db_column='AlarmDate', blank=True, null=True)  # Field name made lowercase.
    alarmstatus = models.CharField(db_column='AlarmStatus', max_length=50, blank=True)  # Field name made lowercase.
    tagno = models.CharField(db_column='TagNo', max_length=50, blank=True)  # Field name made lowercase.
    tday = models.IntegerField(db_column='TDay', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ac_alarm_record'


class TAcAlarmStatus(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderno = models.CharField(db_column='OrderNo', max_length=50, blank=True)  # Field name made lowercase.
    alarm_stepno = models.CharField(max_length=50, blank=True)
    percentstatus = models.IntegerField(db_column='PercentStatus', blank=True, null=True)  # Field name made lowercase.
    sortno = models.IntegerField(blank=True, null=True)
    overdate = models.DateTimeField(db_column='OverDate', blank=True, null=True)  # Field name made lowercase.
    tagno = models.CharField(db_column='TagNo', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ac_alarm_status'


class TAcAlarmSteps(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    stepno = models.CharField(max_length=50, blank=True)
    stepname = models.CharField(max_length=50, blank=True)
    sortno = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_ac_alarm_steps'


class TAcCondition(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    conditionno = models.CharField(db_column='ConditionNo', max_length=50, blank=True)  # Field name made lowercase.
    conditionname = models.CharField(db_column='ConditionName', max_length=50, blank=True)  # Field name made lowercase.
    conditionexpression = models.CharField(db_column='ConditionExpression', max_length=500, blank=True)  # Field name made lowercase.
    tagno = models.CharField(db_column='TagNo', max_length=50, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 't_ac_condition'


class TAcOrderSeverity(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    sevno = models.CharField(db_column='SevNo', max_length=50)  # Field name made lowercase.
    sevtype = models.IntegerField(db_column='SevType', blank=True, null=True)  # Field name made lowercase.
    sevstepno = models.CharField(db_column='SevStepNo', max_length=50, blank=True)  # Field name made lowercase.
    sevvolume = models.IntegerField(db_column='SevVolume', blank=True, null=True)  # Field name made lowercase.
    sevremark = models.CharField(db_column='SevRemark', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ac_order_severity'


class TAcOrderState(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderno = models.CharField(db_column='OrderNo', max_length=50)  # Field name made lowercase.
    orderstate = models.IntegerField(db_column='OrderState')  # Field name made lowercase.
    uptime = models.DateTimeField(db_column='Uptime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ac_order_state'


class TAcPriority(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    priorityno = models.CharField(db_column='PriorityNo', max_length=50, blank=True)  # Field name made lowercase.
    priorityname = models.CharField(db_column='PriorityName', max_length=50, blank=True)  # Field name made lowercase.
    tagno = models.CharField(db_column='TagNo', max_length=50, blank=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ac_priority'

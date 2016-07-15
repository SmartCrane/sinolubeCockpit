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


class LrcCompany(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companycode = models.CharField(db_column='CompanyCode', unique=True, max_length=40)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=255)  # Field name made lowercase.
    companysname = models.CharField(db_column='CompanySName', max_length=255)  # Field name made lowercase.
    erpcode = models.CharField(db_column='ErpCode', max_length=40, blank=True)  # Field name made lowercase.
    companyename = models.CharField(db_column='CompanyEName', max_length=500, blank=True)  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=255, blank=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True)  # Field name made lowercase.
    contract = models.CharField(db_column='Contract', max_length=80, blank=True)  # Field name made lowercase.
    contracttel = models.CharField(db_column='ContractTel', max_length=80, blank=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=80, blank=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=80, blank=True)  # Field name made lowercase.
    webaddress = models.CharField(db_column='WebAddress', max_length=80, blank=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=80, blank=True)  # Field name made lowercase.
    invoicetitle = models.CharField(db_column='InvoiceTitle', max_length=80, blank=True)  # Field name made lowercase.
    propertyid = models.CharField(db_column='PropertyId', max_length=64, blank=True)  # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityId', blank=True, null=True)  # Field name made lowercase.
    companytype = models.CharField(db_column='CompanyType', max_length=1, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=500, blank=True)  # Field name made lowercase.
    bizlicenseregno = models.CharField(db_column='BizLicenseRegNo', max_length=80, blank=True)  # Field name made lowercase.
    blname = models.CharField(db_column='BlName', max_length=200, blank=True)  # Field name made lowercase.
    biaddress = models.CharField(db_column='BIAddress', max_length=200, blank=True)  # Field name made lowercase.
    legalrepresentative = models.CharField(db_column='LegalRepresentative', max_length=80, blank=True)  # Field name made lowercase.
    corporatetype = models.CharField(db_column='CorporateType', max_length=20, blank=True)  # Field name made lowercase.
    registeramount = models.DecimalField(db_column='RegisterAmount', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    paidincapital = models.DecimalField(db_column='PaidInCapital', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    establishdate = models.DateTimeField(db_column='EstablishDate', blank=True, null=True)  # Field name made lowercase.
    businessscope = models.CharField(db_column='BusinessScope', max_length=200, blank=True)  # Field name made lowercase.
    blstartdate = models.DateTimeField(db_column='BlStartDate', blank=True, null=True)  # Field name made lowercase.
    blenddate = models.DateTimeField(db_column='BlEndDate', blank=True, null=True)  # Field name made lowercase.
    blissuedby = models.CharField(db_column='BlIssuedBy', max_length=200, blank=True)  # Field name made lowercase.
    blissueddate = models.DateTimeField(db_column='BlIssuedDate', blank=True, null=True)  # Field name made lowercase.
    taxregno = models.CharField(db_column='TaxRegNo', max_length=200, blank=True)  # Field name made lowercase.
    taxpayername = models.CharField(db_column='TaxpayerName', max_length=200, blank=True)  # Field name made lowercase.
    leadingofficial = models.CharField(db_column='LeadingOfficial', max_length=200, blank=True)  # Field name made lowercase.
    traddress = models.CharField(db_column='TrAddress', max_length=200, blank=True)  # Field name made lowercase.
    trtype = models.CharField(db_column='TrType', max_length=200, blank=True)  # Field name made lowercase.
    trscope = models.CharField(db_column='TrScope', max_length=500, blank=True)  # Field name made lowercase.
    approvalauthority = models.CharField(db_column='ApprovalAuthority', max_length=200, blank=True)  # Field name made lowercase.
    withholdingagent = models.CharField(db_column='WithholdingAgent', max_length=200, blank=True)  # Field name made lowercase.
    taxauthorities = models.CharField(db_column='TaxAuthorities', max_length=200, blank=True)  # Field name made lowercase.
    occcode = models.CharField(db_column='OccCode', max_length=200, blank=True)  # Field name made lowercase.
    occname = models.CharField(db_column='OccName', max_length=200, blank=True)  # Field name made lowercase.
    occtype = models.CharField(db_column='OccType', max_length=200, blank=True)  # Field name made lowercase.
    occaddress = models.CharField(db_column='OccAddress', max_length=500, blank=True)  # Field name made lowercase.
    occstartdate = models.DateTimeField(db_column='OccStartDate', blank=True, null=True)  # Field name made lowercase.
    occenddate = models.DateTimeField(db_column='OccEndDate', blank=True, null=True)  # Field name made lowercase.
    occissuedby = models.CharField(db_column='OccIssuedBy', max_length=200, blank=True)  # Field name made lowercase.
    occregno = models.CharField(db_column='OccRegNo', max_length=200, blank=True)  # Field name made lowercase.
    employeecount = models.IntegerField(db_column='EmployeeCount', blank=True, null=True)  # Field name made lowercase.
    seniorcount = models.IntegerField(db_column='SeniorCount', blank=True, null=True)  # Field name made lowercase.
    middlecount = models.IntegerField(db_column='MiddleCount', blank=True, null=True)  # Field name made lowercase.
    juniorcount = models.IntegerField(db_column='JuniorCount', blank=True, null=True)  # Field name made lowercase.
    netassets = models.DecimalField(db_column='NetAssets', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    originalfixedassets = models.DecimalField(db_column='OriginalFixedAssets', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    netfixedassets = models.DecimalField(db_column='NetFixedAssets', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    debtamount = models.DecimalField(db_column='DebtAmount', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    debtratio = models.DecimalField(db_column='DebtRatio', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    salesamount = models.DecimalField(db_column='SalesAmount', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    totalprofit = models.DecimalField(db_column='TotalProfit', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    netprofit = models.DecimalField(db_column='NetProfit', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    currencyunit = models.CharField(db_column='CurrencyUnit', max_length=100, blank=True)  # Field name made lowercase.
    bankdeposit = models.CharField(db_column='BankDeposit', max_length=100, blank=True)  # Field name made lowercase.
    depositname = models.CharField(db_column='DepositName', max_length=100, blank=True)  # Field name made lowercase.
    bankaccount = models.CharField(db_column='BankAccount', max_length=100, blank=True)  # Field name made lowercase.
    bankcreditrating = models.CharField(db_column='BankCreditRating', max_length=100, blank=True)  # Field name made lowercase.
    corebtransport = models.CharField(db_column='CoreBTransport', max_length=100, blank=True)  # Field name made lowercase.
    corebwarehousing = models.CharField(db_column='CoreBWarehousing', max_length=100, blank=True)  # Field name made lowercase.
    corebother = models.CharField(db_column='CoreBOther', max_length=100, blank=True)  # Field name made lowercase.
    ownedtruckcount = models.IntegerField(db_column='OwnedTruckCount')  # Field name made lowercase.
    contracttruckcount = models.IntegerField(db_column='ContractTruckCount')  # Field name made lowercase.
    warehousingarea = models.IntegerField(db_column='WarehousingArea')  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.CharField(db_column='IsDelete', max_length=1)  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='ProvinceId', blank=True, null=True)  # Field name made lowercase.
    bankaccountname = models.CharField(db_column='BankAccountName', max_length=100, blank=True)  # Field name made lowercase.
    paymentmodeid = models.IntegerField(db_column='PaymentModeID', blank=True, null=True)  # Field name made lowercase.
    managedownerid = models.IntegerField(db_column='ManagedOwnerID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lrc_company'


class LrcCompanyCopy(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companycode = models.CharField(db_column='CompanyCode', unique=True, max_length=40)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=255)  # Field name made lowercase.
    companysname = models.CharField(db_column='CompanySName', max_length=255)  # Field name made lowercase.
    erpcode = models.CharField(db_column='ErpCode', max_length=40, blank=True)  # Field name made lowercase.
    companyename = models.CharField(db_column='CompanyEName', max_length=500, blank=True)  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=255, blank=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True)  # Field name made lowercase.
    contract = models.CharField(db_column='Contract', max_length=80, blank=True)  # Field name made lowercase.
    contracttel = models.CharField(db_column='ContractTel', max_length=80, blank=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=80, blank=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=80, blank=True)  # Field name made lowercase.
    webaddress = models.CharField(db_column='WebAddress', max_length=80, blank=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=80, blank=True)  # Field name made lowercase.
    invoicetitle = models.CharField(db_column='InvoiceTitle', max_length=80, blank=True)  # Field name made lowercase.
    propertyid = models.CharField(db_column='PropertyId', max_length=64, blank=True)  # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityId', blank=True, null=True)  # Field name made lowercase.
    companytype = models.CharField(db_column='CompanyType', max_length=1, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=500, blank=True)  # Field name made lowercase.
    bizlicenseregno = models.CharField(db_column='BizLicenseRegNo', max_length=80, blank=True)  # Field name made lowercase.
    blname = models.CharField(db_column='BlName', max_length=200, blank=True)  # Field name made lowercase.
    biaddress = models.CharField(db_column='BIAddress', max_length=200, blank=True)  # Field name made lowercase.
    legalrepresentative = models.CharField(db_column='LegalRepresentative', max_length=80, blank=True)  # Field name made lowercase.
    corporatetype = models.CharField(db_column='CorporateType', max_length=20, blank=True)  # Field name made lowercase.
    registeramount = models.DecimalField(db_column='RegisterAmount', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    paidincapital = models.DecimalField(db_column='PaidInCapital', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    establishdate = models.DateTimeField(db_column='EstablishDate', blank=True, null=True)  # Field name made lowercase.
    businessscope = models.CharField(db_column='BusinessScope', max_length=200, blank=True)  # Field name made lowercase.
    blstartdate = models.DateTimeField(db_column='BlStartDate', blank=True, null=True)  # Field name made lowercase.
    blenddate = models.DateTimeField(db_column='BlEndDate', blank=True, null=True)  # Field name made lowercase.
    blissuedby = models.CharField(db_column='BlIssuedBy', max_length=200, blank=True)  # Field name made lowercase.
    blissueddate = models.DateTimeField(db_column='BlIssuedDate', blank=True, null=True)  # Field name made lowercase.
    taxregno = models.CharField(db_column='TaxRegNo', max_length=200, blank=True)  # Field name made lowercase.
    taxpayername = models.CharField(db_column='TaxpayerName', max_length=200, blank=True)  # Field name made lowercase.
    leadingofficial = models.CharField(db_column='LeadingOfficial', max_length=200, blank=True)  # Field name made lowercase.
    traddress = models.CharField(db_column='TrAddress', max_length=200, blank=True)  # Field name made lowercase.
    trtype = models.CharField(db_column='TrType', max_length=200, blank=True)  # Field name made lowercase.
    trscope = models.CharField(db_column='TrScope', max_length=500, blank=True)  # Field name made lowercase.
    approvalauthority = models.CharField(db_column='ApprovalAuthority', max_length=200, blank=True)  # Field name made lowercase.
    withholdingagent = models.CharField(db_column='WithholdingAgent', max_length=200, blank=True)  # Field name made lowercase.
    taxauthorities = models.CharField(db_column='TaxAuthorities', max_length=200, blank=True)  # Field name made lowercase.
    occcode = models.CharField(db_column='OccCode', max_length=200, blank=True)  # Field name made lowercase.
    occname = models.CharField(db_column='OccName', max_length=200, blank=True)  # Field name made lowercase.
    occtype = models.CharField(db_column='OccType', max_length=200, blank=True)  # Field name made lowercase.
    occaddress = models.CharField(db_column='OccAddress', max_length=500, blank=True)  # Field name made lowercase.
    occstartdate = models.DateTimeField(db_column='OccStartDate', blank=True, null=True)  # Field name made lowercase.
    occenddate = models.DateTimeField(db_column='OccEndDate', blank=True, null=True)  # Field name made lowercase.
    occissuedby = models.CharField(db_column='OccIssuedBy', max_length=200, blank=True)  # Field name made lowercase.
    occregno = models.CharField(db_column='OccRegNo', max_length=200, blank=True)  # Field name made lowercase.
    employeecount = models.IntegerField(db_column='EmployeeCount', blank=True, null=True)  # Field name made lowercase.
    seniorcount = models.IntegerField(db_column='SeniorCount', blank=True, null=True)  # Field name made lowercase.
    middlecount = models.IntegerField(db_column='MiddleCount', blank=True, null=True)  # Field name made lowercase.
    juniorcount = models.IntegerField(db_column='JuniorCount', blank=True, null=True)  # Field name made lowercase.
    netassets = models.DecimalField(db_column='NetAssets', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    originalfixedassets = models.DecimalField(db_column='OriginalFixedAssets', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    netfixedassets = models.DecimalField(db_column='NetFixedAssets', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    debtamount = models.DecimalField(db_column='DebtAmount', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    debtratio = models.DecimalField(db_column='DebtRatio', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    salesamount = models.DecimalField(db_column='SalesAmount', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    totalprofit = models.DecimalField(db_column='TotalProfit', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    netprofit = models.DecimalField(db_column='NetProfit', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    currencyunit = models.CharField(db_column='CurrencyUnit', max_length=100, blank=True)  # Field name made lowercase.
    bankdeposit = models.CharField(db_column='BankDeposit', max_length=100, blank=True)  # Field name made lowercase.
    depositname = models.CharField(db_column='DepositName', max_length=100, blank=True)  # Field name made lowercase.
    bankaccount = models.CharField(db_column='BankAccount', max_length=100, blank=True)  # Field name made lowercase.
    bankcreditrating = models.CharField(db_column='BankCreditRating', max_length=100, blank=True)  # Field name made lowercase.
    corebtransport = models.CharField(db_column='CoreBTransport', max_length=100, blank=True)  # Field name made lowercase.
    corebwarehousing = models.CharField(db_column='CoreBWarehousing', max_length=100, blank=True)  # Field name made lowercase.
    corebother = models.CharField(db_column='CoreBOther', max_length=100, blank=True)  # Field name made lowercase.
    ownedtruckcount = models.IntegerField(db_column='OwnedTruckCount')  # Field name made lowercase.
    contracttruckcount = models.IntegerField(db_column='ContractTruckCount')  # Field name made lowercase.
    warehousingarea = models.IntegerField(db_column='WarehousingArea')  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.CharField(db_column='IsDelete', max_length=1)  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='ProvinceId', blank=True, null=True)  # Field name made lowercase.
    bankaccountname = models.CharField(db_column='BankAccountName', max_length=100, blank=True)  # Field name made lowercase.
    paymentmodeid = models.IntegerField(db_column='PaymentModeID', blank=True, null=True)  # Field name made lowercase.
    managedownerid = models.IntegerField(db_column='ManagedOwnerID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lrc_company_copy'


class LrcLicense(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    licensetype = models.CharField(db_column='LicenseType', max_length=10)  # Field name made lowercase.
    headerid = models.IntegerField(db_column='HeaderID')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    licensename = models.CharField(db_column='LicenseName', max_length=40, blank=True)  # Field name made lowercase.
    licenseno = models.CharField(db_column='LicenseNo', max_length=40, blank=True)  # Field name made lowercase.
    licensescope = models.CharField(db_column='LicenseScope', max_length=40, blank=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    approvalauthority = models.CharField(db_column='ApprovalAuthority', max_length=100, blank=True)  # Field name made lowercase.
    attachmentname = models.CharField(db_column='AttachmentName', max_length=100, blank=True)  # Field name made lowercase.
    attachmenturl = models.CharField(db_column='AttachmentUrl', max_length=200, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=400, blank=True)  # Field name made lowercase.
    isdelete = models.CharField(db_column='IsDelete', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lrc_license'


class LrcLogisticplatformuser(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    headerid = models.IntegerField(db_column='HeaderID')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.
    userlevel = models.CharField(db_column='UserLevel', max_length=60)  # Field name made lowercase.
    islogin = models.IntegerField(db_column='IsLogin', blank=True, null=True)  # Field name made lowercase.
    lastlogontime = models.DateTimeField(db_column='LastLogonTime', blank=True, null=True)  # Field name made lowercase.
    lastpwdmodifiedtime = models.DateTimeField(db_column='LastPwdModifiedTime', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=40)  # Field name made lowercase.
    islock = models.CharField(db_column='IsLock', max_length=1, blank=True)  # Field name made lowercase.
    lockreason = models.CharField(db_column='LockReason', max_length=200, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=200, blank=True)  # Field name made lowercase.
    extcode1 = models.CharField(db_column='ExtCode1', max_length=40, blank=True)  # Field name made lowercase.
    extcode2 = models.CharField(db_column='ExtCode2', max_length=40, blank=True)  # Field name made lowercase.
    extcode3 = models.CharField(db_column='ExtCode3', max_length=40, blank=True)  # Field name made lowercase.
    extcode4 = models.CharField(db_column='ExtCode4', max_length=40, blank=True)  # Field name made lowercase.
    extcode5 = models.CharField(db_column='ExtCode5', max_length=40, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lrc_logisticplatformuser'


class LrcLspcid(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('LrcLspuser', db_column='UserID')  # Field name made lowercase.
    clientid = models.CharField(db_column='clientId', unique=True, max_length=100)  # Field name made lowercase.
    lastlogontime = models.DateTimeField(db_column='LastLogonTime', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=40)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=200, blank=True)  # Field name made lowercase.
    extcode1 = models.CharField(db_column='ExtCode1', max_length=40, blank=True)  # Field name made lowercase.
    extcode2 = models.CharField(db_column='ExtCode2', max_length=40, blank=True)  # Field name made lowercase.
    extcode3 = models.CharField(db_column='ExtCode3', max_length=40, blank=True)  # Field name made lowercase.
    extcode4 = models.CharField(db_column='ExtCode4', max_length=40, blank=True)  # Field name made lowercase.
    extcode5 = models.CharField(db_column='ExtCode5', max_length=40, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lrc_lspcid'


class LrcLspuser(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    headerid = models.ForeignKey(LrcCompany, db_column='HeaderID')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', unique=True, max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.
    userlevel = models.CharField(db_column='UserLevel', max_length=60)  # Field name made lowercase.
    islogin = models.IntegerField(db_column='IsLogin', blank=True, null=True)  # Field name made lowercase.
    lastlogontime = models.DateTimeField(db_column='LastLogonTime', blank=True, null=True)  # Field name made lowercase.
    lastpwdmodifiedtime = models.DateTimeField(db_column='LastPwdModifiedTime', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=40)  # Field name made lowercase.
    islock = models.CharField(db_column='IsLock', max_length=1, blank=True)  # Field name made lowercase.
    lockreason = models.CharField(db_column='LockReason', max_length=200, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=200, blank=True)  # Field name made lowercase.
    extcode1 = models.CharField(db_column='ExtCode1', max_length=40, blank=True)  # Field name made lowercase.
    extcode2 = models.CharField(db_column='ExtCode2', max_length=40, blank=True)  # Field name made lowercase.
    extcode3 = models.CharField(db_column='ExtCode3', max_length=40, blank=True)  # Field name made lowercase.
    extcode4 = models.CharField(db_column='ExtCode4', max_length=40, blank=True)  # Field name made lowercase.
    extcode5 = models.CharField(db_column='ExtCode5', max_length=40, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lrc_lspuser'


class LrcServiceprovider(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyID')  # Field name made lowercase.
    spattrib = models.CharField(db_column='SpAttrib', max_length=50, blank=True)  # Field name made lowercase.
    sptype = models.CharField(db_column='SpType', max_length=16, blank=True)  # Field name made lowercase.
    splevel = models.CharField(db_column='SpLevel', max_length=16, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=500, blank=True)  # Field name made lowercase.
    sortorder = models.CharField(db_column='SortOrder', max_length=10, blank=True)  # Field name made lowercase.
    genmethod = models.CharField(db_column='GenMethod', max_length=1, blank=True)  # Field name made lowercase.
    genstatus = models.CharField(db_column='GenStatus', max_length=16, blank=True)  # Field name made lowercase.
    approvestatus = models.CharField(db_column='ApproveStatus', max_length=5, blank=True)  # Field name made lowercase.
    firstbizdate = models.DateTimeField(db_column='FirstBizDate', blank=True, null=True)  # Field name made lowercase.
    lastbizdate = models.DateTimeField(db_column='LastBizDate', blank=True, null=True)  # Field name made lowercase.
    iscarrier = models.CharField(db_column='IsCarrier', max_length=1)  # Field name made lowercase.
    iswhprovider = models.CharField(db_column='IsWhProvider', max_length=1)  # Field name made lowercase.
    isotherprovider = models.CharField(db_column='IsOtherProvider', max_length=1)  # Field name made lowercase.
    isvirtual = models.CharField(db_column='IsVirtual', max_length=1)  # Field name made lowercase.
    gpsenabled = models.CharField(db_column='GpsEnabled', max_length=1)  # Field name made lowercase.
    isinsurer = models.CharField(db_column='IsInsurer', max_length=1)  # Field name made lowercase.
    isinsprovider = models.CharField(db_column='IsInsProvider', max_length=1)  # Field name made lowercase.
    isagent = models.CharField(db_column='IsAgent', max_length=1)  # Field name made lowercase.
    isdangertrans = models.CharField(db_column='IsDangerTrans', max_length=1)  # Field name made lowercase.
    isdangerwh = models.CharField(db_column='IsDangerWh', max_length=1)  # Field name made lowercase.
    qualicheck = models.CharField(db_column='QualiCheck', max_length=16, blank=True)  # Field name made lowercase.
    qualicheckdate = models.DateTimeField(db_column='QualiCheckDate', blank=True, null=True)  # Field name made lowercase.
    servicestate = models.CharField(db_column='ServiceState', max_length=64, blank=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='OwnerID', max_length=100, blank=True)  # Field name made lowercase.
    approvedate = models.DateTimeField(db_column='ApproveDate', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=200, blank=True)  # Field name made lowercase.
    isdelete = models.CharField(db_column='IsDelete', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    starlevel = models.CharField(db_column='StarLevel', max_length=40, blank=True)  # Field name made lowercase.
    docmanageperson = models.CharField(db_column='DocManagePerson', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lrc_serviceprovider'


class LrcSpstaff(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    headerid = models.IntegerField(db_column='HeaderID')  # Field name made lowercase.
    staffcode = models.CharField(db_column='StaffCode', max_length=40)  # Field name made lowercase.
    staffname = models.CharField(db_column='StaffName', max_length=50)  # Field name made lowercase.
    idcardno = models.CharField(db_column='IdCardNo', max_length=20, blank=True)  # Field name made lowercase.
    worktype = models.CharField(db_column='WorkType', max_length=20)  # Field name made lowercase.
    mobilephoneno = models.CharField(db_column='MobilePhoneNo', max_length=50, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=150, blank=True)  # Field name made lowercase.
    isenable = models.CharField(db_column='Isenable', max_length=1)  # Field name made lowercase.
    isstatus = models.CharField(db_column='IsStatus', max_length=1)  # Field name made lowercase.
    dlvalidto = models.DateTimeField(db_column='DlValidTo', blank=True, null=True)  # Field name made lowercase.
    dangercertvalidto = models.DateTimeField(db_column='DangerCertValidTo', blank=True, null=True)  # Field name made lowercase.
    supcertvalidto = models.DateTimeField(db_column='SupCertValidTo', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1)  # Field name made lowercase.
    telno = models.CharField(db_column='TelNo', max_length=20, blank=True)  # Field name made lowercase.
    idcardaddress = models.CharField(db_column='IdCardAddress', max_length=150, blank=True)  # Field name made lowercase.
    dlissuedby = models.CharField(db_column='DlIssuedBy', max_length=150, blank=True)  # Field name made lowercase.
    dangercertno = models.CharField(db_column='DangerCertNo', max_length=100, blank=True)  # Field name made lowercase.
    dangercertissuedby = models.CharField(db_column='DangerCertIssuedBy', max_length=150, blank=True)  # Field name made lowercase.
    supcertno = models.CharField(db_column='SupCertNo', max_length=50, blank=True)  # Field name made lowercase.
    supcertissuedby = models.CharField(db_column='SupCertIssuedBy', max_length=150, blank=True)  # Field name made lowercase.
    phyexamcertvalidto = models.DateTimeField(db_column='PhyExamCertValidTo', blank=True, null=True)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.CharField(db_column='IsDelete', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=255, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lrc_spstaff'


class LrcTruck(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    headerid = models.IntegerField(db_column='HeaderID')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    truckcode = models.CharField(db_column='TruckCode', max_length=40)  # Field name made lowercase.
    plateno = models.CharField(db_column='PlateNo', max_length=50)  # Field name made lowercase.
    truckmodel = models.CharField(db_column='TruckModel', max_length=80, blank=True)  # Field name made lowercase.
    truckownertype = models.CharField(db_column='TruckOwnerType', max_length=40)  # Field name made lowercase.
    truckowner = models.CharField(db_column='TruckOwner', max_length=100, blank=True)  # Field name made lowercase.
    truckstatus = models.CharField(db_column='TruckStatus', max_length=50, blank=True)  # Field name made lowercase.
    truckclass = models.CharField(db_column='TruckClass', max_length=50, blank=True)  # Field name made lowercase.
    usecharacter = models.CharField(db_column='UseCharacter', max_length=100, blank=True)  # Field name made lowercase.
    trucklicenseno = models.CharField(db_column='TruckLicenseNo', max_length=80, blank=True)  # Field name made lowercase.
    loadweight = models.DecimalField(db_column='LoadWeight', max_digits=16, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    totalweight = models.DecimalField(db_column='TotalWeight', max_digits=16, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    truckweight = models.DecimalField(db_column='TruckWeight', max_digits=16, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    approveloadweight = models.DecimalField(db_column='ApproveLoadWeight', max_digits=16, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    towweight = models.DecimalField(db_column='TowWeight', max_digits=16, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    approvepassenger = models.DecimalField(db_column='ApprovePassenger', max_digits=16, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    cabpassenger = models.DecimalField(db_column='CabPassenger', max_digits=16, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    innersize = models.CharField(db_column='InnerSize', max_length=80, blank=True)  # Field name made lowercase.
    springnumber = models.DecimalField(db_column='SpringNumber', max_digits=16, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    outsize = models.CharField(db_column='OutSize', max_length=80, blank=True)  # Field name made lowercase.
    tankvolume = models.DecimalField(db_column='TankVolume', max_digits=16, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    purchasedate = models.DateTimeField(db_column='PurchaseDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    trucktype = models.CharField(db_column='TruckType', max_length=40, blank=True)  # Field name made lowercase.
    registerdate = models.DateTimeField(db_column='RegisterDate', blank=True, null=True)  # Field name made lowercase.
    issuedate = models.DateTimeField(db_column='IssueDate', blank=True, null=True)  # Field name made lowercase.
    deliverycode = models.CharField(db_column='DeliveryCode', max_length=80, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=200, blank=True)  # Field name made lowercase.
    validmark = models.CharField(db_column='ValidMark', max_length=20, blank=True)  # Field name made lowercase.
    isdangerallowed = models.CharField(db_column='IsDangerAllowed', max_length=1)  # Field name made lowercase.
    operationvalidto = models.DateTimeField(db_column='OperationValidTo', blank=True, null=True)  # Field name made lowercase.
    pvvalidto = models.DateTimeField(db_column='PvValidTo', blank=True, null=True)  # Field name made lowercase.
    pvcheckno = models.CharField(db_column='PvCheckNo', max_length=80, blank=True)  # Field name made lowercase.
    goodstype = models.CharField(db_column='GoodsType', max_length=50, blank=True)  # Field name made lowercase.
    certno = models.CharField(db_column='CertNo', max_length=50, blank=True)  # Field name made lowercase.
    certdate = models.DateTimeField(db_column='CertDate', blank=True, null=True)  # Field name made lowercase.
    trucklicensevalidto = models.DateTimeField(db_column='TruckLicenseValidTo', blank=True, null=True)  # Field name made lowercase.
    simcardno = models.CharField(db_column='SimCardNo', max_length=50, blank=True)  # Field name made lowercase.
    isdelete = models.CharField(db_column='IsDelete', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    exittime = models.DateTimeField(db_column='ExitTime', blank=True, null=True)  # Field name made lowercase.
    netway = models.CharField(db_column='NetWay', max_length=50, blank=True)  # Field name made lowercase.
    nettime = models.DateTimeField(db_column='NetTime', blank=True, null=True)  # Field name made lowercase.
    isnet = models.CharField(db_column='isNet', max_length=1, blank=True)  # Field name made lowercase.
    gpsprovider = models.CharField(db_column='GpsProvider', max_length=50, blank=True)  # Field name made lowercase.
    gpsunittype = models.CharField(db_column='GpsUnitType', max_length=50, blank=True)  # Field name made lowercase.
    gpsinstalltime = models.DateTimeField(db_column='GpsInstallTime', blank=True, null=True)  # Field name made lowercase.
    gpsservice = models.CharField(db_column='GpsService', max_length=50, blank=True)  # Field name made lowercase.
    isgps = models.CharField(db_column='isGps', max_length=1, blank=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lrc_truck'


class TKeys(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    keyname = models.CharField(db_column='KeyName', unique=True, max_length=255)  # Field name made lowercase.
    nextid = models.BigIntegerField(db_column='NextID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_keys'


class TKeysTest(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    keyname = models.CharField(db_column='KeyName', max_length=255)  # Field name made lowercase.
    nextid = models.BigIntegerField(db_column='NextID', blank=True, null=True)  # Field name made lowercase.
    system = models.CharField(db_column='System', max_length=20, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_keys_test'


class TMdmCity(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    countryid = models.IntegerField(db_column='CountryID')  # Field name made lowercase.
    provinceid = models.ForeignKey('TMdmProvince', db_column='ProvinceID')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    citycode = models.CharField(db_column='CityCode', max_length=20)  # Field name made lowercase.
    cname = models.CharField(db_column='CName', max_length=100)  # Field name made lowercase.
    ename = models.CharField(db_column='EName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=1000, blank=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=200, blank=True)  # Field name made lowercase.
    urlmemo = models.CharField(db_column='UrlMemo', max_length=100, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_city'


class TMdmCodetable(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    classid = models.ForeignKey('TMdmCodetableclass', db_column='ClassID')  # Field name made lowercase.
    ctcode = models.CharField(db_column='CtCode', max_length=100)  # Field name made lowercase.
    ctname = models.CharField(db_column='CtName', max_length=200)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=400, blank=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    ismodifiable = models.CharField(db_column='IsModifiable', max_length=1)  # Field name made lowercase.
    isdeletable = models.CharField(db_column='IsDeletable', max_length=1)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=100, blank=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=100, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_codetable'


class TMdmCodetableclass(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    groupid = models.ForeignKey('TMdmCodetablegroup', db_column='GroupID')  # Field name made lowercase.
    classcode = models.CharField(db_column='ClassCode', max_length=100)  # Field name made lowercase.
    classname = models.CharField(db_column='ClassName', max_length=200)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=400, blank=True)  # Field name made lowercase.
    isaddable = models.CharField(db_column='IsAddable', max_length=1)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_codetableclass'


class TMdmCodetablegroup(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    groupcode = models.CharField(db_column='GroupCode', max_length=100)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=200)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=400, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_codetablegroup'


class TMdmContainer(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    headerid = models.ForeignKey(LrcCompany, db_column='HeaderID')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    containertypecode = models.CharField(db_column='ContainerTypeCode', max_length=40)  # Field name made lowercase.
    ownertype = models.CharField(db_column='OwnerType', max_length=40)  # Field name made lowercase.
    containercode = models.CharField(db_column='ContainerCode', max_length=40)  # Field name made lowercase.
    loadvolume = models.DecimalField(db_column='LoadVolume', max_digits=18, decimal_places=6)  # Field name made lowercase.
    loadweight = models.DecimalField(db_column='LoadWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    tareweight = models.DecimalField(db_column='TareWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    isdelete = models.CharField(db_column='IsDelete', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_container'


class TMdmCountryarea(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cacode = models.CharField(db_column='CaCode', unique=True, max_length=50)  # Field name made lowercase.
    cname = models.CharField(db_column='CName', unique=True, max_length=100)  # Field name made lowercase.
    ename = models.CharField(db_column='EName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    catype = models.CharField(db_column='CaType', max_length=100, blank=True)  # Field name made lowercase.
    countryid = models.IntegerField(db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_countryarea'


class TMdmDistrict(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    countryid = models.IntegerField(db_column='CountryID')  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='ProvinceID')  # Field name made lowercase.
    cityid = models.ForeignKey(TMdmCity, db_column='CityID')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    countycode = models.CharField(db_column='CountyCode', max_length=20)  # Field name made lowercase.
    cname = models.CharField(db_column='CName', max_length=100)  # Field name made lowercase.
    ename = models.CharField(db_column='EName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=1000, blank=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=200, blank=True)  # Field name made lowercase.
    urlmemo = models.CharField(db_column='UrlMemo', max_length=100, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=100)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=100, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_district'


class TMdmItem(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', unique=True, max_length=40)  # Field name made lowercase.
    groupcode = models.CharField(db_column='GroupCode', max_length=200, blank=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=200, blank=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=200, blank=True)  # Field name made lowercase.
    itemdescription = models.CharField(db_column='ItemDescription', max_length=200, blank=True)  # Field name made lowercase.
    itemspec = models.CharField(db_column='ItemSpec', max_length=100, blank=True)  # Field name made lowercase.
    itemclassid1 = models.IntegerField(db_column='ItemClassID1', blank=True, null=True)  # Field name made lowercase.
    itemclassid2 = models.IntegerField(db_column='ItemClassID2', blank=True, null=True)  # Field name made lowercase.
    itemclassid3 = models.IntegerField(db_column='ItemClassID3', blank=True, null=True)  # Field name made lowercase.
    itemclassid4 = models.IntegerField(db_column='ItemClassID4', blank=True, null=True)  # Field name made lowercase.
    itemclassid5 = models.IntegerField(db_column='ItemClassID5', blank=True, null=True)  # Field name made lowercase.
    itemstage = models.CharField(db_column='ItemStage', max_length=40, blank=True)  # Field name made lowercase.
    primaryuom = models.CharField(db_column='PrimaryUom', max_length=40)  # Field name made lowercase.
    transphysicalstate = models.CharField(db_column='TransPhysicalState', max_length=40, blank=True)  # Field name made lowercase.
    storagephysicalstate = models.CharField(db_column='StoragePhysicalState', max_length=40, blank=True)  # Field name made lowercase.
    normalphysicalstate = models.CharField(db_column='NormalPhysicalState', max_length=40, blank=True)  # Field name made lowercase.
    billingtype = models.CharField(db_column='BillingType', max_length=40, blank=True)  # Field name made lowercase.
    ishazardouschemicals = models.CharField(db_column='IsHazardousChemicals', max_length=1, blank=True)  # Field name made lowercase.
    hazchemlistid = models.IntegerField(db_column='HazChemListID', blank=True, null=True)  # Field name made lowercase.
    isdangergoods = models.CharField(db_column='IsDangerGoods', max_length=1, blank=True)  # Field name made lowercase.
    dangergoodsid = models.IntegerField(db_column='DangerGoodsID', blank=True, null=True)  # Field name made lowercase.
    ispoison = models.CharField(db_column='IsPoison', max_length=1, blank=True)  # Field name made lowercase.
    ispoisonraw = models.CharField(db_column='IsPoisonRaw', max_length=1, blank=True)  # Field name made lowercase.
    isexplosionraw = models.CharField(db_column='IsExplosionRaw', max_length=1, blank=True)  # Field name made lowercase.
    msdsid = models.IntegerField(db_column='MsdsID', blank=True, null=True)  # Field name made lowercase.
    statisticsgroupid = models.IntegerField(db_column='StatisticsGroupID', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=400, blank=True)  # Field name made lowercase.
    extcode1 = models.CharField(db_column='ExtCode1', max_length=40, blank=True)  # Field name made lowercase.
    extcode2 = models.CharField(db_column='ExtCode2', max_length=40, blank=True)  # Field name made lowercase.
    extcode3 = models.CharField(db_column='ExtCode3', max_length=40, blank=True)  # Field name made lowercase.
    extcode4 = models.CharField(db_column='ExtCode4', max_length=40, blank=True)  # Field name made lowercase.
    extcode5 = models.CharField(db_column='ExtCode5', max_length=40, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=200, blank=True)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    netweight = models.DecimalField(db_column='NetWeight', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    weightuomcode = models.CharField(db_column='WeightUomCode', max_length=40, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_item'


class TMdmItemtenant(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    itemid = models.ForeignKey(TMdmItem, db_column='ItemID')  # Field name made lowercase.
    itemclassid1 = models.IntegerField(db_column='ItemClassID1', blank=True, null=True)  # Field name made lowercase.
    itemclassid2 = models.IntegerField(db_column='ItemClassID2', blank=True, null=True)  # Field name made lowercase.
    itemclassid3 = models.IntegerField(db_column='ItemClassID3', blank=True, null=True)  # Field name made lowercase.
    itemclassid4 = models.IntegerField(db_column='ItemClassID4', blank=True, null=True)  # Field name made lowercase.
    itemclassid5 = models.IntegerField(db_column='ItemClassID5', blank=True, null=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_itemtenant'


class TMdmItemuom(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    unitcode = models.CharField(db_column='UnitCode', max_length=40)  # Field name made lowercase.
    itemid = models.ForeignKey(TMdmItem, db_column='ItemID')  # Field name made lowercase.
    isprimary = models.CharField(db_column='IsPrimary', max_length=1)  # Field name made lowercase.
    ratio = models.DecimalField(db_column='Ratio', max_digits=22, decimal_places=10)  # Field name made lowercase.
    piececount = models.DecimalField(db_column='PieceCount', max_digits=18, decimal_places=6)  # Field name made lowercase.
    grossweight = models.DecimalField(db_column='GrossWeight', max_digits=12, decimal_places=4)  # Field name made lowercase.
    netweight = models.DecimalField(db_column='NetWeight', max_digits=12, decimal_places=4)  # Field name made lowercase.
    weightuomcode = models.CharField(db_column='WeightUomCode', max_length=40, blank=True)  # Field name made lowercase.
    packinglength = models.DecimalField(db_column='PackingLength', max_digits=12, decimal_places=4)  # Field name made lowercase.
    packingwidth = models.DecimalField(db_column='PackingWidth', max_digits=12, decimal_places=4)  # Field name made lowercase.
    packingheigth = models.DecimalField(db_column='PackingHeigth', max_digits=12, decimal_places=4)  # Field name made lowercase.
    sizeuomcode = models.CharField(db_column='SizeUomCode', max_length=40, blank=True)  # Field name made lowercase.
    volume = models.DecimalField(db_column='Volume', max_digits=12, decimal_places=4)  # Field name made lowercase.
    volumeuomcode = models.CharField(db_column='VolumeUomCode', max_length=40, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=400, blank=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_itemuom'


class TMdmLotsettingheader(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    lotsettingcode = models.CharField(db_column='LotSettingCode', unique=True, max_length=40)  # Field name made lowercase.
    lotsettingname = models.CharField(db_column='LotSettingName', unique=True, max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=400, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=400, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=100)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=100, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_lotsettingheader'


class TMdmLotsettingline(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    headerid = models.ForeignKey(TMdmLotsettingheader, db_column='HeaderID')  # Field name made lowercase.
    lotnocode = models.CharField(db_column='LotNoCode', max_length=40)  # Field name made lowercase.
    displaylabel = models.CharField(db_column='DisplayLabel', max_length=100)  # Field name made lowercase.
    editstyle = models.CharField(db_column='EditStyle', max_length=20)  # Field name made lowercase.
    datasource = models.CharField(db_column='DataSource', max_length=50)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=400, blank=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=100)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=100, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_lotsettingline'


class TMdmLotsettingtenant(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    headerid = models.ForeignKey(TMdmLotsettingheader, db_column='HeaderID')  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=400, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=100)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=100, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_lotsettingtenant'


class TMdmOwner(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    ownercode = models.CharField(db_column='OwnerCode', unique=True, max_length=100)  # Field name made lowercase.
    ownername = models.CharField(db_column='OwnerName', unique=True, max_length=200)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', unique=True, max_length=200)  # Field name made lowercase.
    docprefix = models.CharField(db_column='DocPrefix', max_length=20, blank=True)  # Field name made lowercase.
    ownertype1 = models.CharField(db_column='OwnerType1', max_length=20, blank=True)  # Field name made lowercase.
    ownertype2 = models.CharField(db_column='OwnerType2', max_length=20, blank=True)  # Field name made lowercase.
    ownertype3 = models.CharField(db_column='OwnerType3', max_length=20, blank=True)  # Field name made lowercase.
    ownertype4 = models.CharField(db_column='OwnerType4', max_length=20, blank=True)  # Field name made lowercase.
    ownertype5 = models.CharField(db_column='OwnerType5', max_length=20, blank=True)  # Field name made lowercase.
    superownerid = models.IntegerField(db_column='SuperOwnerID', blank=True, null=True)  # Field name made lowercase.
    ismonthlyrun = models.CharField(db_column='IsMonthlyRun', max_length=1)  # Field name made lowercase.
    ename = models.CharField(db_column='EName', max_length=200, blank=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True)  # Field name made lowercase.
    firstbusinesstime = models.DateTimeField(db_column='FirstBusinessTime', blank=True, null=True)  # Field name made lowercase.
    lasebusinesstime = models.DateTimeField(db_column='LaseBusinessTime', blank=True, null=True)  # Field name made lowercase.
    countgroup = models.CharField(db_column='CountGroup', max_length=40, blank=True)  # Field name made lowercase.
    hostcode = models.CharField(db_column='HostCode', max_length=40, blank=True)  # Field name made lowercase.
    extcode1 = models.CharField(db_column='ExtCode1', max_length=40, blank=True)  # Field name made lowercase.
    extcode2 = models.CharField(db_column='ExtCode2', max_length=40, blank=True)  # Field name made lowercase.
    extcode3 = models.CharField(db_column='ExtCode3', max_length=40, blank=True)  # Field name made lowercase.
    extcode4 = models.CharField(db_column='ExtCode4', max_length=40, blank=True)  # Field name made lowercase.
    extcode5 = models.CharField(db_column='ExtCode5', max_length=40, blank=True)  # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID', blank=True, null=True)  # Field name made lowercase.
    salesorgcode = models.CharField(db_column='SalesOrgCode', max_length=200)  # Field name made lowercase.
    countryid = models.IntegerField(db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='ProvinceID', blank=True, null=True)  # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityID', blank=True, null=True)  # Field name made lowercase.
    countyid = models.IntegerField(db_column='CountyID', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=10, blank=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_owner'


class TMdmParty(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    partycode = models.CharField(db_column='PartyCode', unique=True, max_length=40)  # Field name made lowercase.
    partyname = models.CharField(db_column='PartyName', unique=True, max_length=100)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', unique=True, max_length=100)  # Field name made lowercase.
    countryid = models.IntegerField(db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='ProvinceID', blank=True, null=True)  # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityID', blank=True, null=True)  # Field name made lowercase.
    countyid = models.IntegerField(db_column='CountyID', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=10, blank=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=40, blank=True)  # Field name made lowercase.
    contacttelno = models.CharField(db_column='ContactTelNo', max_length=40, blank=True)  # Field name made lowercase.
    contactfaxno = models.CharField(db_column='ContactFaxNo', max_length=40, blank=True)  # Field name made lowercase.
    contactemail = models.CharField(db_column='ContactEmail', max_length=100, blank=True)  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_party'


class TMdmPartytenant(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    partyid = models.ForeignKey(TMdmParty, db_column='PartyID')  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60, blank=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_partytenant'


class TMdmPlant(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    headerid = models.ForeignKey(TMdmOwner, db_column='HeaderID')  # Field name made lowercase.
    plantcode = models.CharField(db_column='PlantCode', max_length=100)  # Field name made lowercase.
    plantname = models.CharField(db_column='PlantName', max_length=200)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=200)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    shippingpointcode = models.CharField(db_column='ShippingPointCode', max_length=40, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_plant'


class TMdmPort(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    portcode = models.CharField(db_column='PortCode', unique=True, max_length=100)  # Field name made lowercase.
    portname = models.CharField(db_column='PortName', unique=True, max_length=100)  # Field name made lowercase.
    ename = models.CharField(db_column='EName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True)  # Field name made lowercase.
    countryid = models.IntegerField(db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='ProvinceID', blank=True, null=True)  # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityID', blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=200, blank=True)  # Field name made lowercase.
    urlmemo = models.CharField(db_column='UrlMemo', max_length=100, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=1000, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_port'


class TMdmProvince(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    countryid = models.ForeignKey(TMdmCountryarea, db_column='CountryID')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    provincecode = models.CharField(db_column='ProvinceCode', max_length=16)  # Field name made lowercase.
    cname = models.CharField(db_column='CName', max_length=100)  # Field name made lowercase.
    ename = models.CharField(db_column='EName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=1000, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60, blank=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_province'


class TMdmPurchasingorganization(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    headerid = models.ForeignKey(TMdmOwner, db_column='HeaderID')  # Field name made lowercase.
    purorgcode = models.CharField(db_column='PurOrgCode', max_length=100)  # Field name made lowercase.
    purorgname = models.CharField(db_column='PurOrgName', max_length=200)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=200)  # Field name made lowercase.
    docprefix = models.CharField(db_column='DocPrefix', max_length=40, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_purchasingorganization'


class TMdmRailbureau(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rbcode = models.CharField(db_column='RbCode', unique=True, max_length=60)  # Field name made lowercase.
    rbname = models.CharField(db_column='RbName', unique=True, max_length=120)  # Field name made lowercase.
    ename = models.CharField(db_column='EName', max_length=120, blank=True)  # Field name made lowercase.
    ordersort = models.IntegerField(db_column='OrderSort', blank=True, null=True)  # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityID', blank=True, null=True)  # Field name made lowercase.
    countyid = models.IntegerField(db_column='CountyID', blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=128, blank=True)  # Field name made lowercase.
    urlmemo = models.CharField(db_column='UrlMemo', max_length=256, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_railbureau'


class TMdmRailstation(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bureauid = models.ForeignKey(TMdmRailbureau, db_column='BureauID')  # Field name made lowercase.
    rscode = models.CharField(db_column='RsCode', unique=True, max_length=60)  # Field name made lowercase.
    rsname = models.CharField(db_column='RsName', unique=True, max_length=120)  # Field name made lowercase.
    ename = models.CharField(db_column='EName', max_length=120, blank=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityID', blank=True, null=True)  # Field name made lowercase.
    countyid = models.IntegerField(db_column='CountyID', blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_railstation'


class TMdmRoute(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    routecode = models.CharField(db_column='RouteCode', max_length=40)  # Field name made lowercase.
    routename = models.CharField(db_column='RouteName', max_length=100)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=100)  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=100, blank=True)  # Field name made lowercase.
    fromcountryid = models.IntegerField(db_column='FromCountryID', blank=True, null=True)  # Field name made lowercase.
    fromprovinceid = models.IntegerField(db_column='FromProvinceID', blank=True, null=True)  # Field name made lowercase.
    fromcityid = models.IntegerField(db_column='FromCityID', blank=True, null=True)  # Field name made lowercase.
    fromdistrictid = models.IntegerField(db_column='FromDistrictID', blank=True, null=True)  # Field name made lowercase.
    fromaddress = models.CharField(db_column='FromAddress', max_length=200, blank=True)  # Field name made lowercase.
    frompostcode = models.CharField(db_column='FromPostCode', max_length=10, blank=True)  # Field name made lowercase.
    tocountryid = models.IntegerField(db_column='ToCountryID', blank=True, null=True)  # Field name made lowercase.
    toprovinceid = models.IntegerField(db_column='ToProvinceID', blank=True, null=True)  # Field name made lowercase.
    tocityid = models.IntegerField(db_column='ToCityID', blank=True, null=True)  # Field name made lowercase.
    todistrictid = models.IntegerField(db_column='ToDistrictID', blank=True, null=True)  # Field name made lowercase.
    toaddress = models.CharField(db_column='ToAddress', max_length=200, blank=True)  # Field name made lowercase.
    topostcode = models.CharField(db_column='ToPostCode', max_length=10, blank=True)  # Field name made lowercase.
    distance = models.DecimalField(db_column='Distance', max_digits=18, decimal_places=6)  # Field name made lowercase.
    transmodecode = models.CharField(db_column='TransModeCode', max_length=40, blank=True)  # Field name made lowercase.
    servicecompanyid = models.IntegerField(db_column='ServiceCompanyID', blank=True, null=True)  # Field name made lowercase.
    transittime = models.DecimalField(db_column='TransitTime', max_digits=18, decimal_places=6)  # Field name made lowercase.
    leadtime = models.DecimalField(db_column='LeadTime', max_digits=18, decimal_places=6)  # Field name made lowercase.
    drivingtime = models.DecimalField(db_column='DrivingTime', max_digits=18, decimal_places=6)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_route'


class TMdmSalesorganization(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    headerid = models.ForeignKey(TMdmOwner, db_column='HeaderID')  # Field name made lowercase.
    salesorgcode = models.CharField(db_column='SalesOrgCode', unique=True, max_length=100)  # Field name made lowercase.
    salesorgname = models.CharField(db_column='SalesOrgName', unique=True, max_length=200)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', unique=True, max_length=200)  # Field name made lowercase.
    docprefix = models.CharField(db_column='DocPrefix', max_length=40, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_salesorganization'


class TMdmSapinterfacesetting(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID', blank=True, null=True)  # Field name made lowercase.
    systemtype = models.CharField(db_column='SystemType', max_length=20)  # Field name made lowercase.
    companycode = models.CharField(db_column='CompanyCode', unique=True, max_length=100)  # Field name made lowercase.
    systemcode = models.CharField(db_column='SystemCode', max_length=100)  # Field name made lowercase.
    sapclient = models.CharField(db_column='SAPClient', max_length=100)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=100)  # Field name made lowercase.
    commuser = models.CharField(db_column='CommUser', max_length=100)  # Field name made lowercase.
    commpassword = models.CharField(db_column='CommPassword', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60, blank=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_sapinterfacesetting'


class TMdmTenantitemclass(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    groupcode = models.CharField(db_column='GroupCode', max_length=40)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=40)  # Field name made lowercase.
    photourl = models.CharField(db_column='PhotoUrl', max_length=200, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=400, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_tenantitemclass'


class TMdmTown(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    countryid = models.IntegerField(db_column='CountryID')  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='ProvinceID')  # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityID')  # Field name made lowercase.
    countyid = models.ForeignKey(TMdmDistrict, db_column='CountyID')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    towncode = models.CharField(db_column='TownCode', max_length=16)  # Field name made lowercase.
    cname = models.CharField(db_column='CName', max_length=100)  # Field name made lowercase.
    ename = models.CharField(db_column='EName', max_length=100, blank=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=1000, blank=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=200, blank=True)  # Field name made lowercase.
    urlmemo = models.CharField(db_column='UrlMemo', max_length=100, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60, blank=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_town'


class TMdmTransportdistance(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    startpointcode = models.CharField(db_column='StartPointCode', max_length=40, blank=True)  # Field name made lowercase.
    endpointcode = models.CharField(db_column='EndPointCode', max_length=40, blank=True)  # Field name made lowercase.
    distance = models.DecimalField(db_column='Distance', max_digits=18, decimal_places=6)  # Field name made lowercase.
    transmodecode = models.CharField(db_column='TransModeCode', max_length=40, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_transportdistance'


class TMdmTransportplanningpoint(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    headerid = models.IntegerField(db_column='HeaderID')  # Field name made lowercase.
    pointcode = models.CharField(db_column='PointCode', max_length=100)  # Field name made lowercase.
    pointname = models.CharField(db_column='PointName', max_length=200)  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=100, blank=True)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=200)  # Field name made lowercase.
    docprefix = models.CharField(db_column='DocPrefix', max_length=40, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_transportplanningpoint'


class TMdmTransporttime(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    lowerweight = models.DecimalField(db_column='LowerWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    upperweight = models.DecimalField(db_column='UpperWeight', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lowerdistance = models.DecimalField(db_column='LowerDistance', max_digits=18, decimal_places=6)  # Field name made lowercase.
    upperdistance = models.DecimalField(db_column='UpperDistance', max_digits=18, decimal_places=6)  # Field name made lowercase.
    transittime = models.DecimalField(db_column='TransitTime', max_digits=18, decimal_places=6)  # Field name made lowercase.
    pickuptime = models.DecimalField(db_column='PickupTime', max_digits=18, decimal_places=6)  # Field name made lowercase.
    deliverytime = models.DecimalField(db_column='DeliveryTime', max_digits=18, decimal_places=6)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_transporttime'


class TMdmUom(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    unitcode = models.CharField(db_column='UnitCode', unique=True, max_length=100)  # Field name made lowercase.
    unitname = models.CharField(db_column='UnitName', max_length=100)  # Field name made lowercase.
    unitename = models.CharField(db_column='UnitEname', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True)  # Field name made lowercase.
    isphysical = models.CharField(db_column='IsPhysical', max_length=1)  # Field name made lowercase.
    dimension = models.CharField(db_column='Dimension', max_length=100, blank=True)  # Field name made lowercase.
    isprimaryunit = models.CharField(db_column='IsPrimaryUnit', max_length=1)  # Field name made lowercase.
    ratio = models.DecimalField(db_column='Ratio', max_digits=18, decimal_places=8)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=100)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=100, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_uom'


class TMdmWarehouse(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    warehousecode = models.CharField(db_column='WarehouseCode', max_length=40)  # Field name made lowercase.
    warehousename = models.CharField(db_column='WarehouseName', max_length=100)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=100)  # Field name made lowercase.
    docprefix = models.CharField(db_column='DocPrefix', max_length=40, blank=True)  # Field name made lowercase.
    countryid = models.IntegerField(db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='ProvinceID', blank=True, null=True)  # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityID', blank=True, null=True)  # Field name made lowercase.
    countyid = models.IntegerField(db_column='CountyID', blank=True, null=True)  # Field name made lowercase.
    provincecode = models.CharField(db_column='ProvinceCode', max_length=40, blank=True)  # Field name made lowercase.
    citycode = models.CharField(db_column='CityCode', max_length=40, blank=True)  # Field name made lowercase.
    countycode = models.CharField(db_column='CountyCode', max_length=40, blank=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=10, blank=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    railstationid = models.IntegerField(db_column='RailStationID', blank=True, null=True)  # Field name made lowercase.
    railline = models.CharField(db_column='RailLine', max_length=100, blank=True)  # Field name made lowercase.
    portid = models.IntegerField(db_column='PortID', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID')  # Field name made lowercase.
    assettype = models.CharField(db_column='AssetType', max_length=40)  # Field name made lowercase.
    isinventoryaging = models.CharField(db_column='IsInventoryAging', max_length=1)  # Field name made lowercase.
    istransfer = models.CharField(db_column='IsTransfer', max_length=1)  # Field name made lowercase.
    iswmrun = models.CharField(db_column='IsWmRun', max_length=1)  # Field name made lowercase.
    isplantwarehouse = models.CharField(db_column='IsPlantWarehouse', max_length=1)  # Field name made lowercase.
    hostcode = models.CharField(db_column='HostCode', max_length=40, blank=True)  # Field name made lowercase.
    ishostdata = models.CharField(db_column='IsHostData', max_length=10, blank=True)  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=40, blank=True)  # Field name made lowercase.
    contacttelno = models.CharField(db_column='ContactTelNo', max_length=40, blank=True)  # Field name made lowercase.
    contactfaxno = models.CharField(db_column='ContactFaxNo', max_length=40, blank=True)  # Field name made lowercase.
    contactemal = models.CharField(db_column='ContactEmal', max_length=100, blank=True)  # Field name made lowercase.
    receiptunit = models.CharField(db_column='ReceiptUnit', max_length=100, blank=True)  # Field name made lowercase.
    recipient = models.CharField(db_column='Recipient', max_length=100, blank=True)  # Field name made lowercase.
    receiptaddress = models.CharField(db_column='ReceiptAddress', max_length=100, blank=True)  # Field name made lowercase.
    receiptzipcode = models.CharField(db_column='ReceiptZipCode', max_length=20, blank=True)  # Field name made lowercase.
    receipttelno = models.CharField(db_column='ReceiptTelNo', max_length=40, blank=True)  # Field name made lowercase.
    receiptfaxno = models.CharField(db_column='ReceiptFaxNo', max_length=40, blank=True)  # Field name made lowercase.
    isvirtual = models.CharField(db_column='IsVirtual', max_length=1)  # Field name made lowercase.
    hintcode = models.CharField(db_column='HintCode', max_length=100, blank=True)  # Field name made lowercase.
    plantcode = models.CharField(db_column='PlantCode', max_length=40, blank=True)  # Field name made lowercase.
    servicecompanyid = models.IntegerField(db_column='ServiceCompanyID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_warehouse'


class TMdmWarehousecapacity(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    warehouseid = models.ForeignKey(TMdmWarehouse, db_column='WarehouseID')  # Field name made lowercase.
    tenantid = models.IntegerField(db_column='TenantID')  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.
    storagearea = models.DecimalField(db_column='StorageArea', max_digits=10, decimal_places=0)  # Field name made lowercase.
    capacity = models.DecimalField(db_column='Capacity', max_digits=10, decimal_places=0)  # Field name made lowercase.
    maxwarncapacity = models.DecimalField(db_column='MaxWarnCapacity', max_digits=10, decimal_places=0)  # Field name made lowercase.
    minwarncapacity = models.DecimalField(db_column='MinWarnCapacity', max_digits=10, decimal_places=0)  # Field name made lowercase.
    dailyloadcapacity = models.DecimalField(db_column='DailyLoadCapacity', max_digits=10, decimal_places=0)  # Field name made lowercase.
    storagetype = models.CharField(db_column='StorageType', max_length=40)  # Field name made lowercase.
    initcapacity = models.DecimalField(db_column='InitCapacity', max_digits=10, decimal_places=0)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mdm_warehousecapacity'


class TTenant(models.Model):
    tenantid = models.IntegerField(db_column='TenantID', primary_key=True)  # Field name made lowercase.
    tenantcode = models.CharField(db_column='TenantCode', unique=True, max_length=40)  # Field name made lowercase.
    tenantname = models.CharField(db_column='TenantName', unique=True, max_length=120)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', unique=True, max_length=60)  # Field name made lowercase.
    tenanttypeid = models.CharField(db_column='TenantTypeID', max_length=12, blank=True)  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='ProvinceID')  # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityID')  # Field name made lowercase.
    districtid = models.IntegerField(db_column='DistrictID')  # Field name made lowercase.
    townid = models.IntegerField(db_column='TownID')  # Field name made lowercase.
    adrress = models.CharField(db_column='Adrress', max_length=200, blank=True)  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=60, blank=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='PhoneNo', max_length=60, blank=True)  # Field name made lowercase.
    mobilephoneno = models.CharField(db_column='MobilePhoneNo', max_length=60, blank=True)  # Field name made lowercase.
    faxnumber = models.CharField(db_column='FaxNumber', max_length=60, blank=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=120)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=400, blank=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    createduser = models.CharField(db_column='CreatedUser', max_length=60)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    modifieduser = models.CharField(db_column='ModifiedUser', max_length=60, blank=True)  # Field name made lowercase.
    lastwrittentime = models.DateTimeField(db_column='LastWrittenTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_tenant'


class Test(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'test'

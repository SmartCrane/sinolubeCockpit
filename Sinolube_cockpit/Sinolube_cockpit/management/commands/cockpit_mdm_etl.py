# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand, CommandError
from MDMEtl.models import TMdmOwner,TMdmPlant,TTenant,TMdmWarehouse,TMdmWarehousecapacity
from cockpit.models import LuOwner,LuPlant,LuTenant,LuWarehouse
import datetime,logging,time
from django.db import transaction, connection

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    def handle(self, *args, **options):
        # 初始化Lu_owner
        etlOwnerData('1')
        #初始化lu_plant
        eltPlantData('1')
        #初始化Lu_tenant
        etltenantData('1')
        #初始化仓库
        etlwarehouseData('1')
def etlOwnerData(self):
    owners = TMdmOwner.objects.all();
    for owner in owners:
        tenantid = owner.tenantid
        ownerid = owner.id
        ownername = owner.ownername
        ownershortname = owner.shortname
        luowner = LuOwner(tenantid=tenantid,ownerid=ownerid,ownername=ownername,ownershortname=ownershortname)
        luowner.save()
def eltPlantData(self):
    plants = TMdmPlant.objects.all()
    for plant in plants:
        plantid = plant.id
        plantname = plant.plantname
        plantshortname = plant.shortname
        plantcode = plant.plantcode
        headerid = plant.headerid.id
        luplant = LuPlant(plantid=plantid,plantname=plantname,plantshortname=plantshortname,plantcode=plantcode,headerid=headerid)
        luplant.save()
def etltenantData(self):
    tenants = TTenant.objects.all()
    for tenant in tenants:
        tenantid = tenant.tenantid
        tenantname = tenant.tenantname
        tenantshortname = tenant.shortname
        lutenant = LuTenant(tenantid=tenantid,tenantname=tenantname,tenantshortname=tenantshortname)
        lutenant.save()
def etlwarehouseData(self):
    warehouses = TMdmWarehouse.objects.all()
    for warehouse in warehouses:
        warehouseid = warehouse.id
        warehousename = warehouse.warehousename
        warehouseshortname = warehouse.shortname
        plantcode=  warehouse.plantcode
        if TMdmWarehousecapacity.objects.filter(warehouseid=warehouseid).count() == 0:
            luwarehouse = LuWarehouse(warehouseid=warehouseid, warehousename=warehousename,
                                      warehouseshortname=warehouseshortname, plantcode=plantcode,
                                      maxwarncapacity=0, minwarncapacity=0)
            luwarehouse.save()
        else:
            for capacity in TMdmWarehousecapacity.objects.filter(warehouseid=warehouseid):
                maxwarncapacity = capacity.maxwarncapacity
                minwarncapacity = capacity.minwarncapacity
                luwarehouse = LuWarehouse(warehouseid=warehouseid,warehousename=warehousename,warehouseshortname=warehouseshortname,plantcode=plantcode,
                                          maxwarncapacity=maxwarncapacity,minwarncapacity=minwarncapacity)
                luwarehouse.save()





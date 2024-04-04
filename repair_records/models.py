from django.db import models
from datetime import datetime

from supplies.models import SuppliesInfo
from vehicles.models import VehicleInfo


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        abstract = True


class RepairRecord(BaseModel):
    RecordName = models.CharField(choices=(('维修', '维修'), ('保养', '保养')), max_length=2,
                                  verbose_name='维保种类')
    vehicle = models.ForeignKey(VehicleInfo, on_delete=models.CASCADE,verbose_name="记录车辆",)
    usedSupplies = models.ManyToManyField(SuppliesInfo,verbose_name='使用配件', related_name='repair_records')
    work_time = models.IntegerField(verbose_name='工时')
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2,default=50.00, verbose_name='工时单价')
    finish_time = models.DateTimeField(verbose_name='交付时间',default=None)

    def cost(self):
        supplies_cost = self.usedSupplies.all().aggregate(total_cost=models.Sum('price'))['total_cost']
        supplies_cost = supplies_cost or 0
        return self.work_time * self.price_per_hour + supplies_cost

    cost.short_description = '费用（元）'


    class Meta:
        verbose_name = '维保记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.add_time) + '-' + str(self.vehicle.name)+'-'+str(self.vehicle.user.username)


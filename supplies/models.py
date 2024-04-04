from django.db import models

from datetime import datetime
from vehicles.models import VariantInfo, BrandInfo


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        abstract = True


class Supplier(BaseModel):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Supplies_category(BaseModel):
    name = models.CharField(max_length=20, verbose_name='配件分类')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='供应商')
    brand = models.ForeignKey(BrandInfo, verbose_name='适用品牌', on_delete=models.CASCADE,default='通用')

    class Meta:
        verbose_name = '配件种类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


class SuppliesInfo(BaseModel):
    variant = models.ForeignKey(VariantInfo, verbose_name="车型",on_delete=models.CASCADE)
    category = models.ForeignKey(Supplies_category, verbose_name='配件种类', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name="配件名称")
    price = models.DecimalField(max_digits=8, decimal_places=2,verbose_name="单价")
    description = models.CharField(verbose_name="配件描述", max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='supplies/%Y/%m/%d/', verbose_name="配件图片", null=True, blank=True)
    number = models.IntegerField(verbose_name="库存数量", default=0)

    class Meta:
        verbose_name = "配件信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

from django.db import models
from datetime import datetime


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        abstract = True


class BrandInfo(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='品牌')

    class Meta:
        verbose_name = '品牌信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


class Product_Year_Month(BaseModel):
    year = models.CharField(max_length=4,verbose_name='年份')
    month = models.CharField(max_length=2,verbose_name='月份',default=1)

    class Meta:
        verbose_name = '生产年月'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.year) + '年' + str(self.month) + '月'


class VariantInfo(BaseModel):
    brand = models.ForeignKey(BrandInfo, on_delete=models.CASCADE, verbose_name='品牌')
    name = models.CharField(max_length=20, verbose_name='车型')
    product_Year_Month = models.ForeignKey(Product_Year_Month, verbose_name='生产年月', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '车型信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


from users.models import UserProfile


class VehicleInfo(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    name = models.CharField(max_length=20, verbose_name="车辆名称")
    variant = models.ForeignKey(VariantInfo, on_delete=models.CASCADE,verbose_name="车型")
    VIN = models.CharField(max_length=20, verbose_name="车架号")
    color = models.CharField(max_length=20, verbose_name="颜色")
    image = models.ImageField(upload_to='vehicles/%Y/%m/%d/', default='/VehicleDefaultImg.jpg',
                              verbose_name="车辆照片")

    class Meta:
        verbose_name = '车辆信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user.username)+ '的' + str(self.name)


class Massage(BaseModel):
    title = models.CharField(max_length=200, verbose_name="消息")
    vehicle = models.ForeignKey(VehicleInfo, verbose_name="车辆", on_delete=models.CASCADE)
    has_read = models.BooleanField(default=False, verbose_name="已读状态")

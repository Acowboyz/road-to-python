from django.db import models

# Create your models here.

class CartInfo(models.Model):
    cuser = models.ForeignKey('df_user.UserInfo')
    cgoods = models.ForeignKey('df_goods.GoodsInfo')
    ccount = models.IntegerField()

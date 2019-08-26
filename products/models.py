from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')
    icon=models.ImageField(upload_to='images/')
    url = models.TextField()
    vote=models.IntegerField(default=1)
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)# Kullanıcı hesabı silindiğinde ona ait olan ürünlerde silinir.

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


class Votes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title


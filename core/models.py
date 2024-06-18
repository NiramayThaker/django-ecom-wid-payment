from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
	id = models.AutoField(primary_key=True)  # Corrected definition
	name = models.CharField(max_length=50)
	category = models.CharField(max_length=50, default='')
	sub_category = models.CharField(max_length=50, default='')
	price = models.IntegerField()
	desc = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/images')

	def __str__(self):
		return f"{self.name} at ₹{self.price}"


# class Order(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	p_id = models.IntegerField()


class UserOrders(models.Model):
	p_id = models.IntegerField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)

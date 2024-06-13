from django.db import models

# Create your models here.
class Product(models.Model):
	id = models.AutoField
	name = models.CharField(max_length=50)
	category = models.CharField(max_length=50, default='')
	sub_category = models.CharField(max_length=50, default='')
	price = models.IntegerField()
	desc = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/images')

	def __str__(self):
		return f"{self.name} at ₹{self.price}"

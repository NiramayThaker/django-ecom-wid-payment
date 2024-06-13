from django.db import models


# Create your models here.
class ContactUs(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	desc = models.CharField(max_length=50)
	phone_number = models.IntegerField()

	def __str__(self):
		return f"{self.email} - {self.phone_number}"

from django.db import models


class Our_Service(models.Model):
	service_name = models.CharField('Service name',max_length=250)
	Stages = models.CharField(max_length=250)
	Price = models.CharField(max_length=250)

	def __str__(self):
		return self.service_name




class Dental_Procedure(models.Model):
	service_name = models.CharField('Service name',max_length=250)
	Stages = models.CharField(max_length=250)
	Price = models.CharField(max_length=250)

	def __str__(self):
		return self.service_name


class Blog_Post(models.Model):
	Blog_title = models.CharField(max_length=250)
	Img_Blog = models.ImageField(null=True, blank=True, upload_to="images/")
	Blog_content = models.TextField()

	def __str__(self):
		return self.Blog_title

class Testimonial(models.Model):
	Img_testimonial = models.ImageField(null=True, blank=True, upload_to="images/")
	Testimonial_content = models.TextField(max_length=1000)
	Testimonial_Name = models.CharField(max_length=250)
	Testimonial_Identity = models.CharField(max_length=250)

	def __str__(self):
		return self.Testimonial_content











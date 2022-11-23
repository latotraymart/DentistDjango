from django.contrib import admin

from . import models
from .models import Blog_Post
from .models import Testimonial





class Dental_AdminArea(admin.AdminSite):
	site_header = 'Ap Dental Clinic Admin'

dental_site = Dental_AdminArea(name='DentalAdmin')

dental_site.register(models.Dental_Procedure)
dental_site.register(Blog_Post)
dental_site.register(Testimonial)

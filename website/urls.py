from django.urls import path
from . import views
from website.admin import dental_site

urlpatterns = [
	path('', views.home, name="home"),
	path('contact.html', views.contact, name="contact"),
	path('about.html', views.about, name="about"),
	path('pricing.html', views.pricing, name="pricing"),
	path('service.html', views.service, name="service"),
	path('appointmen1.html', views.appointment1, name="appointment1"),
	path('appointment.html', views.appointment, name="appointment"),
    path('blog.html', views.blog, name="blog"),

    path('DentalAdmin/',dental_site.urls),
    
]

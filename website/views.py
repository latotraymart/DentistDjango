from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
from .models import Our_Service
from .models import Dental_Procedure
from .models import Blog_Post
from .models import Testimonial


def home(request):
	service_list = Dental_Procedure.objects.all()
	testimonial_list = Testimonial.objects.all()
	blog_list = Blog_Post.objects.all()
	context = {'service_list':service_list,'testimonial_list':testimonial_list,'blog_list':blog_list}
	return render(request, 'home.html', context)


	

	

def contact(request):
	if request.method == "POST":
		message_name = request.POST.get('message-name')
		message_email = request.POST.get('message-email')
		message = request.POST.get('message')
	


		

		#send email
		send_mail(
		'Message from ' + message_email, #subject
		message, #message
		message_email, # from email
		['lacson.joandale@dfcamclp.edu.ph'], # to email
		fail_silently=False
		)
		return render(request, 'contact.html', {'message_name': message_name})


	else:
		
		return render(request, 'contact.html', )


def about(request):

	testimonial_list = Testimonial.objects.all()
	return render(request, 'about.html', {'testimonial_list': testimonial_list})
	



def pricing(request):
	service_list = Dental_Procedure.objects.all()
	return render(request, 'pricing.html', {'service_list': service_list})


def service(request):
	testimonial_list = Testimonial.objects.all()
	blog_list = Blog_Post.objects.all()
	context = {'testimonial_list':testimonial_list,'blog_list':blog_list}
	return render(request, 'service.html', context)
def appointment1(request):

	if request.method == "POST":
		your_name = request.POST.get('your-name')
		your_phone = request.POST.get('your-phone')
		your_email = request.POST.get('your-email')
		your_address = request.POST.get('your-address')
		your_schedule = request.POST.get('your-schedule')
		your_date = request.POST.get('your-date')
		your_message = request.POST.get('your-message')
		
	

		#send email
		appointment = "Name:" + your_name + "\n" +" Phone: " + your_phone + "\n" +"Email: " + your_email + "\n" +"Address: " + your_address + "\n" +"Schedule: " + your_schedule + "\n" +"Date: " + your_date + "\n" +"Message: " + your_message
		
		send_mail(
		'Appointment Request', #subject

		appointment, #message
		your_email, # from email
		['lacson.joandale@dfcamclp.edu.ph'], # to email
		fail_silently=False
		)
	 	
		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address, 
			'your_schedule': your_schedule,
			'your_date': your_date,
			'your_message': your_message
			})

	
		

	else:
		
		return render(request, 'home.html', )

def appointment(request):

	return render(request, 'appointment.html', {})

def blog(request):
	blog_list = Blog_Post.objects.all()

	return render(request, 'blog.html', {'blog_list': blog_list})

	




	




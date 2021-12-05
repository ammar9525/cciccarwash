from django.shortcuts import render
from django.http import HttpResponse
from car_care.models import Detail
# from django.views.generic import TemplateView
# from django.core.mail import send_mail
# Create your views here.
def index(request):
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     phone = request.POST['phone']
    #     car_id = request.POST['car_id']
    #     service_cat = request.POST['service_cat']
    #     date = request.POST['date']
    #     time = request.POST['time']
    #     print(name, phone, car_id, service_cat, date, time)
    #     ins = Detail(customer_name=name, customer_phone=phone, car_id=car_id, service_cat=service_cat,date=date,time=time )
    #     ins.save()
    #     send_mail(
    #         name,
    #         service_cat,
    #         'neesharansari12341@gmail.com',
    #         ['neesharansari12341@gmail.com'],
    #         fail_silently=False,
    #     )
        # print("the data has been written to the db")
    return render(request, 'ccic_app/home.html')
def about(request):
    return render(request, 'ccic_app/about.html')
def services(request):
    return render(request, 'ccic_app/services.html')
def contact(request):
    return render(request, 'ccic_app/contact.html')
def booking(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        car_id = request.POST['car_id']
        service_cat = request.POST['service_cat']
        date = request.POST['date']
        time = request.POST['time']
        print(name, phone, car_id, service_cat, date, time)
        ins = Detail(customer_name=name, customer_phone=phone, car_id=car_id, service_cat=service_cat,date=date,time=time )
        ins.save()
       
        print("the data has been written to the db")

    return render(request, 'ccic_app/booking.html')
def gallery(request):
    return render(request, 'ccic_app/gallery.html')

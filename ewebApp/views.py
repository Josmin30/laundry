from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import Http404
# Create your views here.


def base(request):
    return render(request,"base.html")
def ba(request):
    return render(request,"ba.html")
def index(request):
    return render(request,'index.html')
def customer(request):
    return render(request,'customer.html')
def customerreg(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        a = Customer.objects.create(name=name,phone=phone,email=email,password=password)
        a.save()
        b= User.objects.create_user(username=name,password=password)
        b.save()

    return render(request,'customerreg.html')

def order(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        location = request.POST['location']
        date = request.POST['date']
        quantity = request.POST['quantity']
        details = request.POST['details']
       
        a = Order.objects.create(name=name,email=email,phone=phone,address=address,location=location,date=date,quantity=quantity,details=details)
        a.save()
    return render(request,'order.html')
def contact(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        message = request.POST['message']
        a = Contact.objects.create(name=name,email=email ,phone_no=phone_no,message=message)
        a.save()
    return render(request,'contact.html')
def service(request):
    return render(request,'service.html')
def manreg(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        section = request.POST['section']
        salary = request.POST['salary']
        password = request.POST['password']
        a=Manager.objects.create(name=name,email=email,phone=phone,section=section,salary=salary,password=password)
        a.save()
        b= User.objects.create_user(username=name,password=password,is_staff=1)
        b.save()
    return render(request,'manreg.html')

def empreg(request):
    uid = request.session['id']
    u = Manager.objects.get(id=uid)                                 
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        section = request.POST['section']
        salary = request.POST['salary']
        password = request.POST['password']
        a=Employee.objects.create(name=name,email=email,phone=phone,section=section,salary=salary,password=password,manager=u)
        a.save()
        b= User.objects.create_user(username=name,password=password,first_name='Employee',is_staff=1)
        b.save()
    return render(request,'empreg.html')
def manager(request):
    return render(request,'manager.html')
def employee(request):
    return render(request,'employee.html')
def adminHome(request):
    return render(request,'adminHome.html')
def login(request):
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            if user.is_superuser == 1:
                return redirect("/adminHome")
            elif user.is_staff == 1:
                if user.first_name == 'Employee':
                    empl =Employee.objects.get(name=username)
                    request.session["id"]=empl.id
                    return redirect("/employee")
                else:
                    manager = Manager.objects.get(name=username)
                    request.session["id"]=manager.id  
                    return redirect("/manager")
            else:
                customer =Customer.objects.get(name=username)
                request.session["id"]=customer.id
                return redirect("/customer")
        else:
            messages.info(request,"User dosent exist")
        
    return render(request,"login.html")
def vieworder(request):
    data = Order.objects.all()
    return render(request,"vieworder.html",{"data":data})
def update(request):
    order_id = request.GET.get('id')
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return redirect('/')  # Redirect to the home page or appropriate error page

    if request.method == 'POST':
        order.name = request.POST.get('name')
        order.email = request.POST.get('email')
        order.phone = request.POST.get('phone')
        order.address = request.POST.get('address')
        order.location = request.POST.get('location')
        order.date = request.POST.get('date')
        order.quantity = request.POST.get('quantity')
        order.details = request.POST.get('details')
        order.save()
        return redirect('/customer')  # Redirect to the home page or the page where orders are displayed

    return render(request, 'update.html', {'order': order})
def updel(request):
    orders = Order.objects.all()  # Fetch all orders to display in the table
    return render(request, 'updel.html', {'data': orders})

def delete(request):
    try:
        order_id = request.GET.get('id')
        order = Order.objects.get(id=order_id)
        order.delete()
        return redirect("/updel")
    except Order.DoesNotExist:
        raise Http404("Order does not exist")

def viewemployee(request):
    data = Employee.objects.all()
    return render(request,'viewemployee.html',{"data":data})
def viewmanager(request):
    data = Manager.objects.all()
    return render(request,"viewmanager.html",{"data":data})
def emplist(request):
    uid = request.session['id']
    u = Manager.objects.get(id=uid)
    data = Employee.objects.filter(manager_id=u.id)
    return render(request,'emplist.html',{"data":data})
def orderlist(request):
    uid = request.session['id']
    u = Customer.objects.get(id=uid)
    data = Order.objects.filter(customer__id=u.id)
    return render(request,'orderlist.html',{"data":data})

def active(request):
    id = request.GET.get('id')
    p = Order.objects.get(id=id)
    p.status = "OnGoing"
    progress=50
    p.save()
    return redirect("/status")

def complete(request):
    id = request.GET.get('id')
    p = Order.objects.get(id=id)
    p.status = "Completed"
    progress = 100
    p.save()
    return redirect("/status")
def status(request):
    if 'id' in request.session:
        user_id = request.session['id']
        user = Employee.objects.get(id=user_id)
        orders = Order.objects.filter(customer_id=user.id)
        return render(request, 'status.html', {"orders": orders})
    else:
        return redirect("/login")
    
def pricelist(request):
    return render(request,'pricelist.html')

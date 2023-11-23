from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
import re
from django.contrib.auth import authenticate,login
from . models import *

# Create your views here.


def login_page(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=uname, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, str("Invalid Credentials"))
            return redirect(request.META['HTTP_REFERER'])
    return render(request,"login.html")

def login_check(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    user = User.objects.filter(username=username).first()
    if not user:
        return JsonResponse({"message": "Invalid Datas", "status": "error"})
    elif not user.check_password(password):
        return JsonResponse({"message": "Invalid Password", "status": "error"})
    else:
        return JsonResponse({"message": "success", "status": "success"})

def register(request):
    if request.method == "POST":
        messages.success(request, str("Successfully Registered"))
        return redirect("/")
    return render(request,"register.html")


def register_data(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        email = request.POST.get("email").strip()
        password = request.POST.get("password").strip()
        required_fields = []
        if not username:
            required_fields.append("Username")
        if not email:
            required_fields.append("email")
        if not password:
            required_fields.append("password")
        if required_fields:
            response = f"{', '.join(required_fields)} are required"
            return JsonResponse({"message": response, "status": "error"})
        if User.objects.filter(username=username).exists():
            return JsonResponse({"message": "username exists", "status": "error"})
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return JsonResponse({"message": "not a valid email", "status": "error"})
        user = User.objects.create_user(username=username,email=email,password=password)
        return JsonResponse({"message": "success", "status": "success"})


def dashboard(request):
    if request.method == "POST":
        messages.success(request, str("Success"))
        return redirect("dashboard")
    data = EmployeeDetails.objects.filter(auth_user=request.user)
    context = {
        'data':data
    }
    return render(request,"dashboard.html",context)


def create_employee(request):
    if request.method == "POST":
        name = request.POST.get("name").strip()
        phone = request.POST.get("phone").strip()
        email = request.POST.get("email").strip()
        age = request.POST.get("age").strip()
        required_fields = []
        if not name:
            required_fields.append("Name")
        if not email:
            required_fields.append("Email")
        if not phone:
            required_fields.append("Phone")
        if required_fields:
            response = f"{', '.join(required_fields)} are required"
            return JsonResponse({"message": response, "status": "error"})
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return JsonResponse({"message": "not a valid email", "status": "error"})
        data_create = EmployeeDetails.objects.create(
            auth_user = request.user,
            name=name,
            email=email,
            age=age,
            phone=phone
        )
        return JsonResponse({"message": "success", "status": "success"})


def edit_employee(request):
    id = request.GET.get("id")
    data = EmployeeDetails.objects.get(id=id)
    context = {
        'data':data
    }
    return render(request,"edit_employee.html",context)


def edit_employee_action(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        name = request.POST.get("name").strip()
        phone = request.POST.get("phone").strip()
        email = request.POST.get("email").strip()
        age = request.POST.get("age").strip()
        required_fields = []
        if not name:
            required_fields.append("Name")
        if not email:
            required_fields.append("Email")
        if not phone:
            required_fields.append("Phone")
        if required_fields:
            response = f"{', '.join(required_fields)} are required"
            return JsonResponse({"message": response, "status": "error"})
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return JsonResponse({"message": "not a valid email", "status": "error"})
        data_update = EmployeeDetails.objects.filter(id=employee_id).update(
            name=name,
            email=email,
            age=age,
            phone=phone
        )
        return JsonResponse({"message": "success", "status": "success"})


def delete_employee(request,id):
    data = EmployeeDetails.objects.get(id=id)
    data.delete()
    messages.success(request, str("Deleted"))
    return redirect("dashboard")
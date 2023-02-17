from django.shortcuts import render, redirect
import random
from MedicsApp.models import User
from django.contrib import messages
from django.core.mail import send_mail
from ProjMedics import settings

# Create your views here.

def index(request):
    return render(request, "index.html")

def fof(request):
    return render(request, "404.html")

def mainCategory(request):
    return render(request, "main-category.html")

def brandList(request):
    return render(request, "brand-list.html")

def invoice(request):
    return render(request, "invoice.html")

def newOrder(request):
    return render(request, "new-order.html")

def orderDetail(request):
    return render(request, "order-detail.html")

def orderHistory(request):
    return render(request, "order-history.html")

def productAdd(request):
    return render(request, "product-add.html")

def productDetail(request):
    return render(request, "product-detail.html")

def productGrid(request):
    return render(request, "product-grid.html")

def productList(request):
    return render(request, "product-list.html")

def reviewList(request):
    return render(request, "review-list.html")

def subCategory(request):
    return render(request, "sub-category.html")

def userCard(request):
    return render(request, "user-card.html")

def userList(request):
    return render(request, "user-list.html")

def userProfile(request):
    return render(request, "user-profile.html")

def vendorCard(request):
    return render(request, "vendor-card.html")

def vendorList(request):
    return render(request, "vendor-list.html")   

def login(request):
     if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        val = User.objects.filter(Email=email, Password=password).count()
        print("-------------------", email, "---------------------", password)
        if val == 1:
            data = User.objects.filter(Email=email, Password=password)
            for item in data:
                request.session['id'] = item.UserId
                request.session['fname'] = item.FirstName
                request.session['lname'] = item.LastName
                request.session['email'] = item.Email
                if request.POST.get("remember"):
                    response = redirect("/index/")
                    response.set_cookie("cookie_Admin_Email", request.POST["email"], 3600 * 24 * 365 * 20)
                    response.set_cookie("cookie_Admin_Password", request.POST["password"], 3600 * 24 * 365 * 20)
                    return response
            return redirect('/index/')
        else:
            messages.error(request, "Invalid Email or Password")
            return redirect('/login/')
     else:
        if request.COOKIES.get("cookie_Admin_Email"):
            return render(request,"sign-in.html",{'admin_email_cookie1':request.COOKIES['cookie_admin_email'],'admin_password_cookie2':request.COOKIES['cookie_admin_password']})
        else:
            return render(request, "sign-in.html")

def register(request):
    return render(request, "sign-up.html")

def vprofile(request):
    return render(request, "vendor-profile.html")

def forgotPass(request):
    return render(request, "forgotpassword.html")

def send_otp(request):

    otp1 = random.randint(10000, 99999)
    e = request.POST['email']
    request.session['temail']= e

    obj = User.objects.filter(Email=e).count()

    if obj == 1:
        val = User.objects.filter(Email=e).update(otp=otp1 , otp_used=0)
        subject = 'OTP Verification'
        message = str(otp1)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, 'set_password.html')
    return render(request, "forgotpassword.html")


def set_password(request):

    if request.method == "POST":

        T_otp = request.POST['otp']
        T_pass = request.POST['password']
        T_cpass = request.POST['cpassword']

        if T_pass == T_cpass:

            e = request.session['temail']
            val = User.objects.filter(Email=e, otp= T_otp, otp_used=0).count()

            if val == 1:
                User.objects.filter(Email = e).update(otp_used = 1,password = T_pass)
                return redirect("/index")
            else:
                messages.error(request,"Invalid OTP")
                return render(request,"set_password.html")

        else:
            messages.error(request,"New password and Confirm password does not match ")
            return render(request,"set_password.html")

    else:
        return redirect("/forgotPass")

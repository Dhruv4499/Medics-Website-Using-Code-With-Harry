"""ProjMedics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from MedicsApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('MedicsApp/',include('MedicsApp.urls'))
    path('index/',views.index, name="index"),
    path('404/',views.fof, name="404"),
    path('login/',views.login, name="login"),
    path('register/',views.register, name="register"),
    path('vprofile/',views.vprofile, name="vprofile"),
    path('forgotPass/',views.forgotPass, name="forgotPass"),
    path('send_otp/', views.send_otp, name="sendOtp"),
    path('mainCategory/', views.mainCategory, name="mainCategory"),
    path('brandList/', views.brandList, name="brandList"),
    path('invoice/', views.invoice, name="invoice"),
    path('newOrder/', views.newOrder, name="newOrder"),
    path('orderDetail/', views.orderDetail, name="orderDetail"),
    path('orderHistory/', views.orderHistory, name="orderHistory"),
    path('productAdd/', views.productAdd, name="productAdd"),
    path('productDetail/', views.productDetail, name="productDetail"),
    path('productList/', views.productList, name="productList"),
    path('reviewList/', views.reviewList, name="reviewList"),
    path('subCategory/', views.subCategory, name="subCategory"),
    path('userCard/', views.userCard, name="userCard"),
    path('userList/', views.userList, name="userList"),
    path('userProfile/', views.userProfile, name="userProfile"),
    path('vendorCard/', views.vendorCard, name="vendorCard"),
    path('vendorList/', views.vendorList, name="vendorList"),
]

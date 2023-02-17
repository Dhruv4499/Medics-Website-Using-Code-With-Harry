# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('',views.index,name="ShopHome"),
#     path('about/',views.about,name="aboutus"),
#     path('contact/',views.contact,name="contactus"),
#     path('product/<int:myid>',views.Product,name="product"),
#     path('search/',views.search,name="search"),
#     path('tracker/',views.tracker,name="tracker"),
#     path('checkout/',views.checkout,name="checkout"),
#     path('handlerequest/',views.handlerequest,name="handlerequest")
# ]

from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="Search"),
    path("product/<int:myid>",views.Product,name="ProductView"),
    path("checkout/",views.checkout,name="Checkout"),
    path("handlerequest/",views.handlerequest,name="HandleRequest"),

]

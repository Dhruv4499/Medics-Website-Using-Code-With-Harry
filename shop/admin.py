from django.contrib import admin

# Register your models here.
# from .models import State , Area , City , User , Store , Product , Category , Sub_Category , Sub_Sub_Category , Order , Order_Status , Payment , Payment_Status , Payment_Type , Role , Blog_Category , Feedback , Medicine , Health_Condition 

from .models import Product
from .models import Contact
from .models import Orders
from .models import OrderUpdate

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)

# admin.site.register(State)
# admin.site.register(Area)
# admin.site.register(City)
# admin.site.register(User)
# admin.site.register(Store)
# admin.site.register(Product)
# admin.site.register(Category)
# admin.site.register(Sub_Category)
# admin.site.register(Sub_Sub_Category)
# admin.site.register(Order)
# admin.site.register(Order_Status)
# admin.site.register(Payment)
# admin.site.register(Payment_Status)
# admin.site.register(Payment_Type)
# admin.site.register(Role)
# admin.site.register(Blog_Category)
# admin.site.register(Feedback)
# admin.site.register(Medicine)
# admin.site.register(Health_Condition)
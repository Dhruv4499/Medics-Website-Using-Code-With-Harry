from django.db import models

# Create your models here.

# class State(models.Model):
#     id = models.AutoField(primary_key=True,default=0)
#     name = models.CharField(max_length=25)
    
#     def __str__(self):
#         return self.name
        
# class City(models.Model):
#     id = models.AutoField(primary_key=True,default=0)
#     name = models.CharField(max_length=25)
#     State.id = models.ForeignKey('State', on_delete=models.CASCADE,null=True)
    
#     def __str__(self):
#         return self.name

# class Area(models.Model):
#     id = models.AutoField(primary_key=True,default=0)
#     name = models.CharField(max_length=25)
#     zipcode = models.IntegerField(default=0)
#     City.id = models.ForeignKey('City', on_delete=models.CASCADE,null=True)
    
#     def __str__(self):
#         return self.name

# class User(models.Model):
#     id = models.AutoField(primary_key=True,default=0)
#     username = models.CharField(max_length=25)
#     firstname = models.CharField(max_length=15)
#     lastname = models.CharField(max_length=15)
#     password = models.CharField(max_length=20)
#     mobile_number = models.IntegerField(default=0)
#     email = models.EmailField(max_length=25)
#     address = models.CharField(max_length=60)
#     security_question = models.CharField(max_length=30)
#     security_answer = models.CharField(max_length=15)
#     Area.id = models.ForeignKey('Area', on_delete=models.CASCADE,null=True)
#     City.id = models.ForeignKey('City', on_delete=models.CASCADE,null=True)
#     State.id = models.ForeignKey('State', on_delete=models.CASCADE,null=True)

#     def __str__(self):
#         return self.firstname + '' + lastname
        
# class Store(models.Model):
#     id = models.AutoField(primary_key=True,default=0)
#     name = models.CharField(max_length=30)
#     address = models.CharField(max_length=50)
#     owner_name = models.CharField(max_length=30)
#     owner_email = models.CharField(max_length=30)
#     license_number = models.CharField(max_length=20)
#     mobile_number = models.IntegerField(default=0)
#     User.id = models.ForeignKey('User', on_delete=models.CASCADE,null=True)

#     def __str__(self):
#         return self.store

# class Category(models.Model):
#     id = models.AutoField(primary_key=True,default=0)
#     name = models.CharField(max_length=10)

#     def __str__(self):
#         return self.name
        
# class Sub_Category(models.Model):
#     id = models.AutoField(primary_key=True,default=0)
#     name = models.CharField(max_length=10)
#     Category.id = models.ForeignKey(Category,to_field="id",on_delete=models.CASCADE,null=True)

#     def __str__(self):
#         return self.name
        
# class Sub_Sub_Category(models.Model):
#     id = models.AutoField(primary_key=True,default=0)
#     name = models.CharField(max_length=10)
#     Sub_Category.id = models.ForeignKey('Sub_Category', on_delete=models.CASCADE,null=True)

#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=25)
#     price = models.IntegerField(default=0)
#     image = models.ImageField(upload_to='shop/images',default='')
#     quantity = models.IntegerField(default=1)
#     category = models.CharField(max_length=30,default=0)
#     Sub_Category.id = models.ForeignKey('Sub_Category', on_delete=models.CASCADE,null=True)
#     Sub_Sub_Category.id = models.ForeignKey('Sub_Sub_Category', on_delete=models.CASCADE,null=True)
#     Store.id = models.ForeignKey('Store', on_delete=models.CASCADE,null=True)
#     # Health_Condition.id = models.ForeignKey('Health_Condition', on_delete=models.CASCADE,null=True)

#     def __str__(self):
#         return self.name

# class Order(models.Model):
#     id = models.AutoField(primary_key=True,default=0)
#     date = models.DateField()
#     User = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
#     Product.id = models.ForeignKey('Product', on_delete=models.CASCADE,null=True)
#     # Order_Status.id = models.ForeignKey('Order_Status', on_delete=models.CASCADE,null=True)
#     # Payment.id = models.ForeignKey('Payment', on_delete=models.CASCADE,null=True)

#     def __str__(self):
#         return self.date

# class Order_Status(models.Model):
#     id = models.AutoField(primary_key=True,default=0)
#     status = models.CharField(max_length=30)

#     def __str__(self):
#         return self.status

# class Payment(models.Model):
#     id = models.AutoField(primary_key=True,default=0)
#     amount = models.IntegerField(default=0)
#     date = models.DateField()
#     User.id = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
#     # Payment_Status.id = models.ForeignKey('Payment_Status', on_delete=models.CASCADE,null=True)

#     def __str__(self):
#         return self.id

# class Payment_Status(models.Model):
#     id = models.AutoField(primary_key=True,default=0)  
#     status = models.CharField(max_length=30)

#     def __str__(self):
#         return self.status
        
# class Payment_Type(models.Model):
#     id = models.AutoField(primary_key=True,default=0)  
#     type = models.CharField(max_length=30)

#     def __str__(self):
#         return self.type
        
# class Role(models.Model):
#     id = models.AutoField(primary_key=True,default='')  
#     type = models.CharField(max_length=30)

#     def __str__(self):
#         return self.type
        
# class Blog_Category(models.Model):
#     id = models.AutoField(primary_key=True)  
#     type = models.CharField(max_length=30)

#     def __str__(self):
#         return self.type  

# class Feedback(models.Model):
#     id = models.AutoField(primary_key=True)  
#     description = models.TextField(max_length=250,blank=True)
#     date = models.DateField()
#     User.id = models.ForeignKey('User', on_delete=models.CASCADE,null=True)

#     def __str__(self):
#         return self._type

# class Medicine(models.Model):
#     id = models.AutoField(primary_key=True)
#     company = models.CharField(max_length=15)
#     name = models.CharField(max_length=20)
#     price = models.IntegerField(default='')
#     MFD = models.DateField(default='')
#     expire_date = models.DateField(default='')
#     quantity = models.IntegerField(default='')
#     Product.id = models.ForeignKey('Product', on_delete=models.CASCADE,null=True)
#     # Health_Condition.id = models.ForeignKey('Health_Condition', on_delete=models.CASCADE,null=True)

#     def __str__(self):
#         return self.name
    
# class Health_Condition(models.Model):
#     id = models.AutoField(primary_key=True)  
#     name = models.CharField(max_length=45)

#     def __str__(self):
#         return self.name      

from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    # subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."


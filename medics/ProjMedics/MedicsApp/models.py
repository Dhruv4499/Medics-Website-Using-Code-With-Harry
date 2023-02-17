from django.db import models

# Create your models here.
class State(models.Model):
    StateId=models.CharField(primary_key=True,max_length=10)
    StateName=models.CharField(max_length=25,null=False)
    
    class Meta:
        db_table='State'

class City(models.Model):
    CityId=models.CharField(primary_key=True,max_length=10)
    CityName=models.CharField(max_length=25,null=False)
    StateId=models.ForeignKey(State,to_field='StateId',on_delete=models.CASCADE)

    class Meta:
        db_table='City'

class Area(models.Model):
    AreaId=models.CharField(primary_key=True,max_length=10)
    AreaName=models.CharField(max_length=25,null=False)
    CityId=models.ForeignKey(City,to_field='CityId',on_delete=models.CASCADE)

    class Meta:
        db_table='Area'


class Role(models.Model):
    RoleId=models.CharField(primary_key=True,max_length=10)
    RoleName=models.CharField(max_length=15,null=False)

    class Meta:
        db_table='Role'

class User(models.Model):
    UserId=models.CharField(primary_key=True,max_length=10)
    UserName=models.CharField(max_length=25,null=False)
    FirstName=models.CharField(max_length=15,null=False)
    LastName=models.CharField(max_length=15,null=False)
    Password=models.CharField(max_length=25,null=False)
    Mobile= models.IntegerField(max_length=10,null=False,default="")
    Email=models.EmailField(max_length=25,null=False)
    Address=models.CharField(max_length=60,null=False)
    AreaId=models.ForeignKey(Area,to_field='AreaId',on_delete=models.CASCADE)
    CityId=models.ForeignKey(City,to_field='CityId',on_delete=models.CASCADE)
    StateId=models.ForeignKey(State,to_field='StateId',on_delete=models.CASCADE)
    SecurityQuestion=models.CharField(max_length=30,null=False)
    SecurityAnswer=models.CharField(max_length=15,null=False)
    RoleId=models.ForeignKey(Role,to_field='RoleId',on_delete=models.CASCADE)
    otp=models.IntegerField(null=False)
    otp_used=models.IntegerField(null=False)

    class Meta:
        db_table='User'

class Store(models.Model):
    StoreId=models.CharField(primary_key=True,max_length=10)
    StoreName=models.CharField(max_length=30,null=False)
    Address=models.CharField(max_length=50,null=False)
    OwnerName=models.CharField(max_length=30,null=False)
    OwnerEmail=models.EmailField(max_length=30,null=False)
    LicenseNumnber=models.IntegerField(max_length=20,null=False,default="")
    Mobile=models.IntegerField(max_length=10,null=False,default="")
    UserId=models.ForeignKey(User,to_field='UserId',on_delete=models.CASCADE)

    class Meta:
        db_table='Store'
    
class Category(models.Model):
    CatId=models.CharField(primary_key=True,max_length=10)
    CatName=models.CharField(max_length=10,null=False)

    class Meta:
        db_table='Category'

class SubCategory(models.Model):
    SubCatId=models.CharField(primary_key=True,max_length=10)
    SubCatName=models.CharField(max_length=10,null=False)
    CatId=models.ForeignKey(Category,to_field='CatId',on_delete=models.CASCADE)

    class Meta:
        db_table='SubCategory'

class SubSubCategory(models.Model):
    SubSubCatId=models.CharField(primary_key=True,max_length=10)
    SubSubCatName=models.CharField(max_length=10,null=False)
    SubCatId=models.ForeignKey(SubCategory,to_field='SubCatId',on_delete=models.CASCADE)

    class Meta:
        db_table='SubSubCategory'

class HealthCondition(models.Model):
    HcId=models.CharField(primary_key=True,max_length=10)
    HcName=models.CharField(max_length=45,null=False)

    class Meta:
        db_table='HealthCondition'

class Product(models.Model):
    ProductId=models.CharField(primary_key=True,max_length=10)
    ProductName=models.CharField(max_length=25,null=False)
    ProductPrice=models.DecimalField(max_digits=5,decimal_places=2,null=False)
    ProductQty=models.IntegerField(max_length=5,null=False,default="")
    ProductImage=models.ImageField(upload_to="shop/images",default="")
    SubCatId=models.ForeignKey(SubCategory,to_field='SubCatId',on_delete=models.CASCADE)
    SubSubCatId=models.ForeignKey(SubSubCategory,to_field='SubSubCatId',on_delete=models.CASCADE)
    StoreId=models.ForeignKey(Store,to_field='StoreId',on_delete=models.CASCADE)
    HCId=models.ForeignKey(HealthCondition,to_field='HcId',on_delete=models.CASCADE)

    class Meta:
        db_table='Product'

class OrderStatus(models.Model):
    OrderStatusId=models.CharField(primary_key=True,max_length=10)
    Status=models.CharField(max_length=30,null=False)

    class Meta:
        db_table='OrderStatus'

class PaymentStatus(models.Model):
    PaymentStatusId=models.CharField(primary_key=True,max_length=10)
    PaymentStatus=models.CharField(max_length=25,null=False)

    class Meta:
        db_table='PaymentStatus'

class PaymentType(models.Model):
    PaymentTypeId=models.CharField(primary_key=True,max_length=10)
    PaymentType=models.CharField(max_length=30,null=False)

    class Meta:
        db_table='PaymentType'

class Payment(models.Model):
    PaymentId=models.CharField(primary_key=True,max_length=10)
    PaymentAmunt=models.DecimalField(max_digits=5,decimal_places=2,null=False)
    PaymentDate=models.DateTimeField(null=False)
    PaymentTypeId=models.ForeignKey(PaymentType,to_field='PaymentTypeId',on_delete=models.CASCADE)
    UserId=models.ForeignKey(User,to_field='UserId',on_delete=models.CASCADE)
    PaymentStatusId=models.ForeignKey(PaymentStatus,to_field='PaymentStatusId',on_delete=models.CASCADE)

    class Meta:
        db_table='Payment'

class Order(models.Model):
    OrderId=models.CharField(primary_key=True,max_length=10)
    UserId=models.ForeignKey(User,to_field='UserId',on_delete=models.CASCADE)
    ProductId=models.ForeignKey(Product,to_field='ProductId',on_delete=models.CASCADE)
    OrderDate=models.DateTimeField(null=False)
    OrderStatusId=models.ForeignKey(OrderStatus,to_field='OrderStatusId',on_delete=models.CASCADE)
    PaymentID=models.ForeignKey(Payment,to_field='PaymentId',on_delete=models.CASCADE)

    class Meta:
        db_table='Order'

class BlogCategory(models.Model):
    BlogId=models.CharField(primary_key=True,max_length=10)
    BlogType=models.CharField(max_length=15,null=False)

    class Meta:
        db_table='BlogCategory'


class FeedBack(models.Model):
    FeedBackId=models.CharField(primary_key=True,max_length=10)
    FeedBackDate=models.DateField()
    FeedBackDesc=models.CharField(max_length=250,null=False)
    UserId=models.ForeignKey(User,to_field='UserId',on_delete=models.CASCADE)

    class Meta:
        db_table='FeedBack'
   

class Medicine(models.Model):
    BatchId=models.CharField(primary_key=True,max_length=10)
    Company=models.CharField(max_length=15,null=False)
    Name=models.CharField(max_length=20,null=False)
    MFG=models.DateField()
    EXPDate=models.DateField()
    Qty=models.IntegerField(max_length=10,null=False,default="")
    ProductId=models.ForeignKey(Product,to_field='ProductId',on_delete=models.CASCADE)
    HCId=models.ForeignKey(HealthCondition,to_field='HcId',on_delete=models.CASCADE)

    class Meta:
        db_table='Medicine'

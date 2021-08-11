from django.db import models

# Create your models here.


class Cat(models.Model):
   name=models.CharField(max_length=50)
   def __str__(self):
      return self.name

class Book(models.Model):
    status_book=[
       ('available','available'),
       ('Not_avalible','Not_avalible'),
                           ]

    title=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    book_photo=models.ImageField(upload_to='photos',null=True , blank=True ,default='photos\got.jpg')
    author_photo=models.ImageField(upload_to='photos',null=True , blank=True)
    pages=models.IntegerField(null=True,blank=True)
    price=models.DecimalField(max_digits=5 , decimal_places=2)
    borrow_book_Price_day=models.IntegerField(null=True,blank=True)
    borrow_book_period=models.IntegerField(null=True,blank=True)
    active=models.BooleanField(default=True)
    status=models.CharField(max_length=50, choices=status_book,null=True,default='available')
    category=models.ForeignKey(Cat,on_delete=models.PROTECT , null=True,blank=True)
    class Meta:
      db_table="bo"
 

class sign_up(models.Model):
   first_name=models.CharField(max_length=50,null=True,blank=True,default='USER')
   last_name=models.CharField(max_length=50,null=True,blank=True)
   email=models.CharField(max_length=50,null=True,blank=True)
   password=models.CharField(max_length=50,null=True,blank=True)

   def __str__(self):
         return self.first_name or ' '

class log_in(models.Model):
   username=models.CharField(max_length=50,null=True,blank=True)
   password=models.CharField(max_length=50,null=True,blank=True)
   def __str__(self):
         return self.username or ' '

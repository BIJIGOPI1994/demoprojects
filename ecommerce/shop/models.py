from django.db import models

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=200)
    dese=models.TextField()
    image=models.ImageField(upload_to='shop/categories',blank=True,null=True)
    def __str__(self):
        return self.name
class product(models.Model):
    name=models.CharField(max_length=200) 
    dese=models.TextField()  
    image=models.ImageField(upload_to='shop/categories',blank=True,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(category,on_delete=models.CASCADE)#one to many
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
from django.db import models
from django.forms import ModelForm
import os
from django.contrib.auth.models import User

# Create your models here.
def get_upload_path(instance, filename):
    return os.path.join(
        "pics",
        str(instance.id),
        filename
    )

class Categorys(models.Model):
    img = models.ImageField(upload_to=get_upload_path)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

STOCK = (
    ('Stock Available','Stock Available'),
    ('Out of stock','Out of stock')
)   

class Products(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField( max_length=100)
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    flavour = models.CharField(max_length=100,default='chocolate')
    original_price = models.IntegerField()
    final_price = models.IntegerField(default=0,null=False)
    shape = models.CharField(max_length=50)
    size = models.IntegerField(default='6')
    stock = models.CharField(choices=STOCK,default='Stock Available', max_length=30)
  
class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['img','name','category','flavour','original_price','final_price','shape','size','stock']

class CategoryForm(ModelForm):
    class meta:
        model = Categorys
        fields = ['img','name']

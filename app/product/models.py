from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=150)
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering=['-id']
class Tag(models.Model):
    tag_name=models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.tag_name
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=150)
    image=models.ImageField(upload_to="product/image/")
    movie=models.FileField(upload_to='product/movie/')
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    published=models.DateTimeField(default=timezone.now)
    tag=models.ManyToManyField(Tag)
    Category=models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering=['-id']
    

class Actor(models.Model):
    image=models.ImageField(upload_to='actor/')
    full_name=models.CharField(max_length=50)
    full_name_movie=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.full_name
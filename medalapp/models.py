from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")
    price = models.PositiveBigIntegerField()
    sell = models.PositiveBigIntegerField()
    description = models.TextField()
    views = models.PositiveBigIntegerField()
    
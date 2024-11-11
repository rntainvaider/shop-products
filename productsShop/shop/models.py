from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='categories/')

    def __str__(self) -> str:
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='cubcategories/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.category.name} - {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image_small = models.ImageField(upload_to='products/small/')
    image_medium = models.ImageField(upload_to='products/medium/')
    image_big = models.ImageField(upload_to='products/big/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Categories(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class CategoryProducts(models.Model):
    name = models.CharField(max_length=60)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(CategoryProducts, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=60)
    category_id = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE)
    slug = models.CharField(max_length=60)
    content = models.CharField(max_length=255)
    price = models.IntegerField()
    code = models.CharField(max_length=8)
    post = models.TextField()
    slug = models.SlugField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Products, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Pictures(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    path = models.FileField(upload_to='uploads/images', blank=True)

    def save(self, *args, **kwargs):
        super(Pictures, self).save(*args, **kwargs)
        filename = self.path.url
        print(filename)

class Carts(models.Model):
    name = models.CharField(max_length=40)
    addrress = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    request = models.CharField(max_length=150)

class Orders(models.Model):
    cart_id = models.ForeignKey(Carts, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    count = models.IntegerField()

class Posts(models.Model):
    content = RichTextField()
    title = models.CharField(max_length=60)
    image = models.FileField(upload_to='uploads/images', blank=True)
    slug = models.SlugField(max_length=60)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Products, self).save(*args, **kwargs)
    
    def __str__(self):
        return '%s' % self.title

class Chats(models.Model):
    date = models.DateTimeField()

class TextCharts(models.Model):
    chat_id = models.ForeignKey(Chats, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    who = models.BooleanField()
from django.db import models

# Create your models here.

class Info(models.Model):
    logo_name = models.CharField(max_length = 500, blank=True)
    title_name = models.CharField(max_length = 500, blank=True)
    title_name_russian = models.CharField(max_length = 500, blank=True)
    email_1 = models.CharField(max_length = 500, blank=True)
    email_2 = models.CharField(max_length = 500, blank=True)
    phone_1 = models.CharField(max_length = 500, blank=True)
    phone_2 = models.CharField(max_length = 500, blank=True)
    address_1 = models.CharField(max_length = 500, blank=True)
    address_1_russian = models.CharField(max_length = 500, blank=True)
    address_2 = models.CharField(max_length = 500, blank=True)
    address_2_russian = models.CharField(max_length = 500, blank=True)
    work_hours = models.CharField(max_length = 500, blank=True)
    instagram_link = models.CharField(max_length = 500, blank=True)
    tiktok_link = models.CharField(max_length = 500, blank=True)
    telegram_link = models.CharField(max_length = 500, blank=True)

    def __str__(self):
        return self.logo_name

    class Meta:
        verbose_name = "Site info"
        verbose_name_plural = "Site info"


class Aboutus(models.Model):
    title = models.CharField(max_length = 500, blank=True)
    text = models.TextField(blank=True)
    title_russian = models.CharField(max_length = 500, blank=True)
    text_russian = models.TextField(blank=True)

    class Meta:
        verbose_name = "About us"
        verbose_name_plural = "About us"

class Slider(models.Model):
    image = models.ImageField(upload_to='images', blank=True)

class Stats(models.Model):
    happy_clients = models.CharField(max_length=100, blank=True)
    translations = models.CharField(max_length=100, blank=True)
    support = models.CharField(max_length=100, blank=True)
    team = models.CharField(max_length=100, blank=True)

    class Meta: 
        verbose_name = "Statistics"
        verbose_name_plural = "Statistics"

class FAQ(models.Model):
    question = models.TextField(blank=True)
    answer = models.TextField(blank=True)
    question_russian = models.TextField(blank=True)
    answer_russian = models.TextField(blank=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"


class HeroSection(models.Model):
    title = models.CharField(max_length = 500, blank=True)
    description = models.TextField(blank=True)
    title_russian = models.CharField(max_length = 500, blank=True)
    description_russian = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"


class Service(models.Model):
    icon = models.CharField(max_length = 100, blank=True)
    color = models.CharField(max_length = 100, blank=True)
    title = models.CharField(max_length = 250, blank=True)
    short_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    title_russian = models.CharField(max_length = 250, blank=True)
    short_description_russian = models.TextField(blank=True)
    full_description_russian = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    image_russian = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title
    
class ITservice(models.Model):
    icon = models.CharField(max_length = 100, blank=True)
    color = models.CharField(max_length = 100, blank=True)
    title = models.CharField(max_length = 250, blank=True)
    short_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    title_russian = models.CharField(max_length = 250, blank=True)
    short_description_russian = models.TextField(blank=True)
    full_description_russian = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "IT services"    
        verbose_name = "IT service"    

class Category(models.Model):
    name = models.CharField(max_length = 250, blank=True)
    name_russian = models.CharField(max_length = 250, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', default=None, blank=True)
    name = models.CharField(max_length = 250, blank=True)
    description = models.TextField(blank=True)
    name_russian = models.CharField(max_length = 250, blank=True)
    description_russian = models.TextField(blank=True)
    price = models.FloatField(null=True, blank=True, default=None)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name
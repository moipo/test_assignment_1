from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=1000,null = True, default = "", blank = True)
    actions_detail = models.CharField(max_length=1000, null = True, default = "", blank = True)
    image = models.CharField(max_length=1000,null = True, default = "", blank = True)
    category = models.ManyToManyField("Category", blank = True)
    gotolink = models.CharField(max_length=1000, null = True, default = "", blank = True)
    products_xml_link = models.CharField(max_length=1000,null = True, default = "", blank = True)
    updated_at = models.DateTimeField(auto_now = True, null = True, blank = True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=1000, default = "", blank = True)
    image = models.ImageField(upload_to = "uploads", default = "default.jpeg", null = True, blank = True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=1000, null = True, default = "", blank = True)
    model = models.CharField(max_length=1000, null = True, default = "", blank = True)
    price = models.IntegerField(null = True, blank = True)
    image = models.CharField(max_length=1000, null = True, default = "", blank = True)
    url = models.CharField(max_length=1000, null = True, default = "", blank = True)
    program = models.ForeignKey("Program", blank = True, null = True, on_delete=  models.SET_NULL)
    updated_at = models.DateTimeField(auto_now = True, null = True, blank = True)

    def __str__(self):
        return self.name

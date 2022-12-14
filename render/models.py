from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name= models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name

class Cars(models.Model):
    name = models.CharField(max_length=64)
    color = models.CharField(max_length=32)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name



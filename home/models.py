from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField()
    question = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "students"
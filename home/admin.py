from django.contrib import admin
from . models import students



class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','question']


admin.site.register(students,StudentsAdmin)

from pyexpat import model
from django.contrib import admin
from .models import vehicle,User,SuperUser
# Register your models here.
@admin.register(vehicle)
class vehicleAdmin(admin.ModelAdmin):
    list_display=['vehicle_no','vehicle_type','vehicle_model','vehicle_desc']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['fullname','email']

@admin.register(SuperUser)
class SuperUserAdmin(admin.ModelAdmin):
    list_display=['username','full_name']

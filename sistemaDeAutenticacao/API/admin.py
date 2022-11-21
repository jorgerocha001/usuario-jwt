from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from API.models import Usuario

# Register your models here.

class Usuarios(UserAdmin):
    list_display = ['id','username', 'is_staff','email']
    search_fields = ( 'username', 'email')
    ordering = ['username']

admin.site.register(Usuario, Usuarios)
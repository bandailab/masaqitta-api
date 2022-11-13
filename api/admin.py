from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User, Tweet, Grade

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Grade)

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': 
        ('password', 'username')}),
        ('Property', {'fields': ('fullname', 'grade', 'image_url', 'following')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('username', 'username', 'is_staff')
    list_filter = ('username', 'is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(User, MyUserAdmin)

from django.contrib import admin

# Register your models here.


from django.contrib import admin
from django.contrib.auth import get_user_model
from django.forms import TextInput, Textarea, CharField
from django.db import models
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ('name',)
    list_filter = ('name',  'price', 'id')
    ordering = ('price','stock_count')
    list_display = ('name','id',
                    'price', 'stock_count')
    fieldsets = (
        (None, {'fields': ('name', 'price','stock_count')}),

    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    list_per_page = 5
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id', 'name',  'price', 'stock_count')}
         ),
    )


admin.site.register(Product, ProductAdmin)
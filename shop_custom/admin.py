from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin
from tags.models import Tag, TaggedItem
from shop.admin import ProductAdmin
from shop.models import Product

# Register your models here.


class TagInline(GenericTabularInline):
  autocomplete_fields = ['tag']
  model = TaggedItem


class CustomProductAdmin(ProductAdmin):
  inlines = [TagInline]
  
admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
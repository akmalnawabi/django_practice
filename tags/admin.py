from django.contrib import admin
from .models import Tag, TaggedItem
# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  search_fields = ['label']
  
  
@admin.register(TaggedItem)
class TaggedItemAdmin(admin.ModelAdmin):
  search_fields = ['tag__label']
  
  def get_queryset(self, request):
    return super().get_queryset(request).select_related('tag')
from django.contrib import admin
from .models import Product , Tag , Category , Actor
# Register your models here.

@admin.register(Product)
class ProductAdim(admin.ModelAdmin):
    list_display=['name', "created","updated", "published"]
    search_fields=['name']
    # prepopulated_fields={'slug':('name')}

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Actor)


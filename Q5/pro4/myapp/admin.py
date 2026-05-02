from django.contrib import admin
from .models import Product, Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]


admin.site.register(Product, ProductAdmin)
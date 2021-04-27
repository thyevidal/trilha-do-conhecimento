from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "slug", "autor", "criacao", "publicacao")
    prepopulated_fields = {"slug": ("titulo",)}
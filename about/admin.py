from django.contrib import admin
from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date', )


admin.site.register(About, AboutAdmin)
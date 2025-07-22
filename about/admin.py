from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'updated_at')
    ordering = ('-updated_at',)
    search_fields = ('title', 'content')
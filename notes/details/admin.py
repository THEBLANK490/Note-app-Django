from django.contrib import admin
from details.models import Note

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title','content','created_at','modified_at']

admin.site.register(Note, NoteAdmin)

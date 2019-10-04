
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Note

# admin.site.register(Note)

class NoteResource(resources.ModelResource):
   class Meta:
        model = Note
class NoteAdmin(ImportExportModelAdmin):
    resource_class = NoteResource
    # inlines = [SOPDetailInline]
    list_display = ('seq','subject','detail')
    # list_filter = ['is_active',]
    # ordering = ('app','page')
    
    search_fields = ['subject','detail']
   
admin.site.register(Note, NoteAdmin)
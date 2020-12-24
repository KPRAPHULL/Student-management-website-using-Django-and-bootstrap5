from django.contrib import admin

# Register your models here.
from StudentApp.models import StudentModel
# admin.site.register(StudentModel)

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    # dict=StudentModel.DisplayFields
    list_display=StudentModel.DisplayFields
    search_fields=StudentModel.SearchFields
    list_filter=StudentModel.FilterFields
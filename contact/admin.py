from django.contrib import admin
from contact.models import Contact
from contact.models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name','last_name','phone',
    ordering = 'id',
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name'
    list_per_page = 1
    list_max_show_all = 200
    list_editable = 'last_name',
    list_display_links = 'id','first_name'
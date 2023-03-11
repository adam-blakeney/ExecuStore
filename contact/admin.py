from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'second_name',
        'contact_email',
        'subject',
    )


admin.site.register(Contact)
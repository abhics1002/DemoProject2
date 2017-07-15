from django.contrib import admin
from person.models import PhoneNumber, Person
# Register your models here.

class PhoneNumberInline(admin.StackedInline):
    model = PhoneNumber
    extra = 2

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'title')
    inlines = [PhoneNumberInline]

admin.site.register(Person, PersonAdmin)


admin.site.register(PhoneNumber)
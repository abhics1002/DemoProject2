from django.contrib import admin
from person.models import PhoneNumber, Person
# Register your models here.


# Register default PhoneNumber Model with admin.
admin.site.register(PhoneNumber)

# Register Custom Admin Model with admin.

class PhoneNumberInline(admin.StackedInline):
    model = PhoneNumber
    extra = 2

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'title','custom_title')
    inlines = [PhoneNumberInline]
    # actions_on_top = False
    # actions_on_bottom = True

    def custom_title(self, obj):
        return obj.title + " at " + obj.company

admin.site.register(Person, PersonAdmin)
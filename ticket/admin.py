from django.contrib import admin
from .models import CustomUser, Event, Company, Ticket

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name')


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    search_fields = ('email',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    search_fields = ('title',)


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type')
    search_fields = ('title',)


admin.site.register(Company,CompanyAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Ticket,TicketAdmin)

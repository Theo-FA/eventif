from django.contrib import admin
from django.utils.timezone import now
from contact.models import Contact

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_at', 'contacted_now', 'response', 'reply_check', 'reply_created_at')
    search_fields = ('name', 'email', 'phone', 'message', 'created_at')
    list_editable = ['response']
    date_hierarchy = 'created_at'
    
    def contacted_now(self, obj):
        return obj.created_at.date() == now().date()
    
    contacted_now.short_description = 'Enviada hoje'
    contacted_now.boolean = True
    
    def reply_check(self, obj):
        return obj.response != ""
    
    reply_check.short_description = 'Respondida'
    reply_check.boolean = True
   
admin.site.register(Contact, ContactModelAdmin)
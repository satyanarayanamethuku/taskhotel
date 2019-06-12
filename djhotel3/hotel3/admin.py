from django.contrib import admin
from .models import Register,Platinum

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display=['id','Customer_name','Username','Password', 'Membership_type','Booking1_id']


admin.site.register(Register,RegisterAdmin)


class PlatinumAdmin(admin.ModelAdmin):
    list_display=['id','User', 'Check_In', 'Check_Out','Room_number','Booking_id','Room_type']

admin.site.register(Platinum, PlatinumAdmin)



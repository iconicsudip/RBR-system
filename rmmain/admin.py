from django.contrib import admin
from rmmain.models import Customer, Location,Manager,Room,Roomtype, Slotdelay, Timing
# Register your models here.
admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Roomtype)
admin.site.register(Location)
admin.site.register(Room)
admin.site.register(Slotdelay)
admin.site.register(Timing)

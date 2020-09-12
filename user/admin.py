from django.contrib import admin

from .models import Tshirt, TshirtRoom, Friend

# Register your models here.
admin.site.register(Tshirt)
admin.site.register(TshirtRoom)
admin.site.register(Friend)
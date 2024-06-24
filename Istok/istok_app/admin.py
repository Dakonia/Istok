from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(RenovationLocation)
admin.site.register(Order)
admin.site.register(Favorite)
admin.site.register(BonusProgram)

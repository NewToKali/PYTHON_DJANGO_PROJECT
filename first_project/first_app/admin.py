from django.contrib import admin
from first_app.models import *

admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
admin.site.register(Users)
admin.site.register(UserProfileInfo)

# Register your models here.

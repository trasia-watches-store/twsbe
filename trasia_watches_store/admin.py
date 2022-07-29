from django.contrib import admin
from .models import Watch, WatchesPicture, MyModel

# Register your models here.
admin.site.register(Watch)
admin.site.register(WatchesPicture)
admin.site.register(MyModel)
from django.contrib import admin
from Accounts.models import Avatar
from my_app.models import Blog


admin.site.register(Avatar)
admin.site.register(Blog)
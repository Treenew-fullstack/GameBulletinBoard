from django.contrib import admin

from .models import BulletinsCategory, Bulletins, Responses

admin.site.register(BulletinsCategory)
admin.site.register(Bulletins)
admin.site.register(Responses)



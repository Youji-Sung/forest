from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Forest, Review, Community

# Register your models here.


admin.site.register(Forest)
admin.site.register(Review)
admin.site.register(Community)
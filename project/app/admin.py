from django.contrib import admin
from . models import Vendors, Recipes

# Register your models here.

admin.site.register(Vendors)
#class VendorsAdmin(admin.ModelAdmin)
#pass
#admin.site.register(Vendors,VendorsAdmin)

admin.site.register(Recipes)
#@admin.register(Recipes)
#class RecipesAdmin(admin.ModelAdmin)
#pass

#admin.site.register(about)

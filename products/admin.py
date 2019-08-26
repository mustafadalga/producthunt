from django.contrib import admin
from .models import Product
from .models import Votes

class ProductListing(admin.ModelAdmin):
    list_display = ('id','title','hunter')
    list_display_links = ('id','title','hunter')
    search_fields = ('title','hunter')
    list_per_page = 50

class VoteListing(admin.ModelAdmin):
    list_display = ('id','product','user')
    list_display_links = ('id','product','user')
    search_fields = ('product__title','user__username')
    list_per_page = 50


admin.site.register(Product,ProductListing)
admin.site.register(Votes,VoteListing)
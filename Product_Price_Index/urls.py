from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('costco/', include('costco_products.urls')),
    path('admin/', admin.site.urls),
]

admin.site.site_header = "Costco Price Index"
admin.site.site_title = "Costco Price Index Admin Area"
admin.site.index_title = "Welcome to Costco Price Index admin area"

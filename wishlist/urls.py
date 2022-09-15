from wishlist.views import show_xml #sesuaikan dengan nama fungsi yang dibuat
from django.urls import path
from wishlist.views import show_wishlist

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
]

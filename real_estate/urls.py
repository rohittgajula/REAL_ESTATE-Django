
from django.conf import settings                # these are for static files

from django.conf.urls.static import static      # this are for static files

from django.contrib import admin
from django.urls import path

from listings.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list, name="home"),
    path('listings/<pk>/', listing_retrive, name="listings"),
    path('add-listing/', listing_create, name="create"),
    path('update-listing/<pk>/', listing_update, name="update"),
    path('delete-listing/<pk>/', listing_delete, name="delete")
]
                    # this is for static files (images)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT )




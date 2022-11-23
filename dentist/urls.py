from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "AP Smile dental Center Administration"
admin.site.index_title = "AP Smile dental Center"
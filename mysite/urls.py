from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404 , handler500
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('sieunhan.urls')),
   path('blog/', include('blog.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'sieunhan.views.error'
handle500 = 'sieunhan.views.error'
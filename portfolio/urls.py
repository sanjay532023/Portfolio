from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', jobs.views.home, name='home'),
    path('news/', include('news.urls')),
    path('blog/', include('blog.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


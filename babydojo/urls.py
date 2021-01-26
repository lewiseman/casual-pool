from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('educator/', include('educator.urls')),
    path('manager/', include('manager.urls')),
    path('job/', include('job.urls')),
    path('booking/', include('booking.urls')),
    path('leave/', include('leave.urls')),
    path('rostering/', include('rostering.urls')),
    path('attendance/', include('attendance.urls')),
    path('availability/', include('availability.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

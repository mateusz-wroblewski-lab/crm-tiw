from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('secret-panel-admin/', admin.site.urls),
    path('', include('crm.urls')),
    path('management/', include('management.urls')),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
]

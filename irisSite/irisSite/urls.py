from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('submissions/', include('submissions.urls')),
    path('admin/', admin.site.urls),
]
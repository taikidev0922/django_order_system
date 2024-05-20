from django.contrib import admin
from django.urls import path, include
from django.urls import path,include,re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/', include('api.urls')),
    re_path('',RedirectView.as_view(url='/'))
]

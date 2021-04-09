from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url('admin/', admin.site.urls),
    url('api/', include('articles.api.urls'))
]
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('students.urls')),
]

urlpatterns += [re_path(r'^.*',  include("start.urls"))]
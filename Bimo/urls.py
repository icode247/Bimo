
from django.contrib import admin
from django.urls import path,include
from.views import Bimo_Index
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'Bimo/', include('Shop.urls'), name='index')
]

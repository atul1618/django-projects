from django.contrib import admin
from django.urls import path

from operations.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add',addition),
    path('additionresult',addresult,name="aresult"),
    path('sub',subtract),
    path('subtractionresult',subresult,name="sresult"),
    path('mul',multiply),
    path('multiplicationresult',mulresult,name='mresult'),
    path('div',divide),
    path('divisionresult',divresult,name='dresult'),
]
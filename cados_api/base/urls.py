from django.urls import path
from . import views

app_name='base'

urlpatterns=[
    path('',views.endpoins),
    path('advocates/',views.advocate_list,name="advocates"),
    path('advocates/<str:username>/',views.advocate_detail),
] 
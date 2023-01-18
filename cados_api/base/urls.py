from django.urls import path
from . import views

app_name='base'

urlpatterns=[
    path('',views.endpoins),
    path('advocates/',views.advocate_list,name="advocates"),
    # path('advocates/<str:username>/',views.advocate_detail),
    path('advocates/<str:username>/',views.AdvocateDetail.as_view()),
    
    #companies/
    path('companies/',views.companies_list),
    #companies/:id
   
    
] 
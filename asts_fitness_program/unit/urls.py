from django.urls import path
from . import views

app_name = 'unit'

urlpatterns = [
    # post views
    # path('', views.airman_list, name='airman_list'),
    path('', views.AirmanListView.as_view(), name='airman_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:airman>/',
         views.airman_detail,
         name='airman_detail'),
]

from django.urls import path
from .views import index, place_details

app_name = 'places'

urlpatterns = [

    path('', index, name='index'),
    path('places/<int:place_id>/', place_details, name='place_details')

]

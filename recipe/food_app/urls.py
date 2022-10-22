from django.urls import path
from .views  import *

urlpatterns = [
    path('', show_food_list , name = "show"),
    path('<int:id>',show_detail , name = "detail"),
]

from django.urls import path
from novo.views import home_novo, sobre_novo, contato_novo

urlpatterns = [
    path('', home_novo),
    path('sobre/', sobre_novo),
    path('contato/', contato_novo)

]
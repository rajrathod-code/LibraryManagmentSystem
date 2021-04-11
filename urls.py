from django.urls import path
from . import views
urlpatterns = [
    path('' ,views.index,name = 'indexPage'),
    path('api/book/' , views.BookAPI.as_view()), 
    path('api/book/<int:pk>/' , views.BookAPI.as_view())
]

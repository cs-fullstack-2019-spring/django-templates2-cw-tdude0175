from django.urls import path

from . import views

# gets the index of the movie clicked for easier access
urlpatterns = \
    [
        path('',views.index, name= 'index'),
        path('details/<int:indexNum>/',views.detailRender, name= 'detailDisplay'),
        path('synopsis/<int:indexNum>/',views.synopsisRender, name= 'synopsisDisplay'),
    ]
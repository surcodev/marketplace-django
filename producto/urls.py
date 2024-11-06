from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('registrarProducto/', views.registrarProducto, name='registrarProducto'),
    # path('edicionProducto/<int:id>/', views.edicionProducto, name='edicionProducto'),
    # path('eliminarProducto/<int:id>/', views.eliminarProducto, name='eliminarProducto'),
    # path('detalleProducto/<int:id>/', views.detalleProducto, name='detalleProducto'),
]

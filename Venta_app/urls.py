from django.urls import path
from Venta_app import views 

urlpatterns = [
    path("ventas",views.inicio_vistaVentas,name="ventas"),
    path("registrarVentas/",views.registrarVentas,name="registrarVentas"),
    path("seleccionarVenta/<id_venta>",views.seleccionarVenta,name="seleccionarVenta"),
    path("editarVentas/",views.editarVentas,name="editarVentas"),
    path("borrarVenta/<id_venta>",views.borrarVenta,name="borrarVenta"),
]
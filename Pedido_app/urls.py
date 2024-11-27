from django.urls import path
from Pedido_app import views 

urlpatterns = [
    path("pedidos",views.inicio_vistaPedidos,name="pedidos"),
    path("registrarPedidos/",views.registrarPedidos,name="registrarPedidos"),
    path("seleccionarPedidos/<id_pedido>",views.seleccionarPedidos,name="seleccionarPedidos"),
    path("editarPedidos/",views.editarPedidos,name="editarPedidos"),
    path("borrarPedidos/<id_pedido>",views.borrarPedidos,name="borrarPedidos"),
]
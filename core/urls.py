from django.urls import path
from .views import IndexView, CreatePessoaView, UpdatePessoaView, DeletePessoasView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreatePessoaView.as_view(), name='add_pessoa'),
    path('<int:pk>/update/', UpdatePessoaView.as_view(), name='upd_pessoa'),
    path('<int:pk>/delete/', DeletePessoasView.as_view(), name='del_pessoa')
]

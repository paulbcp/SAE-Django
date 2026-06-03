from django.urls import path
from . import views

app_name = 'boutique'

urlpatterns = [

    #Clients
    path('clients/',                  views.client_list,   name='client_list'),
    path('clients/nouveau/',          views.client_create, name='client_create'),
    path('clients/<int:pk>/',         views.client_detail, name='client_detail'),
    path('clients/<int:pk>/modifier/',views.client_update, name='client_update'),
    path('clients/<int:pk>/suppr/',   views.client_delete, name='client_delete'),

    #Commandes
    path('commandes/',                    views.commande_list,   name='commande_list'),
    path('commandes/nouvelle/',           views.commande_create, name='commande_create'),
    path('commandes/<int:pk>/',           views.commande_detail, name='commande_detail'),
    path('commandes/<int:pk>/modifier/',  views.commande_update, name='commande_update'),
    path('commandes/<int:pk>/suppr/',     views.commande_delete, name='commande_delete'),
    path('commandes/<int:pk>/fiche/',     views.commande_fiche,  name='commande_fiche'),
]

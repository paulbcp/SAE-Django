from django.contrib import admin
from .models import Categorie, Produit, Client, Commande, LigneCommande


# ── LigneCommande en inline dans Commande ──
class LigneCommandeInline(admin.TabularInline):
    model = LigneCommande
    extra = 1
    min_num = 1


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    search_fields = ('nom',)


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'marque', 'prix', 'categorie', 'date_peremption')
    list_filter = ('categorie',)
    search_fields = ('nom', 'marque')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'date_inscription')
    search_fields = ('nom', 'prenom')


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date')
    list_filter = ('date',)
    inlines = [LigneCommandeInline]


@admin.register(LigneCommande)
class LigneCommandeAdmin(admin.ModelAdmin):
    list_display = ('commande', 'produit', 'quantite')

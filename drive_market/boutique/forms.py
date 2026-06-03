from django import forms
from django.forms import inlineformset_factory
from .models import Client, Commande, LigneCommande


# ─────────────────────────────────────────────
# Formulaire Client
# ─────────────────────────────────────────────
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'adresse']
        widgets = {
            'nom':     forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Adresse complète'}),
        }
        labels = {
            'nom':     'Nom',
            'prenom':  'Prénom',
            'adresse': 'Adresse',
        }


# ─────────────────────────────────────────────
# Formulaire Commande (en-tête)
# ─────────────────────────────────────────────
class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['client']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'client': 'Client',
        }


# ─────────────────────────────────────────────
# Formulaire LigneCommande (une ligne)
# ─────────────────────────────────────────────
class LigneCommandeForm(forms.ModelForm):
    class Meta:
        model = LigneCommande
        fields = ['produit', 'quantite']
        widgets = {
            'produit':  forms.Select(attrs={'class': 'form-select'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
        labels = {
            'produit':  'Produit',
            'quantite': 'Quantité',
        }


# ─────────────────────────────────────────────
# InlineFormSet : plusieurs LigneCommande
# rattachées à une seule Commande
#
# extra=1  → 1 ligne vide affichée par défaut
# can_delete=True → bouton "supprimer" par ligne
# ─────────────────────────────────────────────
LigneCommandeFormSet = inlineformset_factory(
    parent_model=Commande,
    model=LigneCommande,
    form=LigneCommandeForm,
    extra=1,
    can_delete=True,
    min_num=1,
    validate_min=True,
)
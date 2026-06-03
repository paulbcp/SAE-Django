from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import transaction

from .models import Client, Commande, LigneCommande
from .forms import ClientForm, CommandeForm, LigneCommandeFormSet


# ════════════════════════════════════════════════════
#  CLIENT — CRUD
# ════════════════════════════════════════════════════

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'boutique/client_list.html', {'clients': clients})


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    commandes = client.commandes.prefetch_related('lignes__produit').all()
    return render(request, 'boutique/client_detail.html', {
        'client': client,
        'commandes': commandes,
    })


def client_create(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        client = form.save()
        messages.success(request, f"Client « {client} » créé avec succès.")
        return redirect('boutique:client_list')
    return render(request, 'boutique/client_form.html', {'form': form, 'title': 'Nouveau client'})


def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        messages.success(request, f"Client « {client} » mis à jour.")
        return redirect('boutique:client_list')
    return render(request, 'boutique/client_form.html', {'form': form, 'title': 'Modifier le client'})


def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        messages.warning(request, "Client supprimé.")
        return redirect('boutique:client_list')
    return render(request, 'boutique/confirm_delete.html', {
        'objet': client,
        'cancel_url': 'boutique:client_list',
    })


# ════════════════════════════════════════════════════
#  COMMANDE — CRUD
# ════════════════════════════════════════════════════

def commande_list(request):
    commandes = Commande.objects.select_related('client').prefetch_related('lignes__produit').all()
    return render(request, 'boutique/commande_list.html', {'commandes': commandes})


def commande_detail(request, pk):
    commande = get_object_or_404(
        Commande.objects.select_related('client').prefetch_related('lignes__produit'),
        pk=pk
    )
    return render(request, 'boutique/commande_detail.html', {'commande': commande})


def commande_create(request):
    """
    Crée une commande + ses lignes en une seule page.
    On utilise un InlineFormSet pour gérer la relation M2M via LigneCommande.
    """
    form = CommandeForm(request.POST or None)
    formset = LigneCommandeFormSet(request.POST or None)   # pas d'instance encore

    if request.method == 'POST' and form.is_valid():
        # On doit d'abord sauver la commande pour avoir un PK,
        # puis lier le formset à cette instance.
        with transaction.atomic():
            commande = form.save()
            formset = LigneCommandeFormSet(request.POST, instance=commande)
            if formset.is_valid():
                formset.save()
                messages.success(request, f"Commande #{commande.pk} créée.")
                return redirect('boutique:commande_detail', pk=commande.pk)
            else:
                # rollback implicite grâce à atomic()
                raise Exception("Formset invalide – rollback")

    return render(request, 'boutique/commande_form.html', {
        'form': form,
        'formset': formset,
        'title': 'Nouvelle commande',
    })


def commande_update(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    form = CommandeForm(request.POST or None, instance=commande)
    formset = LigneCommandeFormSet(request.POST or None, instance=commande)

    if request.method == 'POST' and form.is_valid() and formset.is_valid():
        with transaction.atomic():
            form.save()
            formset.save()
        messages.success(request, f"Commande #{commande.pk} mise à jour.")
        return redirect('boutique:commande_detail', pk=commande.pk)

    return render(request, 'boutique/commande_form.html', {
        'form': form,
        'formset': formset,
        'title': f'Modifier commande #{commande.pk}',
    })


def commande_delete(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    if request.method == 'POST':
        commande.delete()
        messages.warning(request, "Commande supprimée.")
        return redirect('boutique:commande_list')
    return render(request, 'boutique/confirm_delete.html', {
        'objet': commande,
        'cancel_url': 'boutique:commande_list',
    })


# ════════════════════════════════════════════════════
#  FICHE COMMANDE (impression / PDF)
# ════════════════════════════════════════════════════

def commande_fiche(request, pk):
    commande = get_object_or_404(
        Commande.objects.select_related('client').prefetch_related('lignes__produit'),
        pk=pk
    )
    return render(request, 'boutique/commande_fiche.html', {'commande': commande})


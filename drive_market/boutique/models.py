from django.db import models


# ─────────────────────────────────────────────
# Catégorie de produit
# ─────────────────────────────────────────────
class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.TextField(blank=True)

    class Meta:
        verbose_name = "Catégorie"

    def __str__(self):
        return self.nom


# ─────────────────────────────────────────────
# Produit
# ─────────────────────────────────────────────
class Produit(models.Model):
    nom = models.CharField(max_length=200)
    marque = models.CharField(max_length=100, blank=True)
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    date_peremption = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='produits/', null=True, blank=True)
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.SET_NULL,
        null=True,
        related_name='produits'
    )

    def __str__(self):
        return f"{self.nom} ({self.marque})"


# ─────────────────────────────────────────────
# Client
# ─────────────────────────────────────────────
class Client(models.Model):
    # numéro_client = PK auto Django (id)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_inscription = models.DateField(auto_now_add=True)
    adresse = models.TextField()

    class Meta:
        ordering = ['nom', 'prenom']

    def __str__(self):
        return f"{self.prenom} {self.nom}"


# ─────────────────────────────────────────────
# Commande
# ─────────────────────────────────────────────
class Commande(models.Model):
    # numéro_commande = PK auto Django (id)
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='commandes'
    )
    date = models.DateField(auto_now_add=True)

    # Relation M2M déclarée ici (lecture pratique),
    # mais gérée VIA la table LigneCommande
    produits = models.ManyToManyField(
        Produit,
        through='LigneCommande',
        related_name='commandes'
    )

    class Meta:
        ordering = ['-date']

    def total(self):
        """Calcule le coût total de la commande."""
        return sum(
            ligne.produit.prix * ligne.quantite
            for ligne in self.lignes.all()
        )

    def __str__(self):
        return f"Commande #{self.pk} – {self.client} – {self.date}"


# ─────────────────────────────────────────────
# LigneCommande  ← table intermédiaire M2M
# ─────────────────────────────────────────────
class LigneCommande(models.Model):
    commande = models.ForeignKey(
        Commande,
        on_delete=models.CASCADE,
        related_name='lignes'
    )
    produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE,
        related_name='lignes'
    )
    quantite = models.PositiveIntegerField(default=1)

    class Meta:
        # Empêche d'avoir deux fois le même produit dans une commande
        unique_together = ('commande', 'produit')

    def sous_total(self):
        return self.produit.prix * self.quantite

    def __str__(self):
        return f"{self.quantite}x {self.produit} → {self.commande}"


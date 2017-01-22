from django.db import models

# Create your models here.
class Profile(models.Model):
    nom_utilisateur = models.CharField(max_length=40)
    nom= models.CharField(max_length=25)
    prenom= models.CharField(max_length=25)
    adresse_email= models.CharField(max_length=25)
    data_de_naissance=models.DateTimeField('date de naissance')
    numero_telephone_fixe=models.CharField(max_length=10)
    numero_telephone_mobile=models.CharField(max_length= 10)
    #adresse=models.CharField(max_length= 50)
    #ville=models.CharField(max_length= 40)
    #code_postal=models.CharField(max_length= 5)
    #site_internet=models.CharField(max_length= 50)
    #votre_description=models.CharField(max_length= 500)
    #lien_linkedin=models.CharField(max_length= 40)
    
    #lien_facebook=models.CharField(max_length= 40)
    #lien_twitter=models.CharField(max_length= 40)
    #centre_interet=models.CharField(max_length= 50)
    
    def __str__(self):
        return  self.adresse_email
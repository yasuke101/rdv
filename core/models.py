from django.db import models

#def user_directory_path(instance, filename):
#	return '{0}/{1}'.format(instance.CIN, filename)

class res(models.Model):
	sexe=[('',''),('Homme','Homme'),('Femme','Femme')]
	CIN=models.CharField(max_length=7)
	#image_de_CIN=models.ImageField(upload_to=user_directory_path)
	nom=models.CharField(max_length=200)
	sexe=models.CharField(choices=sexe,max_length=5)
	prenom=models.CharField(max_length=200)
	telephone=models.CharField(max_length=10)
	date_de_RDV=models.DateTimeField()
	date_de_creation=models.DateTimeField(auto_now=True,editable=False)
	class Meta:
		verbose_name = 'Réservation'
		verbose_name_plural = "Réservations"
		ordering = ['-date_de_RDV']
	
		
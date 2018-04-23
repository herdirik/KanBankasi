from django.db import models
from django.contrib.auth.models import User


class Il(models.Model):
	il_adi = models.CharField(max_length = 30)

	def __str__(self):
		return self.il_adi

class Ilce(models.Model):
	ilce_adi = models.CharField(max_length = 30)
	il_id = models.ForeignKey(Il, on_delete= models.PROTECT)

	def __str__(self):
		return self.ilce_adi

class Hastane(models.Model):
	hastane_adi = models.CharField(max_length = 100)
	ilce_id = models.ForeignKey(Ilce, on_delete = models.PROTECT)

	def __str__(self):
		return self.hastane_adi

class Rol(models.Model):
	rol_adi = models.CharField(max_length = 20)

class KanGrubu(models.Model):
	KanGrubu_adi = models.CharField(max_length = 20)

	def __str__(self):
		return self.KanGrubu_adi

class Kullanici(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	ad = models.CharField(max_length = 20)
	soyad = models.CharField(max_length = 20)
	dogum_tarihi = models.DateField(null=True, blank=True)
	BOOL_CHOICES = ((True, 'Erkek'), (False, 'Kadın'))
	cinsiyet = models.NullBooleanField(choices=BOOL_CHOICES, blank=True, null=True)
	telefon = models.CharField(max_length=11)
	il_id = models.ForeignKey(Il, on_delete= models.PROTECT)
	ilce_id = models.ForeignKey(Ilce, on_delete = models.PROTECT)
	kanGrubu_id = models.ForeignKey(KanGrubu, on_delete = models.PROTECT)
	rol_id = models.ForeignKey(Rol, on_delete = models.PROTECT)

class Stok(models.Model):
	stokMiktari = models.IntegerField(default = 0)
	hastane_id = models.ForeignKey(Hastane, on_delete = models.PROTECT)
	kanGrubu_id = models.ForeignKey(KanGrubu, on_delete = models.PROTECT)


from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profil(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profil")
    bio=models.CharField(max_length=123,blank=True,null=True)
    sehir=models.CharField(max_length=46,blank=True,null=True)
    foto=models.ImageField(null=True,blank=True,upload_to='fotolar/%Y/%m/') # yıl ve ay olacak şekilde dosyalar oluşturur

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username

class ProfileDurum(models.Model):
    user_profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    durum_mesaji=models.CharField(max_length=333)
    yaratilma_zamani=models.DateTimeField(auto_now_add=True)
    guncelleme_zamani=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_profil.user.username
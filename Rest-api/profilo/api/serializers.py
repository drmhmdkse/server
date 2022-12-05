from profilo.models import Profil ,ProfileDurum
from rest_framework import serializers

class ProfilSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True) # strRelated bize bir modelin str fonksiyonunu dönderiri
    foto=serializers.ImageField(read_only=True)
    username=serializers.ReadOnlyField(source="get_username")
    class Meta:
        model=Profil
        fields="__all__"



class ProfilePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Profil
        fields="foto",

class ProfileDurumSerializer(serializers.ModelSerializer):
    user_profil=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=ProfileDurum
        fields="__all__"



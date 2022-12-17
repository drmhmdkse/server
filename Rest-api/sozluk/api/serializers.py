from rest_framework import serializers
from sozluk.models import Word,Comment


class CommentSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True) # amaç userin aydisini değilde modelde __str__ ile dönen değeri çekmek
    class Meta:
        model=Comment
        fields="__all__"


class WordSerializer(serializers.ModelSerializer):
    wordComment = CommentSerializer(read_only=True,many=True) # burada wordCommenti modelde related name ile kullandığımız ad ile çektik
    class Meta:
        model=Word
        exclude= ["id"]
        #fields='__all__'

    def validate_name(self,value): # validated_<sütun> bununla sadece bir sutun validate edilir
        for i in value.lower():
            if i in {"ı","ö","ü","ç"}:
                raise serializers.ValidationError("please enter english char")
        return value





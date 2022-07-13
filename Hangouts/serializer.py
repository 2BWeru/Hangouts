from django.forms import PasswordInput
from rest_framework import serializers
from .models import *
# from .models import Profile
from rest_framework.validators import UniqueValidator
from dataclasses import fields

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # model = User
        fields = ['id','name', 'email','password']
        extra_kwargs = {
            'password':{'write_only':True,'required':True}
            }

    def create(self, validated_data):

        password= validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['fname','bio','idNo','user','instagram_acc','facebook_acc','avatar']
        owner = serializers.ReadOnlyField(source='user.username')

    def create(self,args):
        profile=Profile.objects.create()
        return profile


class ProfileListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['fname','bio','idNo','user','instagram_acc','facebook_acc','avatar']
        owner = serializers.ReadOnlyField(source='user.username')



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = '__all__'

class PostEventSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),many=False)

    class Meta:
        model = Event
        fields ='__all__'


class MainEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        




     

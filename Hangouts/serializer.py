from django.forms import PasswordInput
from django.http import HttpResponse
from rest_framework import serializers
# from .models import User
from django.contrib.auth.models import User

from .models import Category, Category1, Posts, Profile,Site,Event

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email','password']
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
        


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['fname','bio','id','instagram_acc','facebook_acc']
        owner = serializers.ReadOnlyField(source='user.username')

    def profile(self, request,args,kwargs,serializer):
        avatar = request.data['avatar'],
        fname= request.data['fname'],
        instagram_acc = request.data['instagram_acc'],
        facebook_acc = request.data['facebook_acc'],
        bio = request.data['bio'],
        Profile.objects.create(
            avatar = avatar,fname = fname,instagram_acc = instagram_acc,
            facebook_acc = facebook_acc,bio = bio
           )

        serializer.save(user=self.request.user)
    # def create(self,args):
    #     profile=Profile.objects.create(pk=args)

    #     profile.save()
        return HttpResponse()


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['fname','bio','id','user','instagram_acc','facebook_acc','user_id']
        owner = serializers.ReadOnlyField(source='user.username')

     

class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id','title','photo','text','Location','url','category1']

class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'about', 'Location', 'time', 'due_date', 'photo', 'date', 'county']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['image','date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category1
        fields = ['type']

class PostlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['image','date']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['user','created','site','reviews']


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
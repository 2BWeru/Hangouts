from unicodedata import category
from rest_framework.views import APIView
from .serializer import  CategorySerializer, EventSerializer, MainEventSerializer, PostEventSerializer, PostSerializer, PostlistSerializer, ProfileListSerializer,EventSerializers, ReviewSerializer, SitesSerializer, UserSerializer,ProfileSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from .models import Category, Posts, Profile, Review, Site,User,Event
import jwt,datetime
from rest_framework import filters
from rest_framework import permissions, mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import generics

from rest_framework.decorators import action, permission_classes as permission_decorator





class RegisterView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()



        return Response(serializer.data)

class LoginView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        
        user=User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not Found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')

        payload = {
            'id' : user.id,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf_8')
        
        response=Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt':token
           
        }
        return response

class UserView(APIView):
    def get(self,request):
        token=request.COOKIES.get('jwt')

        if not token:
           raise AuthenticationFailed('Not Authenticated')

        try:
            payload=jwt.decode(token, 'secret', algorithm=['HS256'])

        except:
            raise AuthenticationFailed('Unauthenticated')

        user=User.objects.filter(id=payload['id']).first()
        serializer=UserSerializer(user)


        return Response(serializer.data)

class ProfileView(APIView):

    def post(self,request):
        serializer = Profile.objects.all()
        serializer=ProfileSerializer(data=request.data,context={'request': None})
        serializer.is_valid(raise_exception=True)
        
        serializer.save()

       
        
        return Response (serializer.data)


class ReviewView(APIView):

    def post(self,request):
        serializer = Review.objects.all()
        serializer=ReviewSerializer(data=request.data,context={'request': None})
        serializer.is_valid(raise_exception=True)
        
        serializer.save()

       
        
        return Response (serializer.data)        

class ProfileListView(APIView):

    def get(self, request, format=None):
        profile = Profile.objects.all()
        serializers = ProfileListSerializer(profile, many=True,context={'request': None})
        return Response(serializers.data)

    
class SitesView(APIView):
 
    
    def get(self, request, format=None):
        sites = Site.objects.all()
        serializers = SitesSerializer(sites, many=True)
  

        return Response(serializers.data)



class SiteListViewSet(generics.ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SitesSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['category1','id',]




class PostView(APIView):

    # def get(self, request, format=None):
    #     post = Posts.objects.all()
    #     serializers = ProfileListSerializer(post, many=True,context={'request': None})
    #     return Response(serializers.data) 

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

class CategoryView(APIView):

    def get(self, request, format=None):
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True,context={'request': None})
        return Response(serializers.data)
      
class PostListView(APIView):

    def get(self, request, format=None):
        category = Posts.objects.all()
        serializers = PostlistSerializer(category, many=True,context={'request': None})
        return Response(serializers.data)
 


class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')

        response.data = {
            "message":"Success"
        }
        return response





class all_events(APIView):
    # permission_classes = (IsAuthenticated, )

    def get(self, request):
        if request.method == "GET":
            if  request.GET['category']:
                category = request.GET['category']
                print(category)
                events = Event.objects.filter(category__id=int(category))
                # print(events)
            # else:
            #     events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data)


class all_categories(APIView):
    # permission_classes = (IsAuthenticated, )

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class create_event(APIView):
    # permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = PostEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



class main_event(APIView):
    def get(self, request):
        main_event = Event.objects.all()
        serializer = MainEventSerializer(main_event, many=True)
        return Response(serializer.data)














# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow owners of an object to edit it.
#     """

#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         # Write permissions are only allowed to the owner of the snippet.
#         return obj.user == request.user

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     authentication_classes=[TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# # f0a9f7ef3f93e50c15b6b2429e349cfb07dd6710

# class ProfileViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


#     def profile(self, request,args,kwargs,serializer):
#         avatar = request.data['avatar'],
#         fname= request.data['fname'],
#         instagram_acc = request.data['instagram_acc'],
#         facebook_acc = request.data['facebook_acc'],
#         bio = request.data['bio'],
#         Profile.objects.create(
#             avatar = avatar,fname = fname,instagram_acc = instagram_acc,
#             facebook_acc = facebook_acc,bio = bio
#            )

#         serializer.save(user=self.request.user)

#         return HttpResponse({'message':'Profile Created'},status=200)






# def search(request):
#         if "event" in request.GET and request.GET["event"]:
#             searched_item=request.GET["event"]
#             event= Event.search_by_title(searched_item)
#             message = f"{searched_item}"


#             return render(request, 'search.html',{"message":message,"event":event})
#         else:
#             message = "Kindly input a search term to get any results"
#             return render(request,'search.html',{})


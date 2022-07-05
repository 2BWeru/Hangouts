from django.urls import include,path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import RegisterView,LoginView,UserView,LogoutView


router = routers.DefaultRouter(trailing_slash=False)
# router.register('profile', views.ProfileViewSet, basename='profile')
# router.register('profiles', views.ProfileList, basename='profile')  


urlpatterns = [
    
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('user/',UserView.as_view()),
    path('logout',LogoutView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
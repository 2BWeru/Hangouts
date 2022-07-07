from django.urls import include,path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import ProfileListView,EventViewset,RegisterView,SitesView,LoginView,UserView,LogoutView,ProfileView


router = routers.DefaultRouter(trailing_slash=False)
# router.register('profile', views.ProfileViewSet, basename='profile')
# router.register('profilelist', views.ProfileList, basename='profilelist')  

events = EventViewset.as_view({'get': 'view_event'})
view_event = EventViewset.as_view({'get': 'view_event'})

urlpatterns = [
    
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('user/',UserView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('profile/',ProfileView.as_view()),
    path('profilelist/',views.ProfileListView.as_view()),
    path('sites/',SitesView.as_view()),

    path('view_event/<pk>/', view_event, name='view_event'),
    path('events/', views.EventList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
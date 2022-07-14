from django.urls import include,path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import CategoryView, PostListView,PostView,RegisterView, ReviewView, SiteListViewSet,SitesView,LoginView,UserView,LogoutView,ProfileView


router = routers.DefaultRouter(trailing_slash=False)
# router.register('profile', views.ProfileViewSet, basename='profile')
# router.register('profilelist', views.ProfileList, basename='profilelist')  


urlpatterns = [
    
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('user/',UserView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('profile/',ProfileView.as_view()),
    path('review/',ReviewView.as_view()),
    path('profilelist/',views.ProfileListView.as_view()),
    path('sites/',SitesView.as_view()),
    path('posts/',PostView.as_view()),
    path('postlist/',PostListView.as_view()),
    path('sitelist/',SiteListViewSet.as_view()),


    path('all_events/',views.all_events.as_view(),name='events'),
    path('create_event/',views.create_event.as_view(),name='createevent'),
    path('all_categories/',views.all_categories.as_view(),name='allcategories'),
    path('main_event/',views.main_event.as_view(),name='main_event'),
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
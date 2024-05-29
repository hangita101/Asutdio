from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user.as_view(),name='login'),
    path('logout/', views.logout_user,name='logout'),
    path('register',views.register_user.as_view(),name='register'),
    
]

from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user.as_view(),name='login'),
    path('logout/', views.logout_user,name='logout'),
    path('register',views.register_user.as_view(),name='register'),
    path('product/<int:pk>',views.product,name='product'),
    path('category/<str:foo>',views.category,name='category'),
    path('anime/<str:foo>',views.anime_based,name='anime'),
    
    
    path('user/',views.UserPage.as_view(),name='userpage'),
    path('search/', views.search.as_view(), name='search'),

    
    
]

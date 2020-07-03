from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user/', views.userPage, name="user-page"),

    path('register/', views.register, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutPage, name="logout"),


    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), 
        name="password_reset_complete"),

    path('create_commande/', views.create_commande, name='create_commande'),
    path('commande/', views.commandes_list, name='commandes'),
    path('delete_commande/<str:pk>/', views.delete_commande, name='delete_commande'),
    path('update_commande/<str:pk>/', views.update_commande, name='update_commande'),

    path('create_hopitaux/', views.create_hopitaux, name='create_hopitaux'),
    path('liste_hopitaux/', views.hopitaux_list, name='liste_hopitaux'),
    path('update_hopitaux/<str:pk>/', views.update_hopitaux, name='update_hopitaux'),
    path('delete_hopitaux/<str:pk>/', views.delete_hopitaux, name='delete_hopitaux'),

    path('liste_donateur/' , views.donateurs_list, name='liste_donateur'),
    path('create_donateur/', views.create_donateur, name='creer_donateur'),
    path('update_donateur/<str:pk>/', views.update_donateur, name='update_donateur'),
    path('delete_donateur/<str:pk>/', views.delete_donateur, name='delete_donateur'),
    
    path('detail_stock/', views.stock_detail, name='stock'),
    path('creer_stock/', views.create_stock, name='creer_stock'),
    path('update_stock/<str:pk>/', views.update_stock, name='update_stock'),
    path('delete_stock/<str:pk>/', views.delete_stock, name='delete_stock'),
]
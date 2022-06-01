from django.urls import path
from product import views

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('<int:pk>/', views.ProductDetail.as_view()),
    # path('login/', views.LoginAPI.as_view()),
    # path('logout/', views.LogoutAPI.as_view()),
    # path('SignIn/', views.SignInAPI.as_view())
]


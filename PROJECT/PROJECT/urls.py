"""PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from authentication import views as v
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('view/', views.adddata, name='home'),
    path('delete/<int:id>/', views.deletedata ,name='deleted'),
    path('<int:id>', views.updatew ,name='updwin'),
    
    path('stu/',views.api),
    
    path('gettoken/',TokenObtainPairView.as_view(),name='gettoken'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refreshtoken'),
    path('verifytoken/',TokenVerifyView.as_view(),name='tokenverify'),
   
    path('otp/',v.otpverify,name='otp'),
    path('signup/',v.signup,name='signup'),
    path('signin/',v.signin,name='signin'),
    path('',v.option,name='option'),
    path('logout/',v.logoutpage,name='logout'),
]

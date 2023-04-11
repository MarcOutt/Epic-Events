from customer.views import CustomerViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user.views import UserViewSet, LoginView

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'customers', CustomerViewSet, basename='customers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('', include(router.urls))
]

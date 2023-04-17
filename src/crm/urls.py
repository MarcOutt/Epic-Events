from contract.views import ContractViewSet
from customer.views import CustomerViewSet
from django.contrib import admin
from django.urls import path, include
from event.views import EventViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.views import UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'customers/(?P<customer_id>[^/.]+)/contracts', ContractViewSet, basename='contract')
router.register(r'customers/(?P<customer_id>[^/.]+)/contracts/(?P<contract_id>[^/.]+)/events', EventViewSet,
                basename='event')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='refresh_token'),

    path('', include(router.urls))
]

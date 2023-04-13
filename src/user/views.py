from crm.permissions import IsManagement
from django.contrib.auth import authenticate, login
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import CustomUser
from user.serializers import UserSerializer


class LoginView(APIView):
    """Endpoint API for user login"""
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Email ou mot de passe invalide'}, status=400)


class UserViewSet(viewsets.ModelViewSet):
    """Endpoint Api for user management(CRUD)"""
    permission_classes = [IsManagement]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


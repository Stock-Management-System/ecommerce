from rest_framework import generics, status
from user.api.serializers import RegisterSerializer, FirmRegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from ..models import UserInfo, Firm

class RegisterView(generics.CreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        token = Token.objects.get(user=user)
        data["token"] = token.key
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

class FirmRegisterView(generics.CreateAPIView):
    queryset = Firm.objects.all()
    serializer_class = FirmRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        token = Token.objects.get(user=user)
        data["token"] = token.key
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
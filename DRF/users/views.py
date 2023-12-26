from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializer import SignUpSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token #ssssssssssssssssssssssssssssss


class Signup(APIView):
    def post(self, request, *args, **kwargs):
        data1 = request.POST
        data2 = request.data
        print(data1)
        print(data2)
        
        data_serializer = SignUpSerializer(data=data1)
        if data_serializer.is_valid():
            data_serializer.save()
            return Response(data_serializer.data, status=200)
        return Response(data_serializer.errors, status=402)

class Login(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        data_ser = LoginSerializer(data=data)
        # serializer = self.serializer_class(data=request.data,
        #                                    context={'request': request})
        # serializer.is_valid(raise_exception=True)
        # user = serializer.validated_data['user']
        # token, created = Token.objects.get_or_create(user=user)
        # return Response({
        #     'token': token.key,
        #     'user_id': user.pk,
        #     'email': user.email
        # })
    
    
class Logout(APIView): ...

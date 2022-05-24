from django.contrib.auth import authenticate, logout
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import Product, CustomUser
from product.serializers import ProductSerializer, CustomUserSerializer
from Base.utils import get_jwt_auth_token
from django.utils import timezone

# Create your views here.


class ProductList(APIView):

    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class LoginAPI(APIView):

    def post(self, request):
        user = authenticate(
            request,
            username=request.data['email'].lower(),
            password=request.data['password']
        )
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        CustomUser.objects.filter(id=user.id).update(last_login=timezone.now())
        user_data = CustomUserSerializer(user, context={'request': request}).data
        return Response(status=status.HTTP_200_OK, data={'data': user_data,
                                                         'token': get_jwt_auth_token(user)})


class LogoutAPI(APIView):

    def user_logout(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class SignInAPI(APIView):

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
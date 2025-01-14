from django.shortcuts import render
from .serializer import UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from patient.models import Patient
from doctor.models import Doctor
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from cart.models import Cart
from wish_list.models import WishList
from django.contrib.auth import login,logout
from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            user_role = serializer.validated_data["user_role"]
            if user_role=="patient":
                try:
                    existing_patient = Patient.objects.get(phone=phone)
                    login(request=request,user=existing_patient.user)
                    token,_ = Token.objects.get_or_create(user=existing_patient.user)
                    return Response({
                        "message":"Login successfull as a patient.",
                        "token":token.key
                    },status=status.HTTP_200_OK)
                except Patient.DoesNotExist:
                    new_user = User.objects.create_user(username=f"patient_{phone}")
                    new_patient = Patient.objects.create(user=new_user,phone=phone)
                    new_cart = Cart.objects.create()
                    new_wish_list = WishList.objects.create()
                    new_patient.cart = new_cart
                    new_patient.wish_list = new_wish_list
                    new_patient.save()
                    login(request=request,user=new_user)
                    token,_ = Token.objects.get_or_create(user=new_user)
                    return Response({
                        "message":"Login successfull as a patient.",
                        "token":token.key
                    },status=status.HTTP_200_OK)
            elif user_role=="doctor":
                try:
                    existing_doctor = Doctor.objects.get(phone=phone)
                    login(request=request,user=existing_doctor.user)
                    token,_ = Token.objects.get_or_create(user=existing_doctor.user)
                    return Response({
                        "message":"Login successfull as a doctor.",
                        "token":token.key
                    },status=status.HTTP_200_OK)
                except Doctor.DoesNotExist:
                    new_user = User.objects.create_user(username=f"doctor_{phone}")
                    new_doctor = Doctor.objects.create(user=new_user,phone=phone)
                    token,_ = Token.objects.get_or_create(user=new_user)
                    login(request=request,user=new_user)
                    return Response({
                        "message":"Login successfull as a doctor.",
                        "token":token.key
                    },status=status.HTTP_200_OK)
            else:
                return Response("Please select a valid role!")
                    

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

     
class UserLogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
       user = request.user
       if isinstance(user,AnonymousUser):
           return Response({"error":"User is not logged in!"},status=status.HTTP_400_BAD_REQUEST)
       if hasattr(request.user,'auth_token'):
           request.user.auth_token.delete()
           logout(request)
           return Response({"success":"Logout successfull"},status=status.HTTP_200_OK)
        



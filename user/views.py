from django.shortcuts import render
from .serializer import UserLoginSerializer
from rest_framework.views import APIView
# Create your views here.

class UserLoginSerializerAPIView(APIView):
    serializer_class = UserLoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            




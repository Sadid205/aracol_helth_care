from django.shortcuts import render
from .serializer import BannerModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Banner
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class BannerModelView(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerModelSerializer
    lookup_field = "pk"
    def create(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            page = serializer.validated_data['page']
            image = serializer.validated_data['image']
            if page !="doctor" and page!="home":
                return Response({"error":"Please select a valid page."})
            Banner.objects.create(title=title,page=page,image=image)
            return Response({"success":"Successfully created a banner."})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def list(self,request,*args,**kwargs):
        page = request.query_params.get("page")
        if page!="doctor" and page!="home":
            return Response({"error":"Please select valid a page!"})
        banner_list = Banner.objects.filter(page=page)
        banner_serializer = BannerModelSerializer(banner_list,many=True)
        return Response({"success":banner_serializer.data},status=status.HTTP_200_OK)
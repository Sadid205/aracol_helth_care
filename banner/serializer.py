from rest_framework.serializers import ModelSerializer
from .models import Banner
class BannerModelSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
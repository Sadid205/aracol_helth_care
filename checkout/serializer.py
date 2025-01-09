from rest_framework.serializers import ModelSerializer
from .models import Checkout

class CheckoutModelSerializer(ModelSerializer):
    class Meta:
        model = Checkout
        fields = "__all__"

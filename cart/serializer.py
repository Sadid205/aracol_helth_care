from rest_framework.serializers import ModelSerializer
from .models import Cart
from rest_framework.serializers import PrimaryKeyRelatedField
from medicine.models import Medicine
from medicine.serializer import MedicineSerializer

class CartModelSerializer(ModelSerializer):
    medicine = PrimaryKeyRelatedField(
        many=True,
        queryset=Medicine.objects.all(),
        write_only=True
    )
    medicine_data = MedicineSerializer(source="medicine",many=True,read_only=True)
    class Meta:
        model = Cart
        fields = ["id","medicine","medicine_data"]
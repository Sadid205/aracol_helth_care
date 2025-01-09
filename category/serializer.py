from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import PrimaryKeyRelatedField
from .models import Category
from medicine.serializer import MedicineSerializer
from medicine.models import Medicine


class CategoryModelSerializer(ModelSerializer):
    medicine = PrimaryKeyRelatedField(
        many=True,
        queryset = Medicine.objects.all(),
        write_only=True
    )
    medicine_data = MedicineSerializer(source='medicine',many=True,read_only=True)
    class Meta:
        model = Category
        fields = ['id','name','image','medicine','medicine_data']
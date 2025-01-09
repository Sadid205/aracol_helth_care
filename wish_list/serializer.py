from rest_framework.serializers import ModelSerializer
from .models import WishList
from medicine.serializer import MedicineSerializer
from rest_framework.serializers import PrimaryKeyRelatedField
from .models import WishList
from medicine.models import Medicine

class WishListModelSerializer(ModelSerializer):
    medicine = PrimaryKeyRelatedField(
        many=True,
        queryset=Medicine.objects.all(),
        write_only=True
    )
    medicine_data = MedicineSerializer(source="medicine",many=True,read_only=True)
    class Meta:
        model = WishList
        fields = ['id','medicine','medicine_data']

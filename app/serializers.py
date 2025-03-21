from rest_framework import serializers
from .models import Client, House,Receipt

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)  # Show client details in response
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), write_only=True, source='client'
    )  # Allow assigning a client by ID

    class Meta:
        model = House
        fields = ['id', 'house_number', 'due_date', 'rent_amount', 'client', 'client_id']


class ReceiptSerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()

    def get_total_amount(self, obj):
        return obj.total_amount()

    class Meta:
        model = Receipt
        fields = '__all__'

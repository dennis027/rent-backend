from rest_framework import serializers
from .models import Client, House,Receipt,SystemVariable

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    # client = ClientSerializer(read_only=True)  # Show client details in response
    # client_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Client.objects.all(), write_only=True, source='client'
    # )  # Allow assigning a client by ID

    class Meta:
        model = House
        fields = ['id', 'house_number', 'due_date', 'rent_amount','last_reading']


class ReceiptSerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()

    def get_total_amount(self, obj):
        return obj.total_amount()

    class Meta:
        model = Receipt
        fields = '__all__'


class SystemVariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemVariable
        fields = ['unit_cost', 'base_value']  # Exclude ID
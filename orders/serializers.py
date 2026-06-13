from rest_framework import serializers
from .models import Order, Cancellation


class OrderSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project.name', read_only=True)
    current_value = serializers.DecimalField(max_digits=20, decimal_places=0, read_only=True)
    profit = serializers.DecimalField(max_digits=20, decimal_places=0, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'project', 'project_name', 'area', 'price_per_meter',
                  'total_price', 'status', 'current_value', 'profit', 'created_at')
        read_only_fields = ('price_per_meter', 'total_price', 'status')


class CancellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancellation
        fields = ('id', 'order', 'cancel_price_per_meter', 'total_refund', 'penalty', 'created_at')
        read_only_fields = ('cancel_price_per_meter', 'total_refund', 'penalty')
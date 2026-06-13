from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'transaction_type', 'amount', 'description', 'created_at')
        read_only_fields = ('transaction_type', 'amount')
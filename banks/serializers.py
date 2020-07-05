from rest_framework import serializers
from .models import bank,branches

class bankSerializer(serializers.ModelSerializer):
    class Meta:
        model = bank
        fields = ['id','name']
        read_only_fields = ('name')


class branchesSerializer(serializers.ModelSerializer):
    bank_name = serializers.SerializerMethodField('get_artists_name')

    def get_artists_name(self, obj):
        return obj.bank_id.name
    
    
    class Meta:
        model = branches
        fields = ['ifsc','branch','address','city','district','state','bank_name']
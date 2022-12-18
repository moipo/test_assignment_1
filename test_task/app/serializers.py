from .models import Program, Category
from rest_framework import serializers

class ProgramSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Program
        fields = [
        "name",
        "actions_detail",
        "image",
        "category",
        "gotolink",
        "products_xml_link",
        ]

class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = '__all__'

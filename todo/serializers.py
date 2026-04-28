from rest_framework import serializers
from .models import Todo




class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user_id', 'title', 'description', 'date_time', 'is_completed', 'created_at']


class TodoCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'date_time', 'is_completed']
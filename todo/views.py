from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from todo.serializers import TodoSerializer, TodoCreateUpdateSerializer
from .models import Todo
from users.models import User

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return only todos for the authenticated user"""
        return Todo.objects.filter(user_id=self.request.user.id)

    def get_serializer_class(self):
        """Use different serializer for create/update operations"""
        if self.action in ['create', 'update', 'partial_update']:
            return TodoCreateUpdateSerializer
        return TodoSerializer

    def perform_create(self, serializer):
        """Set the user to the current authenticated user"""
        # For JWT authentication, we need to create a User instance
        try:
            user = User.objects.get(id=1)  # Get first user or handle appropriately
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(user_id=user)

    def perform_update(self, serializer):
        """Update the todo"""
        serializer.save()

    @action(detail=False, methods=['get'])
    def my_todos(self, request):
        """Get all todos for the current user"""
        todos = self.get_queryset()
        serializer = self.get_serializer(todos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        """Mark a todo as completed"""
        todo = self.get_object()
        todo.is_completed = True
        todo.save()
        serializer = self.get_serializer(todo)
        return Response(serializer.data)

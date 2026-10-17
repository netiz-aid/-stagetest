from rest_framework import viewsets
from .models import Category, Tag, Task
from .serializers import (
    CategorySerializer,
    TagSerializer,
    TaskDetailSerializer,
    TaskShortSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()

  def get_serializer_class(self):
    if self.action == "list":
      return TaskShortSerializer
    return TaskDetailSerializer
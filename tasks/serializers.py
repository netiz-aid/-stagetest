from rest_framework import serializers
from .models import Category, Tag, Task


class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model = Category
    fields = "__all__"


class TagSerializer(serializers.ModelSerializer):

  class Meta:
    model = Tag
    fields = "__all__"


class TaskShortSerializer(serializers.ModelSerializer):

  class Meta:
    model = Task
    fields = ["id", "title", "completed", "created_at", "category"]


class TaskDetailSerializer(serializers.ModelSerializer):
  category = CategorySerializer(read_only=True)
  category_id = serializers.PrimaryKeyRelatedField(
      queryset=Category.objects.all(),
      source="category",
      write_only=True,
      required=False,
      allow_null=True,
  )

  tags = TagSerializer(many=True, read_only=True)
  tag_ids = serializers.PrimaryKeyRelatedField(
      queryset=Tag.objects.all(),
      source="tags",
      write_only=True,
      many=True,
      required=False,
  )

  class Meta:
    model = Task
    fields = [
        "id",
        "title",
        "description",
        "completed",
        "created_at",
        "category",
        "category_id",
        "tags",
        "tag_ids",
    ]
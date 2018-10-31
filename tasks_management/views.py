from rest_framework.generics import \
    (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveAPIView
)
from rest_framework.filters import SearchFilter

from .serializers import *


# Users
class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer

    filter_backends = [SearchFilter]
    search_fields = ['role']

    def get_queryset(self):
        is_with_task = self.request.GET.get('with_task')
        if is_with_task:
            queryset = User.objects.exclude(assigned_tasks__assigned__isnull=True)
        else:
            queryset = User.objects.all()

        return queryset


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Tasks
class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    filter_backends = [SearchFilter]
    search_fields = ['name']


class TaskDetailAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class TaskUpdateAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDeleteAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class AssignedTasksAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            queryset = Task.objects.filter(assigned=user_id)
        else:
            queryset = User.objects.all()

        return queryset

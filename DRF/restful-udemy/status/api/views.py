import json
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
from django.shortcuts import get_object_or_404

from status.models import Status
from .serializers import StatusSerializer


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

#-------------------------------------------------------------------------------
# prosty widok oparty o APIView bez generic
#-------------------------------------------------------------------------------
# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []

#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)

#-------------------------------------------------------------------------------
# widok oparty o generics - każdy ma inny endpoint
#-------------------------------------------------------------------------------
# class StatusAPIView(ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusCreateAPIView(CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer

# class StatusDetailAPIView(RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     # def get_object(self):
#     #     kwargs = self.kwargs
#     #     kw_id = kwargs.get('id')
#     #     return Status.objects.get(id=kw_id)

# class StatusUpdateAPIView(UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusDeleteAPIView(DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

#-------------------------------------------------------------------------------
# widoki oparte o generics z mixin
#-------------------------------------------------------------------------------
# class StatusAPIView(mixins.CreateModelMixin, ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#-------------------------------------------------------------------------------
# One API endpoint CRUDL - generics view + mixins
#-------------------------------------------------------------------------------

# class StatusAPIView(
#     mixins.CreateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     ListAPIView):

#     permission_classes = []
#     authentication_classes = []
#     # queryset = Status.objects.all()
#     serializer_class = StatusSerializer

#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs

#     def get_object(self):
#         request = self.request
#         queryset = self.get_queryset()
#         obj = None
#         if self.passed_id is not None:
#             obj = get_object_or_404(queryset, id=self.passed_id)
#             self.check_object_permissions(request, obj)
#         return obj

#     def get(self, request, *args, **kwargs):
#         request = self.request
#         json_data = {}
#         url_passed_id = request.GET.get('id', None)
#         if is_json(request.body):
#             json_data = json.loads(request.body)
#         new_passed_id = json_data.get('id', None)

#         passed_id = url_passed_id or new_passed_id

#         self.passed_id = passed_id
        
#         if passed_id is not None:
#             return super().retrieve(request, *args, **kwargs )
#         return super().get(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#         if is_json(request.body):
#             json_data = json.loads(request.body)
#         new_passed_id = json_data.get('id', None)

#         passed_id = url_passed_id or new_passed_id

#         self.passed_id = passed_id
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#         if is_json(request.body):
#             json_data = json.loads(request.body)
#         new_passed_id = json_data.get('id', None)

#         passed_id = url_passed_id or new_passed_id

#         self.passed_id = passed_id
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
        # url_passed_id = request.GET.get('id', None)
        # json_data = {}
        # if is_json(request.body):
        #     json_data = json.loads(request.body)
        # new_passed_id = json_data.get('id', None)

        # passed_id = url_passed_id or new_passed_id

        # self.passed_id = passed_id
        # return self.destroy(request, *args, **kwargs)

#-------------------------------------------------------------------------------
# Two API endpoints CRUDL - generics view + mixins
# The best solution
#-------------------------------------------------------------------------------

class StatusAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView
    ):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_update(self, serializer):
    #     serializer.save(updated_by_user=self.request.user)

    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     else:
    #         return None

    
class StatusAPIView(
    mixins.CreateModelMixin,
    generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication]
    serializer_class = StatusSerializer
    # queryset = Status.objects.all()
    
    def get_queryset(self):
        print(self.request.user)
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.core.paginator import Paginator



class ProgramAPIView(APIView):
    def get(self, request, *args, **kwargs):
        paginator = Paginator(Program.objects.all(),10)
        page_num = kwargs.get("page_num")
        try:
            page_obj = paginator.get_page(page_num)
            page_sr = ProgramSerializer(page_obj, many = True)
            return Response({
            "programs" : page_sr.data,
                })
        except:
            return Response("incorrect get request")


class CategoryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is None:
            categories_sr = CategorySerializer(Category.objects.all(), many = True)
            return Response({
            "categories" : categories_sr.data,
            })
        else:
            try:
                ctg = Category.objects.get(id = pk)
                categories_sr = CategorySerializer(ctg)
                return Response({
                "categories" : categories_sr.data,
                })
            except:
                return Response("incorrect get request")


class CategorySecondAPIView(APIView):
    def get(self, request, *args, **kwargs):
        paginator = Paginator(Category.objects.all(),10)
        page_num = kwargs.get("page_num")
        try:
            page_obj = paginator.get_page(page_num)
            page_sr = CategorySerializer(page_obj, many = True)
            return Response({
            "categories" : page_sr.data,
                })
        except:
            return Response("incorrect get request")

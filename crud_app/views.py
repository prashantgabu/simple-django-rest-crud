from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from .models import Crud
from .serializers import CrudSerializer


@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def alllist(request):
    if request.method == 'GET':
        alllist = Crud.objects.all()
        print("Alllist:::", alllist)
        title = request.GET.get('title', None)
        print("TITLE:::", title)
        if title is not None:
            print("INSIDE IF...............")
            alllist = alllist.filter(title__icontains=title)
        alllist_serializer = CrudSerializer(alllist, many=True)
        return JsonResponse(alllist_serializer.data, safe=False)
    elif request.method == 'POST':
        alllist_data = JSONParser().parse(request)
        print(":::::::::::::::", alllist_data)
        alllist_serializer = CrudSerializer(data=alllist_data)
        if alllist_serializer.is_valid():
            alllist_serializer.save()
            return JsonResponse(alllist_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(alllist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Crud.objects.all().delete()
        return JsonResponse({'message': '{} Books were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def details_list(request, pk):
    detail_list = Crud.objects.get(pk=pk)
    if request.method == 'GET':
        crud_serializer = CrudSerializer(detail_list)
        return JsonResponse(crud_serializer.data)
    elif request.method == 'PUT':
        book_data = JSONParser().parse(request)
        crud_serializer = CrudSerializer(detail_list, data=book_data)
        if crud_serializer.is_valid():
            crud_serializer.save()
            return JsonResponse(crud_serializer.data)
        return JsonResponse(crud_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        detail_list.delete()
        return JsonResponse({'message': 'Book was successfully deleted.'}, status=status.HTTP_204_NO_CONTENT)

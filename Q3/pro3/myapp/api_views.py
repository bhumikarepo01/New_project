from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Company
from .serializers import CompanySerializer


@api_view(['GET'])
def company_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def company_create(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def company_detail(request, pk):
    company = get_object_or_404(Company, id=pk)
    serializer = CompanySerializer(company)
    return Response(serializer.data)


@api_view(['PUT'])
def company_update(request, pk):
    company = get_object_or_404(Company, id=pk)
    serializer = CompanySerializer(company, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)
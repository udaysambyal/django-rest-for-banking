from django.shortcuts import render
from rest_framework import viewsets
from .serializers import bankSerializer, branchesSerializer
from .models import bank, branches
from rest_framework import filters, generics
from django.db.models import Q
# Create your views here.

class bankViewset(generics.ListCreateAPIView):
    search_fields = ['^name','name']
    filter_backends = (filters.SearchFilter)
    queryset = bank.objects.all()
    serializer_class = bankSerializer

    # def get_queryset(self):
    #     queryset = self.queryset
    #     #query_set = queryset.filter(user=self.request.user)

    #     print(self.request.GET)
    #     return queryset

class branchesViewset(generics.ListCreateAPIView):
    search_fields = ['ifsc',]
    filter_backends = (filters.SearchFilter,)
    queryset = branches.objects.all()
    serializer_class = branchesSerializer
    def get_queryset(self):
        queryset = branches.objects.all()        
        query_filters=dict(self.request.GET)
       
        if 'name' and 'city' in query_filters:
            queryset=branches.objects.filter(city__contains=query_filters['city'][0],bank_id__name__contains=query_filters['name'][0])
            
            
        elif 'ifsc' in query_filters:
            queryset=branches.objects.filter(Q(ifsc__iexact=query_filters['ifsc'][0])| Q( ifsc__contains=query_filters['ifsc'][0]) )
        else:
            branches.objects.all()
        return queryset

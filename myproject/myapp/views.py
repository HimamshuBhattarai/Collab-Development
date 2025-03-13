from django.shortcuts import render
from rest_framework import viewsets,status
from django.shortcuts import get_object_or_404
from .models import Home
from .serializers import HomeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class HomeViewSet(viewsets.ReadOnlyModelViewSet):  # For Getting data
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class PostItems(APIView):   # For Posting Data
    
    def post(self,request):
        serializer = HomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ({
                "message":"Data saved successfully"
            }, status == status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



    def put(self, request, pk): # For fully updating 
        instance = get_object_or_404(Home, pk=pk)  
        serializer = HomeSerializer(instance, data=request.data, partial=False)  
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def patch(self, request, pk): # For partially updating
        instance = get_object_or_404(Home, pk=pk)  
        serializer = HomeSerializer(instance, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk): # For deleting data
        instance = get_object_or_404(Home, pk=pk)  
        instance.delete()
        return Response({"message": "Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



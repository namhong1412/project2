from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from medicalClinicAPI.models import Bed
from medicalClinicAPI.serializers import BedSerializer


class BedView(APIView):
    serializer_class = BedSerializer

    def get_object(self, pk):
        try:
            return Bed.objects.get(pk=pk)
        except Bed.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        queryset = Bed.objects.all().order_by('-id')
        serialized_data = self.serializer_class(queryset, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        bed = self.get_object(pk)
        if isinstance(bed, Response):
            return bed
        serializer = self.serializer_class(bed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bed = self.get_object(pk)
        if isinstance(bed, Response):
            return bed
        bed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

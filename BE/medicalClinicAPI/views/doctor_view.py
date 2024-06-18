from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from medicalClinicAPI.models import Doctor
from medicalClinicAPI.serializers import DoctorSerializer


class DoctorView(APIView):
    serializer_class = DoctorSerializer

    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        queryset = Doctor.objects.all().order_by('-id')
        serialized_data = self.serializer_class(queryset, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        doctor = self.get_object(pk)
        if isinstance(doctor, Response):
            return doctor
        serializer = self.serializer_class(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        doctor = self.get_object(pk)
        if isinstance(doctor, Response):
            return doctor
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

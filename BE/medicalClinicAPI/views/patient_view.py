from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from medicalClinicAPI.models import Patient
from medicalClinicAPI.serializers import PatientSerializer


class PatientView(APIView):
    serializer_class = PatientSerializer

    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        queryset = Patient.objects.all().order_by('-id')
        serialized_data = self.serializer_class(queryset, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        patient = self.get_object(pk)
        if isinstance(patient, Response):
            return patient
        serializer = self.serializer_class(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        patient = self.get_object(pk)
        if isinstance(patient, Response):
            return patient
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

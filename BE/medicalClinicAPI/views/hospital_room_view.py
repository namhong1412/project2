from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from medicalClinicAPI.models import HospitalRoom
from medicalClinicAPI.serializers import HospitalRoomSerializer


class HospitalRoomView(APIView):
    serializer_class = HospitalRoomSerializer

    def get_object(self, pk):
        try:
            return HospitalRoom.objects.get(pk=pk)
        except HospitalRoom.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        queryset = HospitalRoom.objects.all().order_by('-id')
        serialized_data = self.serializer_class(queryset, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        hospital_room = self.get_object(pk)
        if isinstance(hospital_room, Response):
            return hospital_room
        serializer = self.serializer_class(hospital_room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        hospital_room = self.get_object(pk)
        if isinstance(hospital_room, Response):
            return hospital_room
        hospital_room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from medicalClinicAPI.models import ExaminationRoom
from medicalClinicAPI.serializers import ExaminationRoomSerializer


class ExaminationRoomView(APIView):
    serializer_class = ExaminationRoomSerializer

    def get_object(self, pk):
        try:
            return ExaminationRoom.objects.get(pk=pk)
        except ExaminationRoom.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        queryset = ExaminationRoom.objects.all().order_by('-id')
        serialized_data = self.serializer_class(queryset, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        examination_room = self.get_object(pk)
        if isinstance(examination_room, Response):
            return examination_room
        serializer = self.serializer_class(examination_room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        examination_room = self.get_object(pk)
        if isinstance(examination_room, Response):
            return examination_room
        examination_room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

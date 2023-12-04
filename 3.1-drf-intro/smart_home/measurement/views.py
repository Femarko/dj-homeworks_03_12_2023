# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateSensor, RetrieveUpdateSensor, CreateMeasurement
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

class ListCreateSensor(ListCreateAPIView): # получение датчиков, создание датчика
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class RetrieveUpdateSensor(RetrieveUpdateAPIView): # получение информации по датчику, обновление датчика
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get(self, request, pk): # получение информации по датчику
        serialized_entry = SensorDetailSerializer(Sensor.objects.get(pk=pk))
        return Response(serialized_entry.data)


class CreateMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

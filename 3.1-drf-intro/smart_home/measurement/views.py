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

    def post(self, request):
        entry = Sensor(name=request.data.get('name'), description=request.data.get('description'))
        entry.save()
        serialized_entry = SensorSerializer(entry)
        return Response(serialized_entry.data)

class RetrieveUpdateSensor(RetrieveUpdateAPIView): # получение информации по датчику, обновление датчика
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, pk): # обновление датчика
        entry = Sensor.objects.get(pk=pk)
        entry.name = request.data.get('name')
        entry.description = request.data.get('description')
        entry.save()
        serialized_entry = SensorSerializer(entry)
        return Response(serialized_entry.data)

    def get(self, request, pk): # получение информации по датчику
        serialized_entry = SensorDetailSerializer(Sensor.objects.get(pk=pk))
        return Response(serialized_entry.data)


class CreateMeasurement(CreateAPIView): # добавление измерения: работает при отправке POST-запроса
    # через форму Raw data. В HTML form нет строки для ввода ID датчика - почему так?
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    def post(self, request):
        sensor = request.data.get('sensor')
        entry = Measurement(sensor_id=sensor, temperature=request.data.get('temperature'))
        entry.save()
        serialized_entry = MeasurementSerializer(entry)
        return Response(serialized_entry.data)

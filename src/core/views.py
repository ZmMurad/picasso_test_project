import logging
from django.shortcuts import render
from rest_framework import status,viewsets, generics
from core.models import File
from core.serializers import FileSerializer
from rest_framework.exceptions import ValidationError
from core.tasks import process_file
from django.core.exceptions import SuspiciousFileOperation
# Create your views here.

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    def perform_create(self, serializer):
        try:
            # Получите тип файла здесь и установите его в соответствующее поле
            file_type = detect_file_type(serializer.validated_data['file'])
            instance=serializer.save(file_type=file_type)
            process_file.delay(file_id=instance.id)
        except SuspiciousFileOperation:
            raise ValidationError("Недопустимая операция с файлом")
        except Exception as e:
            logging.error(e)
            raise ValidationError(str(e))

class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


def detect_file_type(file):
    # Реализуйте логику определения типа файла здесь
    # Например, можно проверить расширение файла
    file_name = file.name.lower()
    if file_name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        return 'image'
    elif file_name.endswith(('.txt', '.doc', '.pdf')):
        return 'text'
    else:
        return 'unknown'  # Или что-то еще по умолчанию
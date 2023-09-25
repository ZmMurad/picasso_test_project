import logging
from uploader.celery import app
from .models import File
from celery import shared_task

@shared_task
def process_file(file_id):
    try:
        file = File.objects.get(pk=file_id)
        file.processed = True
        file.save()
    except File.DoesNotExist:
        raise Exception("Файл с указанным ID не существует")
    except Exception as e:
        logging.error(e)
        raise Exception(str(e))

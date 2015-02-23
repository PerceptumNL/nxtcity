from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings
from assetstorage.models import DatabaseStorageWrapper
import os, mimetypes

def asset(request, filename):
    # Read file from database
    storage = DatabaseStorageWrapper()
    image_file = storage.open(
            os.path.join(settings.DBS_OPTIONS['base_url'],filename), 'rb')
    if not image_file:
      raise Http404
    file_content = image_file.read()

    # Prepare response
    content_type, content_encoding = mimetypes.guess_type(filename)
    response = HttpResponse(content=file_content, content_type=content_type)
    response['Content-Disposition'] = 'inline; filename=%s' % filename
    if content_encoding:
      response['Content-Encoding'] = content_encoding
    return response


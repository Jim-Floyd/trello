from time import time_ns
from uuid import uuid4
from os.path import join as join_path
from django.views.decorators.http import require_http_methods

from files.models import UploadUser
from trello2.settings import MEDIA_ROOT

require_DELETE = require_http_methods(["DELETE"])
require_PUT = require_http_methods(["PUT"])
require_PATCH = require_http_methods(["PATCH"])
require_HEAD = require_http_methods(["HEAD"])


def media_path(file_name):
    return f'/media/uploads/{file_name}'


def process_name(code: str, extension: str):
    return f"{code}.{extension}"


def get_extension(file_name: str):
    return file_name.split(".")[-1]


def unique_code():
    return "%s%s" % (time_ns(), str(uuid4()).replace("-", ""))


def store_file(file):
    code = unique_code()
    new_name = process_name(code, get_extension(file.name))
    for chunk in file.chunks():
        with open(join_path(MEDIA_ROOT, 'uploads', new_name), mode="wb+") as write_file:
            write_file.write(chunk)

    uploads = UploadUser(
        original_name=file.name,
        content_type=file.content_type,
        size=file.size,
        code=code,
        new_name=new_name,
        path=media_path(new_name)
    )
    uploads.save()

    return uploads.id

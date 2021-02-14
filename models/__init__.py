#!/usr/bin/python3

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

""" This init file handles the file storage """

storage = FileStorage()
storage.reload()

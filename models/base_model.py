#!/usr/bin/python3
""" Class BaseModel """
import uuid
from datetime import datetime
from models.engine.file_storage import storage


class BaseModel:
     """ construct """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strftime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                if "id" not in kwargs:
                    self.id = str(uuid.uuid4())
                    self.createdat = datetime.now()
                    self.updatedat = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.createdat = datetime.now()
            self.updatedat = datetime.now()
            models.storage.new(self)

    def __str__(self):
         """ String """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """save function"""
        self.updatedat = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dictonary """
        our_dict = dict(self.__dict__)
        our_dict["__class__"] = (type(self).__name__)
        our_dict['createdat'] = self.createdat.isoformat()
        our_dict['updatedat'] = self.updatedat.isoformat()
        return our_dict

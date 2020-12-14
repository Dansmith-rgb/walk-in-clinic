from django.db import models
import json

class Register(models.Model):
    name = models.CharField(max_length=60, unique = True)
    password = models.CharField(max_length=60)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return {'message': 'Username not available'}, 400

class Signin(models.Model):
    pass
    def __str__(self):
        return self.name
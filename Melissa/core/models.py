from django.db import models
from django.contrib.auth.models import User



tipo_mensajes=[
    ("Ciencias","Ciencias"),
    ("Humanista","Humanista"),
    ("Informatica","Informatica"),
    ("Tecnologia","Tecnologia"),
    ("Electricidad","Electricidad"),
    ("Quimica","Quimica"),
    ("Matematica","Matematica"),
]
    

class Mensaje(models.Model):
    Nombree= models.CharField(max_length=100)
    tipo= models.CharField(max_length=100,choices=tipo_mensajes)
    alumno= models.CharField(max_length=100)
    profesor=models.CharField(max_length=100)
    informacion=models.CharField(max_length=250)
    def __str__(self) -> str:
        return self.Nombree
    
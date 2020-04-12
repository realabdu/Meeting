from django.db import models


class room(models.Model):
    @property
    def files_related(self):
        return self.files.objects.all()



class file(models.Model):
    room = models.ForeignKey('room' , null=True , related_name='files' , on_delete=models.CASCADE)

# Create your models here.

from django.db import models
from picklefield import PickledObjectField


class Component(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True, null=False, blank=False)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    structure = PickledObjectField()
    path = models.CharField(max_length=100, null=True, blank=True)
    sequence_number = models.PositiveSmallIntegerField(default=0, null=False, blank=False)

    class Meta:
        ordering = ['sequence_number']

    def __str__(self):
        return self.name

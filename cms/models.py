from django.db import models

from cms.services.structures import Levels


class Component(models.Model):
    LEVELS = [(level.name, level.value) for level in Levels]
    name = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False, default='Заголовок')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    structure = models.JSONField()
    path = models.CharField(max_length=100, null=True, blank=True)
    sequence_number = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    level = models.CharField(max_length=100, choices=LEVELS,
                             default=Levels.any.value)

    class Meta:
        ordering = ['sequence_number']

    def __str__(self):
        return self.name


class AppScript(models.Model):
    name = models.CharField(max_length=100)
    path = models.TextField()

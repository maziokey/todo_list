from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class TenInstanceMixin(object):
    """Makes sure that no more than Ten instances of a given model is created."""

    def clean(self):
        model = self.__class__
        if (model.objects.count() >= 10):
            raise ValidationError("Can only create 10 %s instance" % model.__name__)
        super(TenInstanceMixin, self).clean()


class Task(TenInstanceMixin, models.Model):
    title=models.CharField(max_length=350)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models


class Coordinator(models.Model):

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name


class Visitor(models.Model):

    host = models.ForeignKey(Coordinator, on_delete=models.SET_NULL, null=True, related_name='visitors')
    name = models.CharField(max_length=50)
    organization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)
    event = models.CharField(max_length=100)
    date = models.DateField()
    updated  = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated' , '-created']


    def __str__(self) -> str:
        return self.name
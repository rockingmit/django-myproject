from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=30)
    status = models.IntegerField(default=1)
    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)
    def __str__(self):
        return self.name

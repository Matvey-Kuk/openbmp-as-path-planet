from asn2location import getCoordinates

from django.db import models


class Peer(models.Model):
    hash = models.CharField(max_length=1000)

    def __str__(self):
        return self.hash


class Prefix(models.Model):
    prefix = models.CharField(max_length=1000)

    def __str__(self):
        return self.prefix


class AS(models.Model):
    number = models.IntegerField(default=0)
    latitude = models.CharField(max_length=200, default="", null=True, blank=True)
    longitude = models.CharField(max_length=200, default="", null=True, blank=True)

    def clean(self):
        print("aSASDSADASD")
        res = getCoordinates(self.number)
        if res is not None:
            print(res)
            self.longitude = res['lat']
            self.latitude = res['lng']
        else:
            if(self.latitude == "" or self.longitude == ""):
                self.latitude = 0
                self.longitude = 0
        return super(AS, self).clean()

    def __str__(self):
        return str(self.number)


class PathUpdate(models.Model):
    peer = models.ForeignKey('Peer', related_name='updates')
    paths = models.ManyToManyField(AS, related_name='updates')
    prefix = models.ForeignKey('Prefix', related_name='updates')
    time = models.DateTimeField()

    def __str__(self):
        return str(self.peer) + " " + str(self.prefix) + " " + str(self.paths) + " " + str(self.time)
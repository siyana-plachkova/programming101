from django.db import models


class Movie(models.Model):

    name = models.CharField(max_length=100)

    rating = models.FloatField()

    def __str__(self):
        all_projections = self.projections.all()
        return "%s - %d" % (self.name, len(all_projections))


class Projection(models.Model):

    PROJECTION_TYPE_CHOICES = (
        ('2D', '2D'),
        ('3D', '3D'),
        ('4DX', '4DX'),
    )

    projection_type = models.CharField(max_length=3,
                                       choices=PROJECTION_TYPE_CHOICES)

    date_time = models.DateTimeField()

    movie = models.ForeignKey(Movie, related_name='projections')

    def __str__(self):
        return "%s - %s - %s" % (self.projection_type, str(self.date_time), self.movie.name)


class Reservation(models.Model):

    username = models.CharField(max_length=30)

    projection = models.ForeignKey(Projection, related_name='reservations')

    row = models.PositiveSmallIntegerField()

    col = models.PositiveSmallIntegerField()

    def __str__(self):
        return "%s - %s - %s" % (self.username, str(self.projection.date_time), self.projection.movie.name)

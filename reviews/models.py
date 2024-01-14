from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    rate = models.IntegerField()

    def __str__(self):
        return f'name:{self.name} review: {self.review} rate:{self.rate}'
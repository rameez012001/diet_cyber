from django.db import models

class fdata(models.Model):
    food=models.CharField(max_length=255)
    calories=models.IntegerField()
    protein=models.FloatField()
    fat=models.FloatField()


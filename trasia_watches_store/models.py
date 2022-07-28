from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Watch(models.Model):
    name = models.CharField("Name", max_length=255)
    type = models.CharField("Type", max_length=255)
    # features = models.TextField("Features")
    # price = models.DecimalField("Price", max_digits=6, decimal_places=2)
    # stockNum = models.IntegerField("Stock Number")
    # brand = models.CharField("Brand", max_length=100)
    # family = models.CharField("Family", max_length=100)
    # model = models.CharField("Model", max_length=100)
    # limited = models.BooleanField("Limited", default=False)
    # water_resistance_depth = models.IntegerField("Water Resistance Feature", default=0)
    # case_description = models.TextField("Case Description")
    # dial_description = models.TextField("Dial Description")
    # movement_description = models.TextField("Movement Description")
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True)
    users = models.ManyToManyField("users.CustomUser", related_name="watches")

    def __str__(self):
        return self.name

class WatchesPicture(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)

    def __str__(self):
        return f'Photo for watch_id: {self.watch.id} @{self.url}'
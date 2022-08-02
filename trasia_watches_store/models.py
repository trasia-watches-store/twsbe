from django.db import models
from users.models import CustomUser

# Create your models here.
# Image tester
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class MyModel(models.Model):
    # creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=80, blank=False, null=False)
    description = models.TextField()
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    creator = models.ManyToManyField("users.CustomUser")
###############################################################################
class Watch(models.Model):
    name = models.CharField("Name", max_length=255)
    type = models.CharField("Type", max_length=255)
    features = models.TextField("Features", null=True, blank=True)
    price = models.DecimalField("Price", max_digits=6, decimal_places=2, null=True, blank=True)
    stockNum = models.IntegerField("Stock Number", null=True, blank=True)
    brand = models.CharField("Brand", max_length=100, null=True, blank=True)
    family = models.CharField("Family", max_length=100, null=True, blank=True)
    model = models.CharField("Model", max_length=100, null=True, blank=True)
    limited = models.BooleanField("Limited", default=False, null=True, blank=True)
    water_resistance_depth = models.IntegerField("Water Resistance Feature", default=0, null=True, blank=True)
    case_description = models.TextField("Case Description", null=True, blank=True)
    dial_description = models.TextField("Dial Description", null=True, blank=True)
    movement_description = models.TextField("Movement Description", null=True, blank=True)
    wimage = models.ImageField("Watch Image", upload_to=upload_to, null=True, blank=True)
    # wimage = models.CharField(max_length=255)
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
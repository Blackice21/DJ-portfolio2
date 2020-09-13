from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.URLField(blank=True)

    def fixedtime(self):
        return datetime.strftime(self.pub_date,'%b %d %Y')

    def summary(self):
        return self.body[0:76]
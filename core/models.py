from django.db import models

from django.conf import settings
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100,unique=True)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    #pdf = PrivateFileField("File")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #       short_url=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)

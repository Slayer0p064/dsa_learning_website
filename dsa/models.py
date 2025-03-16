from django.db import models

class DSATopic(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pdf_file = models.FileField(upload_to='pdfs/', blank=True, null=True)

    def __str__(self):
        return self.title

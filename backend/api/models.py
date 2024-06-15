from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

    def summary(self):
        return self.content[:100]
    
    class Meta:
        ordering = ['-published_date']

    
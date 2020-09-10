from django.db import models
from django.db.models import Q
from users.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=511, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(to="Tag", related_name="questions", blank=True)
    answer = models.ForeignKey("Answer", on_delete=models.CASCADE, blank=True, null=True, related_name='questions')
    star_by_user = models.ManyToManyField(to=User, related_name="questions", blank=True)


    def get_tag_names(self):
        tag_names = []
        for tag in self.tags.all():
            tag_names.append(tag.tag)

        return " ".join(tag_names)

    def __str__(self):
        return f'{self.title} | {self.body}'

class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag

class Answer(models.Model):
    body = models.TextField(null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    star_by_user = models.ManyToManyField(to=User, related_name="answers", blank=True)
    
    def __str__(self):
        return self.body
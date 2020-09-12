from django.db import models
from django.db.models import Q, QuerySet
from users.models import User
# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag

class Question(models.Model):
    title = models.CharField(max_length=511, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False, null=False)
    tags = models.ManyToManyField(to="Tag", related_name="questions", blank=True)
    answer = models.ManyToManyField("Answer",  related_name='questions', blank=True)
    star_by_user = models.ManyToManyField(to=User, related_name="questions", blank=True)

    def __str__(self):
        return f'{self.title} | {self.body}'

    def get_tag_names(self):
        tag_names = []
        for tag in self.tags.all():
            tag_names.append(tag.tag)

        return " ".join(tag_names)


    def set_tag_names(self, tag_names):
        """
        Given a string of tag names separated by spaces,
        create any tags that do not currently exist, and associate all
        of these tags with the recipe.
        """
        tag_names = tag_names.split()
        tags = []
        for tag_name in tag_names:
            tag = Tag.objects.filter(tag=tag_name).first()
            if tag is None:
                tag = Tag.objects.create(tag=tag_name)
            tags.append(tag)
        self.tags.set(tags)

class Answer(models.Model):
    body = models.TextField(null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False, null=False)
    star_by_user = models.ManyToManyField(to=User, related_name="answers", blank=True)
    
    def __str__(self):
        return self.body

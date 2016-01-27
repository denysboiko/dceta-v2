import datetime

from django.utils import timezone

from django.db import models


class Cover(models.Model):
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)


class Image(models.Model):
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    image_url = models.URLField(max_length=200)
    load_date = models.DateTimeField('Loaded')
    user = models.CharField(max_length=200)

    def __unicode__(self):
        return self.artist + ", " + self.album


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
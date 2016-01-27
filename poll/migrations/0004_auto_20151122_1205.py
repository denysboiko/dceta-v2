# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_image_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='load_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 12, 4, 31, 660249, tzinfo=utc), verbose_name=b'Loaded'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.CharField(default='denysboiko', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='year',
            field=models.CharField(default='2015', max_length=4),
            preserve_default=False,
        ),
    ]

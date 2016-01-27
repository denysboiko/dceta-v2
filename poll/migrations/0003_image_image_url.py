# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_url',
            field=models.URLField(default='/Users/denisbojko/PycharmProjects/TestApp/poll/covers/m/f2f8134c166404f6d27951fb232e2d8aca6533d3.jpeg'),
            preserve_default=False,
        ),
    ]

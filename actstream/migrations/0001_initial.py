# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actor_object_id', models.CharField(max_length=255, db_index=True)),
                ('verb', models.CharField(max_length=255, db_index=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('target_object_id', models.CharField(db_index=True, max_length=255, null=True, blank=True)),
                ('action_object_object_id', models.CharField(db_index=True, max_length=255, null=True, blank=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('public', models.BooleanField(default=True, db_index=True)),
                ('data', jsonfield.fields.JSONField(null=True, blank=True)),
                ('action_object_content_type', models.ForeignKey(related_name='action_object', blank=True, to='contenttypes.ContentType', null=True)),
                ('actor_content_type', models.ForeignKey(related_name='actor', to='contenttypes.ContentType')),
                ('target_content_type', models.ForeignKey(related_name='target', blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.CharField(max_length=255, db_index=True)),
                ('actor_only', models.BooleanField(default=True, verbose_name='Only follow actions where the object is the target.')),
                ('started', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('user', 'content_type', 'object_id')]),
        ),
    ]

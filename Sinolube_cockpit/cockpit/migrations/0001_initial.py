# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BiCommonPagesu',
            fields=[
                ('mstrid', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('mstrname', models.CharField(max_length=64, blank=True)),
                ('mstraddr', models.CharField(max_length=250, blank=True)),
                ('urladdr', models.CharField(max_length=1000, blank=True)),
            ],
            options={
                'verbose_name': '\u9875\u9762\u914d\u7f6e',
                'db_table': 'bi_common_pagesu',
                'managed': True,
                'verbose_name_plural': '\u9875\u9762\u914d\u7f6e',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PagesuDocID',
            fields=[
                ('pageid', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('documentname', models.CharField(max_length=64, blank=True)),
                ('docid', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'verbose_name': '\u6587\u6863\u914d\u7f6e',
                'db_table': 'bi__pagesu_docid',
                'managed': True,
                'verbose_name_plural': '\u6587\u6863\u914d\u7f6e',
            },
            bases=(models.Model,),
        ),
    ]

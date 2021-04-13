# Generated by Django 3.1.7 on 2021-04-08 12:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='招聘岗位')),
                ('description', models.TextField(verbose_name='招聘要求')),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '招聘信息',
                'verbose_name_plural': '招聘信息',
                'ordering': ['-publish_date'],
            },
        ),
    ]
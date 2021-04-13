# Generated by Django 3.1.7 on 2021-04-12 02:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='资料名称')),
                ('file', models.FileField(blank=True, upload_to='Service/', verbose_name='文件资料')),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='上传时间')),
            ],
            options={
                'verbose_name': '资料',
                'verbose_name_plural': '资料',
                'ordering': ['-publish_date'],
            },
        ),
    ]
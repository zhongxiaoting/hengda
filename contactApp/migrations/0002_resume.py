# Generated by Django 3.1.7 on 2021-04-09 07:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='招聘岗位')),
                ('personID', models.CharField(max_length=30, verbose_name='身份证号')),
                ('sex', models.CharField(choices=[('男', '男'), ('女', '女')], default='男', max_length=5, verbose_name='性别')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('birth', models.DateField(default='2021-04-09', verbose_name='出生日期')),
                ('edu', models.CharField(default='本科', max_length=50, verbose_name='学历')),
                ('school', models.CharField(max_length=50, verbose_name='毕业学校')),
                ('major', models.CharField(max_length=50, verbose_name='专业')),
                ('position', models.CharField(max_length=40, verbose_name='申请职位')),
                ('experience', models.TextField(blank=True, null=True, verbose_name='项目经验')),
                ('photo', models.ImageField(upload_to='contact/recruit/%Y-%m-%d', verbose_name='个人照片')),
                ('status', models.CharField(choices=[(1, '未审'), (2, '通过'), (3, '未通过')], default=1, max_length=5, verbose_name='面试成绩')),
                ('publish_data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='提交时间')),
            ],
            options={
                'verbose_name': '简历',
                'verbose_name_plural': '简历',
                'ordering': ('-status', '-publish_data'),
            },
        ),
    ]

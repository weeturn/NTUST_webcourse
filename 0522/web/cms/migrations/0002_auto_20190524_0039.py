# Generated by Django 2.0 on 2019-05-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='food',
            name='restaurant',
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]

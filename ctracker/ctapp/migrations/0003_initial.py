# Generated by Django 4.0.5 on 2022-10-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ctapp', '0002_delete_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='fdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('calories', models.IntegerField()),
            ],
        ),
    ]

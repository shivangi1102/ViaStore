# Generated by Django 3.0.3 on 2020-03-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0007_auto_20200313_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regisvendor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
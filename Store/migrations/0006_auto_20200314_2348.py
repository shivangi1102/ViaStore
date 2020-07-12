# Generated by Django 3.0.3 on 2020-03-14 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='id',
        ),
        migrations.AddField(
            model_name='cart',
            name='imag',
            field=models.ImageField(default='', upload_to='Vendor/images'),
        ),
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='cart',
            name='prod_tittle',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='cart',
            name='c_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
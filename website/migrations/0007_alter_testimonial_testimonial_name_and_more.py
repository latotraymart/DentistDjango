# Generated by Django 4.1.1 on 2022-11-07 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='Testimonial_Name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='Testimonial_Patient',
            field=models.CharField(max_length=250),
        ),
    ]
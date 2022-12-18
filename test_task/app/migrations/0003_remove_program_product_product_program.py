# Generated by Django 4.1.3 on 2022-12-16 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_image_alter_product_model_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.program'),
        ),
    ]
# Generated by Django 4.1.4 on 2022-12-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created',), 'verbose_name_plural': 'Product'},
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]

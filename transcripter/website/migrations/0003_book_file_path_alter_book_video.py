# Generated by Django 4.1 on 2022-08-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_book_pdf_book_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file_path',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='video',
            field=models.FileField(upload_to=''),
        ),
    ]
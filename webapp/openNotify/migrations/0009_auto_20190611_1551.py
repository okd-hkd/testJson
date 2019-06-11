# Generated by Django 2.2.2 on 2019-06-11 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openNotify', '0008_remove_apiresponse_jsondata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newapiresponse',
            old_name='request_timestamp',
            new_name='altitude',
        ),
        migrations.RenameField(
            model_name='newapiresponse',
            old_name='response_timestamp',
            new_name='datetime',
        ),
        migrations.RemoveField(
            model_name='newapiresponse',
            name='image_path',
        ),
        migrations.RemoveField(
            model_name='newapiresponse',
            name='success',
        ),
    ]

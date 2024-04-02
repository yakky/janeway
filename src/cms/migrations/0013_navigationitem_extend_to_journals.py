# Generated by Django 3.2.18 on 2023-05-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_navigationitem_for_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationitem',
            name='extend_to_journals',
            field=models.BooleanField(
                default=False,
                help_text='Whether this item should be '
                          'extended to journal websites. '
                          'Only implemented for footer links.',
            ),
        ),
    ]

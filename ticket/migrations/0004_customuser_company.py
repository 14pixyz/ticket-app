# Generated by Django 4.2.11 on 2024-07-26 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_customuser_is_supporter_alter_event_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ticket.company'),
            preserve_default=False,
        ),
    ]

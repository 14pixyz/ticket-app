# Generated by Django 4.2.11 on 2024-07-31 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0010_alter_ticket_area_alter_ticket_seat_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ticket.company'),
            preserve_default=False,
        ),
    ]

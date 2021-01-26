# Generated by Django 3.1.3 on 2021-01-25 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('educator', '0004_educator_pin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('shift_start', models.TimeField(null=True)),
                ('shift_end', models.TimeField(null=True)),
                ('lunch', models.CharField(choices=[('1 hr', '1 hr'), ('30 min', '30 min'), ('1 hr 30min', '1 hr 30min'), ('2 hr', '2 hr')], max_length=200, null=True)),
                ('educator_shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='educator.educator')),
            ],
        ),
    ]

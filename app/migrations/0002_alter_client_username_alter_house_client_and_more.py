# Generated by Django 4.2.20 on 2025-03-14 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='house',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.client'),
        ),
        migrations.AlterField(
            model_name='house',
            name='house_number',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('receipt_number', models.AutoField(primary_key=True, serialize=False)),
                ('date_issued', models.DateTimeField(auto_now_add=True)),
                ('monthly_rent', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('rental_deposit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('electricity_deposit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('electricity_bill', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('water_deposit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('water_bill', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('service_charge', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('security_charge', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('previous_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('other_charges', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.client')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.house')),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2023-03-07 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('Email', models.EmailField(max_length=100)),
                ('Address', models.TextField(max_length=600)),
                ('Branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bankapp.branch')),
                ('District', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bankapp.district')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='District',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.district'),
        ),
    ]
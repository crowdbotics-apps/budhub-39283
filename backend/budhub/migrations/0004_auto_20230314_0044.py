# Generated by Django 2.2.28 on 2023-03-14 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budhub', '0003_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='type',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_type', to='budhub.Company_type'),
        ),
    ]
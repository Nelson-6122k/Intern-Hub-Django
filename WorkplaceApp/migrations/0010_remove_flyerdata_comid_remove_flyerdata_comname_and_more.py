# Generated by Django 4.1.5 on 2023-01-25 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WorkplaceApp', '0009_rename_comid_studentflyer_stuid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flyerdata',
            name='comid',
        ),
        migrations.RemoveField(
            model_name='flyerdata',
            name='comname',
        ),
        migrations.RemoveField(
            model_name='studentflyer',
            name='flyerid',
        ),
        migrations.RemoveField(
            model_name='studentflyer',
            name='stuid',
        ),
        migrations.AddField(
            model_name='flyerdata',
            name='company',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='WorkplaceApp.companydatatable'),
        ),
        migrations.AddField(
            model_name='studentflyer',
            name='flyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='WorkplaceApp.flyerdata'),
        ),
        migrations.AddField(
            model_name='studentflyer',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='WorkplaceApp.studentdatatable'),
        ),
    ]

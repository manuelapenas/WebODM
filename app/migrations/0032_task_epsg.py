# Generated by Django 2.1.15 on 2021-11-01 14:37

from django.db import migrations, models
import rasterio
import os
from webodm import settings

def update_epsg_fields(apps, schema_editor):
    Task = apps.get_model('app', 'Task')

    for t in Task.objects.all():

        epsg = None
        for asset in [os.path.join('odm_orthophoto', 'odm_orthophoto.tif'), 
                      os.path.join('odm_dem', 'dsm.tif'), 
                      os.path.join('odm_dem', 'dtm.tif')]:
            asset_path = os.path.join(settings.MEDIA_ROOT, "project", str(t.project.id), "task", str(t.id), "assets", asset)
            if os.path.isfile(asset_path):
                try:
                    with rasterio.open(asset_path) as f:
                        if f.crs is not None:
                            epsg = f.crs.to_epsg()
                            break # We assume all assets are in the same CRS
                except Exception as e:
                    print(e)
                
        print("Updating {} (with epsg: {})".format(t, epsg))

        t.epsg = epsg
        t.save()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20210610_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='epsg',
            field=models.IntegerField(blank=True, default=None, help_text='EPSG code of the dataset (if georeferenced)', null=True, verbose_name='EPSG'),
        ),

        migrations.RunPython(update_epsg_fields),
    ]
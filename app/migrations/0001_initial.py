# Generated by Django 4.2.14 on 2024-08-17 07:04

import app.models.task
import colorfield.fields
from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('nodeodm', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('name', models.CharField(help_text='Plugin name', max_length=255, primary_key=True, serialize=False, verbose_name='Name')),
                ('enabled', models.BooleanField(db_index=True, default=True, help_text='Whether this plugin is turned on.', verbose_name='Enabled')),
            ],
            options={
                'verbose_name': 'Plugin',
                'verbose_name_plural': 'Plugins',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A label used to describe the project', max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, default='', help_text='More in-depth description of the project', verbose_name='Description')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date', verbose_name='Created at')),
                ('deleting', models.BooleanField(db_index=True, default=False, help_text='Whether this project has been marked for deletion. Projects that have running tasks need to wait for tasks to be properly cleaned up before they can be deleted.', verbose_name='Deleting')),
                ('tags', models.TextField(blank=True, db_index=True, default='', help_text='Project tags', verbose_name='Tags')),
                ('owner', models.ForeignKey(help_text='The person who created the project', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of theme', max_length=255, verbose_name='Name')),
                ('primary', colorfield.fields.ColorField(default='#2c3e50', help_text='Most text, icons, and borders.', image_field=None, max_length=25, samples=None, verbose_name='Primary')),
                ('secondary', colorfield.fields.ColorField(default='#ffffff', help_text='The main background color, and text color of some buttons.', image_field=None, max_length=25, samples=None, verbose_name='Secondary')),
                ('tertiary', colorfield.fields.ColorField(default='#3498db', help_text='Navigation links.', image_field=None, max_length=25, samples=None, verbose_name='Tertiary')),
                ('button_primary', colorfield.fields.ColorField(default='#2c3e50', help_text='Primary button color.', image_field=None, max_length=25, samples=None, verbose_name='Button Primary')),
                ('button_default', colorfield.fields.ColorField(default='#95a5a6', help_text='Default button color.', image_field=None, max_length=25, samples=None, verbose_name='Button Default')),
                ('button_danger', colorfield.fields.ColorField(default='#e74c3c', help_text='Delete button color.', image_field=None, max_length=25, samples=None, verbose_name='Button Danger')),
                ('header_background', colorfield.fields.ColorField(default='#3498db', help_text="Background color of the site's header.", image_field=None, max_length=25, samples=None, verbose_name='Header Background')),
                ('header_primary', colorfield.fields.ColorField(default='#ffffff', help_text="Text and icons in the site's header.", image_field=None, max_length=25, samples=None, verbose_name='Header Primary')),
                ('border', colorfield.fields.ColorField(default='#e7e7e7', help_text='The color of most borders.', image_field=None, max_length=25, samples=None, verbose_name='Border')),
                ('highlight', colorfield.fields.ColorField(default='#f7f7f7', help_text='The background color of panels and some borders.', image_field=None, max_length=25, samples=None, verbose_name='Highlight')),
                ('dialog_warning', colorfield.fields.ColorField(default='#f39c12', help_text='The border color of warning dialogs.', image_field=None, max_length=25, samples=None, verbose_name='Dialog Warning')),
                ('failed', colorfield.fields.ColorField(default='#ffcbcb', help_text='The background color of failed notifications.', image_field=None, max_length=25, samples=None, verbose_name='Failed')),
                ('success', colorfield.fields.ColorField(default='#cbffcd', help_text='The background color of success notifications.', image_field=None, max_length=25, samples=None, verbose_name='Success')),
                ('css', models.TextField(blank=True, default='', verbose_name='CSS')),
                ('html_before_header', models.TextField(blank=True, default='', verbose_name='HTML (before header)')),
                ('html_after_header', models.TextField(blank=True, default='', verbose_name='HTML (after header)')),
                ('html_after_body', models.TextField(blank=True, default='', verbose_name='HTML (after body)')),
                ('html_footer', models.TextField(blank=True, default='', verbose_name='HTML (footer)')),
            ],
            options={
                'verbose_name': 'Theme',
                'verbose_name_plural': 'Theme',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('uuid', models.CharField(blank=True, db_index=True, default='', help_text='Identifier of the task (as returned by NodeODM API)', max_length=255, verbose_name='UUID')),
                ('name', models.CharField(blank=True, help_text='A label for the task', max_length=255, null=True, verbose_name='Name')),
                ('processing_time', models.IntegerField(default=-1, help_text='Number of milliseconds that elapsed since the beginning of this task (-1 indicates that no information is available)', verbose_name='Processing Time')),
                ('auto_processing_node', models.BooleanField(default=True, help_text='A flag indicating whether this task should be automatically assigned a processing node', verbose_name='Auto Processing Node')),
                ('status', models.IntegerField(blank=True, choices=[(10, 'QUEUED'), (20, 'RUNNING'), (30, 'FAILED'), (40, 'COMPLETED'), (50, 'CANCELED')], db_index=True, help_text='Current status of the task', null=True, verbose_name='Status')),
                ('last_error', models.TextField(blank=True, help_text='The last processing error received', null=True, verbose_name='Last Error')),
                ('options', models.JSONField(blank=True, default=dict, help_text='Options that are being used to process this task', validators=[app.models.task.validate_task_options], verbose_name='Options')),
                ('available_assets', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=80), blank=True, default=list, help_text='List of available assets to download', size=None, verbose_name='Available Assets')),
                ('orthophoto_extent', django.contrib.gis.db.models.fields.GeometryField(blank=True, help_text='Extent of the orthophoto', null=True, srid=4326, verbose_name='Orthophoto Extent')),
                ('dsm_extent', django.contrib.gis.db.models.fields.GeometryField(blank=True, help_text='Extent of the DSM', null=True, srid=4326, verbose_name='DSM Extent')),
                ('dtm_extent', django.contrib.gis.db.models.fields.GeometryField(blank=True, help_text='Extent of the DTM', null=True, srid=4326, verbose_name='DTM Extent')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date', verbose_name='Created at')),
                ('pending_action', models.IntegerField(blank=True, choices=[(1, 'CANCEL'), (2, 'REMOVE'), (3, 'RESTART'), (4, 'RESIZE'), (5, 'IMPORT')], db_index=True, help_text='A requested action to be performed on the task. The selected action will be performed by the worker at the next iteration.', null=True, verbose_name='Pending Action')),
                ('public', models.BooleanField(default=False, help_text='A flag indicating whether this task is available to the public', verbose_name='Public')),
                ('resize_to', models.IntegerField(default=-1, help_text='When set to a value different than -1, indicates that the images for this task have been / will be resized to the size specified here before processing.', verbose_name='Resize To')),
                ('upload_progress', models.FloatField(blank=True, default=0.0, help_text="Value between 0 and 1 indicating the upload progress of this task's files to the processing node", verbose_name='Upload Progress')),
                ('resize_progress', models.FloatField(blank=True, default=0.0, help_text="Value between 0 and 1 indicating the resize progress of this task's images", verbose_name='Resize Progress')),
                ('running_progress', models.FloatField(blank=True, default=0.0, help_text='Value between 0 and 1 indicating the running progress (estimated) of this task', verbose_name='Running Progress')),
                ('import_url', models.TextField(blank=True, default='', help_text='URL this task is imported from (only for imported tasks)', verbose_name='Import URL')),
                ('images_count', models.IntegerField(blank=True, default=0, help_text='Number of images associated with this task', verbose_name='Images Count')),
                ('partial', models.BooleanField(default=False, help_text='A flag indicating whether this task is currently waiting for information or files to be uploaded before being considered for processing.', verbose_name='Partial')),
                ('potree_scene', models.JSONField(blank=True, default=dict, help_text='Serialized potree scene information used to save/load measurements and camera view angle', verbose_name='Potree Scene')),
                ('epsg', models.IntegerField(blank=True, default=None, help_text='EPSG code of the dataset (if georeferenced)', null=True, verbose_name='EPSG')),
                ('tags', models.TextField(blank=True, db_index=True, default='', help_text='Task tags', verbose_name='Tags')),
                ('orthophoto_bands', models.JSONField(blank=True, default=list, help_text='List of orthophoto bands', verbose_name='Orthophoto Bands')),
                ('size', models.FloatField(blank=True, default=0.0, help_text='Size of the task on disk in megabytes', verbose_name='Size')),
                ('processing_node', models.ForeignKey(blank=True, help_text='Processing node assigned to this task (or null if this task has not been associated yet)', null=True, on_delete=django.db.models.deletion.SET_NULL, to='nodeodm.processingnode', verbose_name='Processing Node')),
                ('project', models.ForeignKey(help_text='Project that this task belongs to', on_delete=django.db.models.deletion.CASCADE, to='app.project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(help_text='The name of your application', max_length=255, verbose_name='App name')),
                ('app_logo', models.ImageField(help_text='A 512x512 logo of your application (.png or .jpeg)', upload_to='settings/', verbose_name='App logo')),
                ('organization_name', models.CharField(blank=True, default='WebODM', help_text='The name of your organization', max_length=255, null=True, verbose_name='Organization name')),
                ('organization_website', models.URLField(blank=True, default='https://github.com/OpenDroneMap/WebODM/', help_text='The website URL of your organization', max_length=255, null=True, verbose_name='Organization website')),
                ('theme', models.ForeignKey(help_text='Active theme', on_delete=django.db.models.deletion.DO_NOTHING, to='app.theme', verbose_name='Theme')),
            ],
            options={
                'verbose_name': 'Settings',
                'verbose_name_plural': 'Settings',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota', models.FloatField(blank=True, default=-1, help_text='Maximum disk quota in megabytes', verbose_name='Quota')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Preset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A label used to describe the preset', max_length=255, verbose_name='Name')),
                ('options', models.JSONField(blank=True, default=list, help_text="Options that define this preset (same format as in a Task's options).", validators=[app.models.task.validate_task_options], verbose_name='Options')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date', verbose_name='Created at')),
                ('system', models.BooleanField(db_index=True, default=False, help_text='Whether this preset is available to every user in the system or just to its owner.', verbose_name='System')),
                ('owner', models.ForeignKey(blank=True, help_text='The person who owns this preset', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Preset',
                'verbose_name_plural': 'Presets',
            },
        ),
        migrations.CreateModel(
            name='PluginDatum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, help_text='Setting key', max_length=255, verbose_name='Key')),
                ('int_value', models.IntegerField(blank=True, default=None, null=True, verbose_name='Integer value')),
                ('float_value', models.FloatField(blank=True, default=None, null=True, verbose_name='Float value')),
                ('bool_value', models.BooleanField(blank=True, default=None, null=True, verbose_name='Bool value')),
                ('string_value', models.TextField(blank=True, default=None, null=True, verbose_name='String value')),
                ('json_value', models.JSONField(blank=True, default=None, null=True, verbose_name='JSON value')),
                ('user', models.ForeignKey(blank=True, default=None, help_text='The user this setting belongs to. If NULL, the setting is global.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Plugin Datum',
                'verbose_name_plural': 'Plugin Datum',
            },
        ),
        migrations.CreateModel(
            name='ProjectUserObjectPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.permission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'unique_together': {('user', 'permission', 'content_object')},
            },
        ),
        migrations.CreateModel(
            name='ProjectGroupObjectPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.permission')),
            ],
            options={
                'abstract': False,
                'unique_together': {('group', 'permission', 'content_object')},
            },
        ),
    ]

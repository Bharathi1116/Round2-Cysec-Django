# Generated by Django 5.0.4 on 2024-04-10 04:21

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_projectfile_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectNote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='project.project')),
            ],
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-21 00:08

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KubernetesContainer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='kubernetes-object', max_length=128)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('image_name', models.CharField(db_index=True, default='debian', help_text='Properly qualified image name to execute this job within', max_length=200)),
                ('image_tag', models.CharField(db_index=True, default='latest', help_text='Tag name for the image to be used for this job', max_length=100)),
                ('image_pull_policy', models.CharField(choices=[('Always', 'Always'), ('IfNotPresent', 'IfNotPresent'), ('Never', 'Never')], default='IfNotPresent', max_length=16)),
                ('command', models.TextField(blank=True, default='/bin/sh', help_text='Command to run when instantiating container', null=True)),
                ('args', models.TextField(blank=True, default='-c,sleep 6000', help_text='Comma separated args to run with command when instantiating container.', null=True)),
                ('port', models.IntegerField(default=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TargetCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('api_endpoint', models.URLField(help_text='Cluster Endpoint URL')),
                ('telemetry_endpoint', models.URLField(help_text='Telemetry Endpoint URL')),
                ('telemetry_source', models.CharField(choices=[('p', 'Prometheus')], default='p', max_length=5)),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(help_text='Configuration data stored as an encrypted blob in the database')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KubernetesVolumeMount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='kubernetes-object', max_length=128)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('mount_path', models.CharField(default='/media', max_length=255)),
                ('sub_path', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('cluster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_kubernetes_manager.TargetCluster')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KubernetesVolume',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='kubernetes-object', max_length=128)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('cluster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_kubernetes_manager.TargetCluster')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KubernetesService',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='kubernetes-object', max_length=128)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('labels', django.contrib.postgres.fields.jsonb.JSONField(default={'app': 'default'})),
                ('annotations', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('api_version', models.CharField(default='v1', max_length=16)),
                ('kind', models.CharField(default='Service', max_length=16)),
                ('port', models.IntegerField(default=80)),
                ('selector', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('target_port', models.IntegerField(default=80)),
                ('cluster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_kubernetes_manager.TargetCluster')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KubernetesPodTemplate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='kubernetes-object', max_length=128)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('labels', django.contrib.postgres.fields.jsonb.JSONField(default={'app': 'default'})),
                ('annotations', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('restart_policy', models.CharField(choices=[('Always', 'Always'), ('OnFailure', 'OnFailure'), ('Never', 'Never')], default='Never', max_length=16)),
                ('cluster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_kubernetes_manager.TargetCluster')),
                ('primary_container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_container', to='django_kubernetes_manager.KubernetesContainer')),
                ('secondary_container', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='secondary_container', to='django_kubernetes_manager.KubernetesContainer')),
                ('volume', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_kubernetes_manager.KubernetesVolume')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KubernetesIngress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='kubernetes-object', max_length=128)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('labels', django.contrib.postgres.fields.jsonb.JSONField(default={'app': 'default'})),
                ('annotations', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('api_version', models.CharField(default='v1', max_length=16)),
                ('kind', models.CharField(default='Service', max_length=16)),
                ('port', models.IntegerField(default=80)),
                ('hostname', models.CharField(default='localhost', max_length=255)),
                ('path', models.CharField(default='/', max_length=255)),
                ('cluster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_kubernetes_manager.TargetCluster')),
                ('target_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_kubernetes_manager.KubernetesService')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KubernetesDeployment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='kubernetes-object', max_length=128)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('labels', django.contrib.postgres.fields.jsonb.JSONField(default={'app': 'default'})),
                ('annotations', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('api_version', models.CharField(default='v1', max_length=16)),
                ('kind', models.CharField(default='Service', max_length=16)),
                ('port', models.IntegerField(default=80)),
                ('selector', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('replicas', models.IntegerField(default=1)),
                ('cluster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_kubernetes_manager.TargetCluster')),
                ('pod_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_kubernetes_manager.KubernetesPodTemplate')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='kubernetescontainer',
            name='cluster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_kubernetes_manager.TargetCluster'),
        ),
        migrations.AddField(
            model_name='kubernetescontainer',
            name='volume_mount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_kubernetes_manager.KubernetesVolumeMount'),
        ),
    ]

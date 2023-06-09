# Generated by Django 3.1.3 on 2023-06-09 07:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('lecture', models.BigAutoField(primary_key=True, serialize=False)),
                ('lecture_name', models.CharField(default='강사명', max_length=100)),
                ('recommended', models.FloatField(default=0)),
                ('lecture_url', models.CharField(default='https://example.com/default-url', max_length=250)),
                ('lecture_length', models.IntegerField(default=0)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('tutor', models.BigAutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(default=0, max_length=50)),
                ('tutor_name', models.CharField(default='박선생', max_length=50)),
                ('email', models.CharField(default='default@example.com', max_length=100)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user', models.BigAutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(default=0, max_length=50)),
                ('user_name', models.CharField(default='김학생', max_length=50)),
                ('email', models.CharField(default='default@example.com', max_length=100)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserLecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finish', models.CharField(default='0', max_length=10)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='ocds.lecture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='ocds.user')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('result', models.BigAutoField(primary_key=True, serialize=False)),
                ('capture_start', models.TimeField(default=django.utils.timezone.now)),
                ('capture_end', models.TimeField(default=django.utils.timezone.now)),
                ('start_log', models.TimeField(default=django.utils.timezone.now)),
                ('end_log', models.TimeField(default=django.utils.timezone.now)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocds.lecture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocds.user')),
            ],
        ),
        migrations.AddField(
            model_name='lecture',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocds.tutor'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event', models.BigAutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('sleep', models.FloatField(default=0.0)),
                ('awake', models.FloatField(default=0.0)),
                ('stateNo', models.IntegerField(default=0)),
                ('continued_time', models.IntegerField(default=0)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocds.lecture')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocds.result')),
            ],
        ),
    ]

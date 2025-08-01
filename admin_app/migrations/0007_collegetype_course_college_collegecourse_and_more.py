# Generated by Django 5.0.6 on 2025-06-03 00:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0006_psychometricanswer_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('course_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('hostel_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ranking', models.IntegerField()),
                ('scholarships', models.TextField(blank=True)),
                ('placements', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('recognized_by', models.CharField(max_length=255)),
                ('about', models.TextField(blank=True)),
                ('established_year', models.IntegerField(blank=True)),
                ('top_recruiters', models.TextField(blank=True)),
                ('college_types', models.ManyToManyField(related_name='colleges', to='admin_app.collegetype')),
            ],
        ),
        migrations.CreateModel(
            name='CollegeCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tuition_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('placements', models.TextField(blank=True)),
                ('eligibility_criteria', models.TextField()),
                ('category', models.CharField(blank=True, max_length=50)),
                ('cutoff_score', models.FloatField(blank=True, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.college')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseCutoff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('cutoff_score', models.FloatField()),
                ('college_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.collegecourse')),
            ],
            options={
                'unique_together': {('college_course', 'category')},
            },
        ),
    ]

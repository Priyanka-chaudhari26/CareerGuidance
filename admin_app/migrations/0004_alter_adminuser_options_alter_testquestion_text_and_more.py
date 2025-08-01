# Generated by Django 5.0.6 on 2025-03-29 10:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_remove_adminuser_admin_role_adminuser_is_admin'),
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminuser',
            options={},
        ),
        migrations.AlterField(
            model_name='testquestion',
            name='text',
            field=models.CharField(max_length=255),
        ),
        migrations.AddIndex(
            model_name='adminuser',
            index=models.Index(fields=['email'], name='admin_app_a_email_d14e39_idx'),
        ),
        migrations.AddIndex(
            model_name='studentanswer',
            index=models.Index(fields=['question'], name='admin_app_s_questio_706b96_idx'),
        ),
        migrations.AddIndex(
            model_name='studentanswer',
            index=models.Index(fields=['student', 'question'], name='admin_app_s_student_b40d18_idx'),
        ),
        migrations.AddIndex(
            model_name='testcategory',
            index=models.Index(fields=['name'], name='admin_app_t_name_b024b7_idx'),
        ),
        migrations.AddIndex(
            model_name='testoption',
            index=models.Index(fields=['question'], name='admin_app_t_questio_7247b2_idx'),
        ),
        migrations.AddIndex(
            model_name='testoption',
            index=models.Index(fields=['question', 'is_correct'], name='admin_app_t_questio_b3f0cf_idx'),
        ),
        migrations.AddIndex(
            model_name='testquestion',
            index=models.Index(fields=['category'], name='admin_app_t_categor_9edbfb_idx'),
        ),
        migrations.AddIndex(
            model_name='testquestion',
            index=models.Index(fields=['category', 'text'], name='admin_app_t_categor_0e4c3a_idx'),
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-30 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_alter_question_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='know_satisfied',
            new_name='satisfied',
        ),
        migrations.RemoveField(
            model_name='question',
            name='show_satisfied',
        ),
    ]

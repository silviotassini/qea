# Generated by Django 4.0.5 on 2022-06-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_alter_question_asktext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='iscorrect',
            field=models.PositiveIntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_type',
            field=models.PositiveIntegerField(choices=[(0, 'Multiple Choice'), (1, 'Right or wrong')], null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]

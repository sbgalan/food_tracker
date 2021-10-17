# Generated by Django 2.2 on 2021-10-14 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Food Name')),
                ('calories', models.FloatField(verbose_name='Calories (kcal)')),
                ('total_fat', models.FloatField(verbose_name='Total Fat (g)')),
                ('saturated_fat', models.FloatField(verbose_name='Saturated Fat (g)')),
                ('cholesterol', models.FloatField(default=0, verbose_name='Cholesterol (mg)')),
                ('sodium', models.FloatField(default=0, verbose_name='Sodium (mg)')),
                ('total_carbohydate', models.FloatField(default=0, verbose_name='Total Carbohydrate (g)')),
                ('dietary_fibre', models.FloatField(default=0, verbose_name='Dietary Fibre (g)')),
                ('sugar', models.FloatField(default=0, verbose_name='Sugar (g)')),
                ('protein', models.FloatField(default=0, verbose_name='Protein (g)')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serving_size', models.IntegerField(verbose_name='Serving Size')),
                ('meal_time', models.IntegerField(choices=[(1, 'Breakfast'), (2, 'Morning Snack'), (3, 'Lunch'), (4, 'Afternoon Snack'), (5, 'Dinner'), (6, 'Evening Snack')], verbose_name='Meal Time')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Food', verbose_name='Food')),
            ],
        ),
    ]

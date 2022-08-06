from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField(default=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=100)),
            ],
        ),
    ]
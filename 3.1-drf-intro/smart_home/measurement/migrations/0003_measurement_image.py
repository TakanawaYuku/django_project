from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='image',
            field=models.ImageField(blank=True,
                                    null=True,
                                    upload_to='measurement_images',
                                    verbose_name='Изображение'),
        ),
    ]

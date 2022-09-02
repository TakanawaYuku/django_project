from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления'
            },
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.TextField(choices=[('OPEN', 'Открыто'),
                                            ('CLOSED', 'Закрыто'),
                                            ('DRAFT', 'Черновик')],
                                   default='OPEN'),
        ),
        migrations.CreateModel(
            name='UserFavoriteAdvertisement',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('advertisement',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='advertisements.advertisement')),
                ('like_user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Объявление в избранном',
                'verbose_name_plural': 'Избранные объявления',
            },
        ),
    ]

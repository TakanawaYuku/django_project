from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_articlescope_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Раздел'),
        ),
    ]

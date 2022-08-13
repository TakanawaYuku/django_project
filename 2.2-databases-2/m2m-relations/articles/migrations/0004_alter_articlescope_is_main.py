from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles',
         '0003_alter_article_options_alter_articlescope_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlescope',
            name='is_main',
            field=models.BooleanField(verbose_name='Основной'),
        ),
    ]

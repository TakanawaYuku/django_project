from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articlescope_scope_articlescope_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={
                'ordering': ['-published_at'],
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи'
            },
        ),
        migrations.AlterModelOptions(
            name='articlescope',
            options={'ordering': ['-is_main']},
        ),
        migrations.AlterModelOptions(
            name='scope',
            options={
                'ordering': ['name'],
                'verbose_name': 'раздел',
                'verbose_name_plural': 'Разделы'
            },
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='tag',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='scopes',
                to='articles.scope',
                verbose_name='Раздел'),
        ),
    ]

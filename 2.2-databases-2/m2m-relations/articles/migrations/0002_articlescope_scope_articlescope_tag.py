from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleScope',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('is_main', models.BooleanField(default=False)),
                ('article',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='scopes',
                                   to='articles.article')),
            ],
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('articles',
                 models.ManyToManyField(related_name='tags',
                                        through='articles.ArticleScope',
                                        to='articles.article')),
            ],
        ),
        migrations.AddField(
            model_name='articlescope',
            name='tag',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='scopes',
                to='articles.scope'),
        ),
    ]

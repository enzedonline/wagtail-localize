# Generated by Django 3.1.3 on 2020-11-12 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize_test', '0009_auto_20201110_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestOverrideTranslatableFieldsPage',
            fields=[
                ('testgeneratetranslatablefieldspage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtail_localize_test.testgeneratetranslatablefieldspage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtail_localize_test.testgeneratetranslatablefieldspage',),
        ),
    ]

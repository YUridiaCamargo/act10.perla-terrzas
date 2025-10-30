from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(max_digits=10, decimal_places=2)),
                ('stock', models.PositiveIntegerField()),
                ('categoria', models.CharField(max_length=100)),
            ],
        ),
    ]

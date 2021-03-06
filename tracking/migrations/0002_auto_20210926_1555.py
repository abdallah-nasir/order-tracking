# Generated by Django 3.2.4 on 2021-09-26 13:55

from django.db import migrations, models
import django.db.models.deletion
import tracking.models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_account_trade_name'),
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iamge', models.ImageField(upload_to=tracking.models.upload_image)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.category')),
                ('image', models.ManyToManyField(to='tracking.Image')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='lat_lng',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='lat_lng',
        ),
        migrations.AlterField(
            model_name='order',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracking.shop'),
        ),
        migrations.RemoveField(
            model_name='shop',
            name='address',
        ),
        migrations.CreateModel(
            name='Product_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('ordered', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.account')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ManyToManyField(to='tracking.Image'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
                ('product', models.ManyToManyField(to='tracking.Product_Cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.account')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('lat_lng', models.CharField(max_length=100)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.account')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracking.address'),
        ),
        migrations.AddField(
            model_name='shop',
            name='address',
            field=models.ManyToManyField(to='tracking.Address'),
        ),
    ]

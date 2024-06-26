# Generated by Django 4.2.7 on 2024-05-23 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address1',
            new_name='shipping_address1',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='state',
            new_name='shipping_address2',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address2',
            new_name='shipping_city',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='city',
            new_name='shipping_country',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='country',
            new_name='shipping_email',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='email',
            new_name='shipping_full_name',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='zipcode',
            new_name='shipping_state',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='full_name',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='shipping_zipcode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-22 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auction_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancelledAuctions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancelation_reason', models.TextField()),
                ('cancelled_by', models.CharField(choices=[('owner', 'owner'), ('admin', 'admin')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SuccessAuctions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_amount', models.FloatField()),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to='auction_app.auctiondetails')),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s_bidder', to='auction_app.bidders')),
            ],
        ),
    ]

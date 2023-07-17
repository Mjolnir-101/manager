# Generated by Django 4.2.3 on 2023-07-17 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('registered_address', models.CharField(blank=True, max_length=200, null=True)),
                ('area_of_operation', models.CharField(blank=True, max_length=200, null=True)),
                ('pan_no', models.CharField(blank=True, max_length=10, null=True)),
                ('tan_no', models.CharField(blank=True, max_length=10, null=True)),
                ('officer_authorized', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('service_tax_no', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, max_length=40, null=True)),
                ('district', models.CharField(blank=True, max_length=40, null=True)),
                ('startup_type', models.CharField(blank=True, max_length=20, null=True)),
                ('is_validated', models.BooleanField(default=False)),
                ('is_investor', models.BooleanField(default=False)),
                ('startup_idea', models.CharField(max_length=1000)),
                ('startup_name', models.CharField(max_length=100)),
                ('is_registered', models.BooleanField(default=False)),
                ('is_accepted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grievance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Your name')),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('complain_type', models.CharField(max_length=100)),
                ('complain_startup', models.CharField(max_length=100)),
                ('complainXfeedback', models.CharField(max_length=100)),
                ('complain_date', models.DateTimeField(auto_now_add=True, verbose_name='date of complain')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.PositiveIntegerField(default=0)),
                ('request_text', models.TextField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('feedback', models.TextField(blank=True, max_length=500, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('comments', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startups.category')),
                ('tags', models.ManyToManyField(to='startups.tag')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

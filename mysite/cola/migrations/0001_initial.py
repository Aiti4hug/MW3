# Generated by Django 5.1.5 on 2025-02-08 22:49

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG')),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(80)], verbose_name='age')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=32, unique=True)),
                ('category_name_en', models.CharField(max_length=32, null=True, unique=True)),
                ('category_name_ru', models.CharField(max_length=32, null=True, unique=True)),
                ('category_name_de', models.CharField(max_length=32, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bio', models.TextField()),
                ('bio_en', models.TextField(null=True)),
                ('bio_ru', models.TextField(null=True)),
                ('bio_de', models.TextField(null=True)),
                ('work_days', multiselectfield.db.fields.MultiSelectField(choices=[('Mo', 'Mo'), ('Tu', 'Tu'), ('We', 'We'), ('Th', 'Th'), ('Fr', 'Fr'), ('Sa', 'Sa'), ('Su', 'Su')], max_length=16)),
                ('subject', models.TextField()),
                ('experience', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(21), django.core.validators.MaxValueValidator(45)])),
                ('role', models.CharField(choices=[('teacher', 'teacher'), ('student', 'student')], default='teacher', max_length=16)),
            ],
            options={
                'verbose_name_plural': 'teachers',
            },
            bases=('cola.profile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=64)),
                ('course_name_en', models.CharField(max_length=64, null=True)),
                ('course_name_ru', models.CharField(max_length=64, null=True)),
                ('course_name_de', models.CharField(max_length=64, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_de', models.TextField(null=True)),
                ('level', models.CharField(choices=[('ez', 'ez'), ('norm', 'norm'), ('hard', 'hard')], max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('type_course', models.CharField(choices=[('free', 'free'), ('paid', 'paid')], max_length=32)),
                ('created_ap', models.DateTimeField(auto_now_add=True)),
                ('updated_ap', models.DateTimeField(auto_now=True)),
                ('course_certificate', models.BooleanField(default=True)),
                ('category', models.ManyToManyField(to='cola.category')),
                ('author', models.ManyToManyField(to='cola.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.cart')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('stars', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('title_en', models.CharField(max_length=32, null=True)),
                ('title_ru', models.CharField(max_length=32, null=True)),
                ('title_de', models.CharField(max_length=32, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.course')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.course')),
                ('favorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.favorite')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('title_en', models.CharField(max_length=32, null=True)),
                ('title_ru', models.CharField(max_length=32, null=True)),
                ('title_de', models.CharField(max_length=32, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='course_video')),
                ('content', models.FileField(blank=True, null=True, upload_to='course_document')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.course')),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_name', models.CharField(max_length=32)),
                ('network_name_en', models.CharField(max_length=32, null=True)),
                ('network_name_ru', models.CharField(max_length=32, null=True)),
                ('network_name_de', models.CharField(max_length=32, null=True)),
                ('network_link', models.URLField()),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('title_en', models.CharField(blank=True, max_length=64, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=64, null=True)),
                ('title_de', models.CharField(blank=True, max_length=64, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('score', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.exam')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.CharField(max_length=64)),
                ('option_check', models.BooleanField(default=False)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.questions')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('teacher', 'teacher'), ('student', 'student')], default='student', max_length=16)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.student')),
            ],
        ),
        migrations.AddField(
            model_name='favorite',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.student'),
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_at', models.DateField(auto_now_add=True)),
                ('certificate_url', models.FileField(upload_to='certificate')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.student')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.student'),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('title_en', models.CharField(max_length=32, null=True)),
                ('title_ru', models.CharField(max_length=32, null=True)),
                ('title_de', models.CharField(max_length=32, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_de', models.TextField(null=True)),
                ('due_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.course')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cola.student')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cola.teacher')),
            ],
        ),
    ]

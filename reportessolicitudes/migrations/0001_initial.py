# Generated by Django 4.2.4 on 2023-08-22 21:31

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenReporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='reportes_problemas/', verbose_name='Imagen')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudInformacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='Sin título', max_length=300, verbose_name='Título')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('estatus', models.CharField(default='Pendiente', max_length=50, verbose_name='Estado')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Última Actualización')),
                ('id_ciudadano', models.CharField(max_length=20, unique=True, verbose_name='id Ciudadano')),
                ('id_funcionario', models.CharField(max_length=20, unique=True, verbose_name='id funcionario')),
                ('archivo_adjunto', models.FileField(blank=True, null=True, upload_to='archivos_solicitudes/', verbose_name='Archivo Adjunto')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioCiudadano',
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
                ('groups', models.ManyToManyField(blank=True, related_name='ciudadanos', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='ciudadanos', to='auth.permission', verbose_name='user permissions')),
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
            name='UsuarioAdministrador',
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
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'permissions': [('can_do_admin_stuff', 'Can do admin stuff')],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Open311ReporteProblema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='Sin título', max_length=300, verbose_name='Título')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('categoria', models.CharField(default='Otra', max_length=100, verbose_name='Categoría')),
                ('estatus', models.CharField(default='Pendiente', max_length=50, verbose_name='Estado')),
                ('direccion', models.CharField(max_length=200, verbose_name='Ubicación')),
                ('latitud', models.FloatField(blank=True, null=True, verbose_name='Latitud')),
                ('longitud', models.FloatField(blank=True, null=True, verbose_name='Longitud')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Última Actualización')),
                ('id_ciudadano', models.CharField(max_length=20, unique=True, verbose_name='id Ciudadano')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='reportes_problemas/', verbose_name='Imagen')),
                ('archivo_adjunto', models.FileField(blank=True, null=True, upload_to='archivos_reportes/', verbose_name='Archivo Adjunto')),
                ('imagenes', models.ManyToManyField(related_name='reportes_problemas', to='reportessolicitudes.imagenreporte')),
            ],
        ),
        migrations.CreateModel(
            name='AvanceReporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_avance', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Avance')),
                ('comentario', models.TextField(verbose_name='Comentario')),
                ('funcionario', models.CharField(max_length=20, unique=True, verbose_name='id Funcionario')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportessolicitudes.open311reporteproblema')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioFuncionario',
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
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo o Puesto')),
                ('departamento', models.CharField(max_length=100, verbose_name='Departamento o Área')),
                ('telefono_contacto', models.CharField(max_length=20, verbose_name='Teléfono de Contacto')),
                ('horario_trabajo', models.CharField(max_length=100, verbose_name='Horario de Trabajo')),
                ('especialidad', models.CharField(blank=True, max_length=100, verbose_name='Especialidad o Experiencia')),
                ('foto_perfil', models.ImageField(blank=True, upload_to='funcionarios/', verbose_name='Foto de Perfil')),
                ('groups', models.ManyToManyField(blank=True, related_name='funcionarios', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='funcionarios', to='auth.permission', verbose_name='user permissions')),
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
    ]

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

#Everything should be good now -annie

from django.db import models


class Actor(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    actor_first_name = models.CharField(max_length=255)
    actor_last_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Actor'


class Award(models.Model):
    award_id = models.IntegerField(primary_key=True)
    award_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Award'


class Casting(models.Model):
    actor_actor = models.ForeignKey(Actor, on_delete=models.CASCADE, db_column='Actor_actor_id')  # Field name made lowercase.
    movie_movie = models.ForeignKey('Movie', on_delete=models.CASCADE, db_column='Movie_movie_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Casting'


class Director(models.Model):
    director_id = models.IntegerField(primary_key=True)
    director_first_name = models.CharField(max_length=255)
    director_last_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Director'


class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    genre_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Genre'


class GenreMovieAssignment(models.Model):
    movie_movie = models.ForeignKey('Movie', on_delete=models.CASCADE, db_column='Movie_movie_id')  # Field name made lowercase.
    genre_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, db_column='Genre_genre_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Genre_movie_assignment'


class Gross(models.Model):
    domestic_gross = models.IntegerField()
    international_gross = models.IntegerField()
    movie_movie = models.ForeignKey('Movie', on_delete=models.CASCADE, db_column='Movie_movie_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gross'


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    movie_title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    duration = models.DateTimeField()
    rating_rating = models.ForeignKey('Rating', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Movie'


class MovieDirectorAssignment(models.Model):
    movie_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, db_column='Movie_movie_id')  # Field name made lowercase.
    director_director = models.ForeignKey(Director, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Movie_director_assignment'


class Rating(models.Model):
    rating_id = models.IntegerField(primary_key=True)
    rating_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Rating'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)
    permission = models.ForeignKey('AuthPermission', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(AuthPermission, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MovieAwardAssignment(models.Model):
    award_award = models.ForeignKey(Award, on_delete=models.CASCADE, db_column='Award_award_id')  # Field name made lowercase.
    movie_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, db_column='Movie_movie_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movie_award_assignment'


class Timestamps(models.Model):
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timestamps'


class User(models.Model):
    username = models.CharField(max_length=16)
    user_type = models.CharField(max_length=255)
    password = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'user'

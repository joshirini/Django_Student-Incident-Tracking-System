# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Appointment(models.Model):
    appointmentid = models.AutoField(db_column='appointmentID', primary_key=True)  # Field name made lowercase.
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentID_id', blank=True, null=True)  # Field name made lowercase.
    counselorid = models.ForeignKey('Counselor', models.DO_NOTHING, db_column='counselorID_id', blank=True, null=True)  # Field name made lowercase.
    astarttime = models.DateTimeField(db_column='aStartTime', blank=True, null=True)  # Field name made lowercase.
    aendtime = models.DateTimeField(db_column='aEndTime', blank=True, null=True)  # Field name made lowercase.
    requestcomment = models.CharField(db_column='requestComment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    requesttype = models.CharField(db_column='requestType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    timeofsubmittingrequest = models.DateTimeField(db_column='timeOfSubmittingRequest', blank=True, null=True)  # Field name made lowercase.
    requeststarttime = models.DateTimeField(db_column='requestStartTime', blank=True, null=True)  # Field name made lowercase.
    requestendtime = models.DateTimeField(db_column='requestEndTime', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Appointment'


class Counselor(models.Model):
    counselorid = models.CharField(db_column='counselorID', primary_key=True, max_length=10)  # Field name made lowercase.
    counselorlname = models.CharField(db_column='counselorLName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    counselorfname = models.CharField(db_column='counselorFName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    counselorpassword = models.CharField(db_column='counselorPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Counselor'


class Educator(models.Model):
    educatorid = models.CharField(db_column='educatorID', primary_key=True, max_length=10)  # Field name made lowercase.
    educatorfname = models.CharField(db_column='educatorFName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    educatorlname = models.CharField(db_column='educatorLName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    educatortype = models.CharField(db_column='educatorType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    educatoremailaddress = models.CharField(db_column='educatorEmailAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    educatorpassword = models.CharField(db_column='educatorPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Educator'


class Incident(models.Model):
    incidentid = models.CharField(db_column='incidentID', primary_key=True, max_length=10)  # Field name made lowercase.
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentID_id')  # Field name made lowercase.
    counselorid = models.ForeignKey(Counselor, models.DO_NOTHING, db_column='counselorID_id')  # Field name made lowercase.
    educatorid = models.ForeignKey(Educator, models.DO_NOTHING, db_column='educatorID_id')  # Field name made lowercase.
    incidenttype = models.CharField(db_column='incidentType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Incident'


class Student(models.Model):
    studentid = models.CharField(db_column='studentID', primary_key=True, max_length=10)  # Field name made lowercase.
    studentlname = models.CharField(db_column='studentLName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studentfname = models.CharField(db_column='studentFName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studentemailaddress = models.CharField(db_column='studentEmailAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studentage = models.IntegerField(db_column='studentAge', blank=True, null=True)  # Field name made lowercase.
    studentdob = models.DateField(db_column='studentDOB', blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    program = models.CharField(max_length=30, blank=True, null=True)
    trackrepid = models.ForeignKey('self', models.DO_NOTHING, db_column='trackRepID', blank=True, null=True)  # Field name made lowercase.
    studentpassword = models.CharField(db_column='studentPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studenttype = models.CharField(db_column='studentType', max_length=15, blank=True, null=True)  # Field name made lowercase.
    careergoal = models.CharField(db_column='careerGoal', max_length=100, blank=True, null=True)  # Field name made lowercase.
    studentimage = models.TextField(db_column='studentImage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student'


class Studentprofile(models.Model):
    profileid = models.CharField(db_column='profileID', primary_key=True, max_length=10)  # Field name made lowercase.
    studentid = models.ForeignKey(Student, models.DO_NOTHING, db_column='studentID_id', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=50, blank=True, null=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    seq = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'StudentProfile'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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

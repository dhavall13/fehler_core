from django.db import models
from django.utils import timezone

from .managers import AdminManager, ProjectManagerManager, TeamLeadManager


class Space(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField('fehler_auth.User', on_delete=models.CASCADE)
    members = models.ManyToManyField(
        'fehler_auth.User', through='Membership', related_name='space_members'
    )
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Space, self).save(*args, **kwargs)


class Membership(models.Model):

    ADMIN = 'ADMIN'
    PROJECT_MANAGER = 'PROJECT_MANAGER'
    TEAM_LEAD = 'TEAM_LEAD'

    TYPE_OF_MEMBER_CHOICES = [
        (ADMIN, 'Admin'),
        (PROJECT_MANAGER, 'ProjectManager'),
        (TEAM_LEAD, 'TeamLead'),
    ]

    user = models.ForeignKey('fehler_auth.User', on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    invite = models.ForeignKey('fehler_auth.Invite', null=True, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)
    type_of_member = models.CharField(
        max_length=50, choices=TYPE_OF_MEMBER_CHOICES, blank=True, null=True
    )

    def __str__(self):
        return self.user.email


class Admin(Membership):
    objects = AdminManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.member_type = Membership.ADMIN
        return super().save(*args, **kwargs)

    def is_admin(self):
        return 'i am admin'


class ProjectManager(Membership):
    objects = ProjectManagerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.member_type = Membership.PROJECT_MANAGER
        return super().save(*args, **kwargs)

    def is_projectmanger(self):
        return 'i am project manager'


class TeamLead(Membership):
    objects = TeamLeadManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.member_type = Membership.TEAM_LEAD
        return super().save(*args, **kwargs)

    def is_teamlead(self):
        return 'i am team lead'
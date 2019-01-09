from django.db import models
from django.utils import timezone
from django.conf import settings

from vng.accounts.models import User

from ..utils import choices


class TestScenario(models.Model):
    name = name = models.CharField(max_length=200, unique=True)
    validation_file = models.FileField(settings.MEDIA_FOLDER_FILES['test_scenario'])

    def __str__(self):
        return self.name


class ServerRun(models.Model):

    test_scenario = models.ForeignKey(TestScenario, on_delete=models.SET_NULL, null=True)
    api_endpoint = models.URLField(max_length=200, blank=True, null=True, default=None)
    started = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    stopped = models.DateTimeField(null=True, default=None, blank=True)
    status = models.CharField(max_length=10, choices=choices.StatusChoices.choices, default=choices.StatusChoices.starting)
    log = models.FileField(settings.MEDIA_FOLDER_FILES['servervalidation_log'], blank=True, null=True, default=None)

    def __str__(self):
        if self.user and self.api_endpoint:
            return "{} - {} - {}".format(self.api_endpoint, self.user.username, self.status)
        else:
            return "{} - {}".format(self.started, self.status)

    def is_stopped(self):
        return self.status == choices.StatusChoices.stopped

    def get_fields_no_file(self):
        '''
        Used in server-run_detail
        '''
        res = []
        for field in self._meta.fields:
            if field.get_internal_type() not in ('FileField',):
                res.append((field.name, field.value_to_string(self)))
        return res

    def display_log(self):
        if self.log:
            with open(self.log.path) as fp:
                return fp.read().replace('\n', '<br>')
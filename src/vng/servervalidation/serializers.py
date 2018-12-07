from .models import *
from rest_framework import serializers


class TestScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestScenario
        fields = ['name', 'validation_file']


class ServerRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerRun
        fields = ['pk', 'test_scenario', 'api_endpoint', 'started', 'stopped']

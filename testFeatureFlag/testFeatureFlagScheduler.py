from apscheduler.schedulers.background import BackgroundScheduler
from pymongo import MongoClient
from configuration.config import get_config_logger
from configuration.logger_messages import *
from featureFlagClient.featureFlagClient import get_grpc_clients, FeatureFlagClient
from testFeatureFlag.featureFlagDefaultValue import get_list_FeatureFlagDefaultValue, FeatureFlagDefaultValue
from testFeatureFlag.logTestFeatureFlagModel import getTestFeatureFlagModel


logger = get_config_logger()
collectionLogs = MongoClient("mongo:27017")['test-feature-flag']['logs']


def runBackgroundScheduler(scheduler: BackgroundScheduler, minutes: int):
    default_values = get_list_FeatureFlagDefaultValue()
    clients = get_grpc_clients()
    for client in clients:
        for default_value in default_values:
            arr = [client, default_value]
            scheduler.add_job(test_flag, 'interval', args=arr, minutes=minutes)


def test_flag(client: FeatureFlagClient, default_value: FeatureFlagDefaultValue):
    flag = client.get_feature_flag(default_value.application_name, default_value.feature_name)
    if flag.feature_enabled != default_value.default_value:
        logger.error(incorrect_flag_state_message(),
                     default_value.feature_name, client.feature_flag_host, flag.feature_enabled)
        collectionLogs.insert_one(getTestFeatureFlagModel(client, default_value, False))
        client.set_feature_flag(
            default_value.application_name,
            default_value.feature_name,
            not flag.feature_enabled)
    logger.debug(correct_flag_state_message(),
                 default_value.feature_name, client.feature_flag_host, flag.feature_enabled)
    collectionLogs.insert_one(getTestFeatureFlagModel(client, default_value, True))

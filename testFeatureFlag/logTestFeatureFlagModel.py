from datetime import datetime
from featureFlagClient.featureFlagClient import FeatureFlagClient
from testFeatureFlag.featureFlagDefaultValue import FeatureFlagDefaultValue


def getTestFeatureFlagModel(client: FeatureFlagClient, default_value: FeatureFlagDefaultValue, correct: bool) -> {}:
    return {
        'date': datetime.utcnow(),
        'correct': correct,
        'feature_name': default_value.feature_name,
        'application_name': default_value.application_name,
        'grpc_host': client.feature_flag_host,
    }

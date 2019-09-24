from grpc import insecure_channel
from configuration import config
from configuration.config import grpc_host_services
from featureFlagClient.generated import FeatureFlagService_pb2 as featureFlagService
from featureFlagClient.generated.FeatureFlagService_pb2_grpc import FeatureFlagServiceStub


class FeatureFlagClient:
    def __init__(self, feature_flag_host: str = config.grpc_host_default):
        self.feature_flag_host = feature_flag_host
        feature_flag_channel = insecure_channel(self.feature_flag_host)
        self._feature_flag_stub: FeatureFlagServiceStub = FeatureFlagServiceStub(feature_flag_channel)

    def get_feature_flag(self, app_name: str, feature_name: str):
        request = featureFlagService.GetFeatureFlagRequest(
            station_external_id="",
            application_name=app_name,
            feature_name=feature_name
        )
        return self._feature_flag_stub.GetFeatureFlag(request)

    def set_feature_flag(self, app_name: str, feature_name: str, enabled: bool):
        request = featureFlagService.SetFeatureFlagRequest(
            station_external_id="",
            application_name=app_name,
            feature_name=feature_name,
            feature_enabled=enabled
        )
        response = self._feature_flag_stub.SetFeatureFlag(request)
        return response


def get_grpc_clients() -> [FeatureFlagClient]:
    hosts = grpc_host_services()
    clients = []
    for host in hosts:
        clients.append(FeatureFlagClient(feature_flag_host=host))
    return clients

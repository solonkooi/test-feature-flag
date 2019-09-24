class FeatureFlagModel:
    def __init__(self, feature_name: str, application_name: str, feature_enabled: bool):
        self.feature_name: str = feature_name
        self.application_name: str = application_name
        self.feature_enabled: bool = feature_enabled

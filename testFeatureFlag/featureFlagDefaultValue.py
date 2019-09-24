class FeatureFlagDefaultValue:
    def __init__(self, feature_name: str, application_name: str, default_value: bool):
        self.feature_name: str = feature_name
        self.application_name: str = application_name
        self.default_value: bool = default_value


def get_list_FeatureFlagDefaultValue() -> [FeatureFlagDefaultValue]:
    return [FeatureFlagDefaultValue('useNewSso', 'sso2', True),
            FeatureFlagDefaultValue('UserAccount_AGENCY_ASSIGNMENT', 'user-mgmt-web', False)]

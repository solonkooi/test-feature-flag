import logging
from logging import Logger

grpc_host_sales = 'featureflag-service-sales.tcp.qa1.qa.eks.videa.io:31380'
grpc_host_alpha = 'featureflag-service.tcp.alpha.qa.eks.videa.io:31380,keepalive=true'
grpc_host_default = 'featureflag-service-sales.tcp.qa1.qa.eks.videa.io:31380'

web_test_feature_flag_host = '0.0.0.0'
web_test_feature_flag_port: int = 5000
ping_time_minutes = 5


def grpc_host_services() -> [str]:
    return [grpc_host_sales]


def get_config_logger() -> Logger:
    logger = logging.getLogger("__main__")
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler('file.log')
    logger.addHandler(file_handler)
    return logger

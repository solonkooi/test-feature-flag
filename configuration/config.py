import logging
import os
from logging import Logger

grpc_host_sales = 'featureflag-service:31380'
grpc_host_alpha = 'featureflag-service:31380'
grpc_host_default = 'featureflag-service:31380'

web_test_feature_flag_host = '0.0.0.0'
web_test_feature_flag_port: int = 5001
ping_time_minutes = 5


def grpc_host_services() -> [str]:
    return [grpc_host_sales, grpc_host_alpha]


def get_config_logger() -> Logger:
    logger = logging.getLogger("__main__")
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler('file.log')
    logger.addHandler(file_handler)
    return logger


def get_mongodb_host() -> str:
    return os.getenv('DB_MONGO_URL', 'localhost')


def get_mongodb_port() -> int:
    return int(os.getenv('DB_MONGO_PORT', '27017'))

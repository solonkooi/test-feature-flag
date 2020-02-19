import atexit
import json
from apscheduler.schedulers.background import BackgroundScheduler
from bson import json_util
from flask import Flask, render_template, make_response, send_from_directory
from pymongo import MongoClient
from pytz import utc
from configuration.config import *
from featureFlagClient.featureFlagClient import get_grpc_clients
from featureFlagClient.featureFlagModel import FeatureFlagModel
from testFeatureFlag.featureFlagDefaultValue import get_list_FeatureFlagDefaultValue
from testFeatureFlag.testFeatureFlagScheduler import runBackgroundScheduler

app = Flask(__name__)
client = MongoClient(get_mongodb_host(), get_mongodb_port())
db = client['test-feature-flag']
collectionLogs = db['logs']
scheduler = BackgroundScheduler(timezone=utc)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path, 'favicon-ox.png')


@app.route('/', methods=['GET', 'POST'])
def index():
    clients = get_grpc_clients()
    default_values = get_list_FeatureFlagDefaultValue()
    feature_flags = []
    for clientFeatureFlag in clients:
        for defaultValue in default_values:
            response_service = clientFeatureFlag.get_feature_flag(defaultValue.application_name,
                                                                  defaultValue.feature_name)
            feature_flags.append(
                {
                    'app_host': clientFeatureFlag.feature_flag_host,
                    'flags': [
                        FeatureFlagModel(defaultValue.feature_name,
                                         defaultValue.application_name,
                                         response_service.feature_enabled),
                    ]
                }
            )
    return render_template('index.html', feature_flags=feature_flags)


@app.route('/logs')
def logs():
    pipeline = [
        {
            "$sort": {
                "date": -1
            }
        },
        {
            "$limit": 20
        },
        {
            "$project": {
                "date": {
                    "$dateToString": {
                        "date": "$date"
                    }
                },
                "correct": "$correct",
                "feature_name": "$feature_name",
                "application_name": "$application_name",
                "grpc_host": "$grpc_host"
            }
        }
    ]
    result = list(collectionLogs.aggregate(pipeline))
    _log_collection = json.dumps(result, default=json_util.default)
    return make_response(_log_collection, 200)


atexit.register(lambda: scheduler.shutdown(wait=False))

if __name__ == '__main__':
    testFeatureFlagScheduler = runBackgroundScheduler(scheduler, ping_time_minutes)
    scheduler.start()
    app.run(host=web_test_feature_flag_host, port=web_test_feature_flag_port, use_reloader=False)

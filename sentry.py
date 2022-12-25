from flask import Flask, request
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import logging


sentry_sdk.init(
    dsn="http://014010b17cc44e0aaa2ac2764169b6d3@127.0.0.1:9000/4",
    integrations=[FlaskIntegration()],
    # auto_enabling_integrations=False,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0


@app.route('/test_type')
def test_type():
    user_id = request.args.get('user_id')
    user_id = float(user_id)
    return str(user_id)


@app.route('/test')
def ll():
    raise IndexError


@app.route('/test_logging')
def test_logging():
    logging.error("error to log")
    return 'error'


if __name__ == '__main__':
    app.run()
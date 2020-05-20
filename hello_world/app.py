import json
import requests
import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

sentry_sdk.init(
    dsn="https://632ab7513da4474997fc1d70e962e961@o394662.ingest.sentry.io/5245069",
    integrations=[AwsLambdaIntegration()]
)


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
        sentry_sdk.capture_exception(
            Exception("This is an example of an error message #2."))
    except requests.RequestException as e:
        print(e)
        raise e

    response = {
        'statusCode': 200,
        'headers': {
            "Content-Type": "application/json"
        },
        'body': json.dumps({
            "message": "hello world again",
            "location": ip.text.replace("\n", "")
        })
    }
    return response

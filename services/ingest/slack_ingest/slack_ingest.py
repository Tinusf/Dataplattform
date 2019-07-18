import os
import urllib.request
import urllib.parse
import slack_signature_validator


def handler(event, context):
    slack_validator = slack_signature_validator.check_slack_event_legit(event)
    if not slack_validator["statusCode"] == 200:
        return slack_validator

    body = event["body"]
    response = post_to_ingest_api(body)
    return {
        'statusCode': response,
        'body': ""
    }


def post_to_ingest_api(body):
    ingest_url = os.getenv("DATAPLATTFORM_INGEST_URL")
    apikey = os.getenv("DATAPLATTFORM_INGEST_APIKEY")
    data = body.encode("ascii")
    try:
        request = urllib.request.Request(ingest_url, data=data, headers={"x-api-key": apikey})
        response = urllib.request.urlopen(request)
        return response.getcode()
    except urllib.request.HTTPError:
        return 500
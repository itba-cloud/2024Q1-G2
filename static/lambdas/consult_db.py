import json
import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
table_name = 'tweets-processed'

def lambda_handler(event, context):
    try:
        word = event['queryStringParameters']['word']

        if not word:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "The 'word' query parameter is required"})
            }

        table = dynamodb.Table(table_name)

        response = table.scan(
            FilterExpression=Attr('text').contains(word)
        )

        items = response.get('Items', [])

        return {
            "statusCode": 200,
            "body": json.dumps({"results": items})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

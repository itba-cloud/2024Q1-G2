import json
import boto3

dynamodb = boto3.resource('dynamodb')
source_table_name = 'tweets-raw'
destination_table_name = 'tweets-processed'


def lambda_handler(event, context):
    try:
        source_table = dynamodb.Table(source_table_name)

        tweets = json.loads(event['body'])

        for tweet in tweets:
            key = {'id': tweet['id'], 'subject': tweet['subject']}
            source_table.delete_item(Key=key)

        destination_table = dynamodb.Table(destination_table_name)

        for tweet in tweets:
            destination_table.put_item(Item=tweet)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Tweets added to the destination table"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


import json
import boto3

def lambda_handler(event, context):
 
    try:
    
        # Create DynamoDB resource
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(student)

        # Put the data into DynamoDB
        table.put_item(Item=event)

        response = {
            'statusCode': 200,
            'body': json.dumps('Data inserted successfully Tushar shrivastav Software engineer!')
        }

    except Exception as e:
        print(f"Error inserting data: {str(e)}")
        response = {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')  
        }

    return response
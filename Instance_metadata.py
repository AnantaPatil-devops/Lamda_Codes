import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    try:
        # Initialize Boto3 EC2 client
        ec2_client = boto3.client('ec2')

        # Get all EC2 instances
        response = ec2_client.describe_instances()

        # Initialize an empty list to store instance metadata
        instance_metadata_list = []

        # Iterate through reservations and instances to collect metadata
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_metadata = ec2_client.describe_instance_attribute(InstanceId=instance_id, Attribute='userData')
                instance_metadata_list.append(instance_metadata)

        # If no instances found, raise a custom exception
        if not instance_metadata_list:
            raise Exception("No EC2 instances found in the account.")

        # Convert metadata list to JSON format
        metadata_json = json.dumps(instance_metadata_list, indent=4)

        return {
            'statusCode': 200,
            'body': metadata_json
        }
    
    except ClientError as e:
        error_message = f"ClientError: {str(e)}"
        return {
            'statusCode': 500,
            'body': json.dumps({'error_message': error_message})
        }
    
    except Exception as e:
        error_message = str(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error_message': error_message})
        }

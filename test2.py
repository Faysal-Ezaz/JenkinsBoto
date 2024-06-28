import boto3
import os

# Create a session using environment variables
session = boto3.session.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
) # here, access keys will be fetched auto as ec2 instance has been granted full ec2 access via iam role. 

ec2 = session.resource('ec2')

image_id = os.getenv('IMAGE_ID')
instance_type = os.getenv('INSTANCE_TYPE')
count = int(os.getenv('COUNT'))
key_name = os.getenv('KEY_NAME')
security_group = os.getenv('SECURITY_GROUP')
instance_name = os.getenv('INSTANCE_NAME')  # Environment variable for the instance name

try:
    instances = ec2.create_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        MinCount=count,
        MaxCount=count,
        KeyName=key_name,
        SecurityGroupIds=[security_group], 
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': instance_name}]
        }]
    )

    print(f"Successfully created EC2 instance(s): {[instance.id for instance in instances]}")
except Exception as e:
    print(f"Error creating EC2 instance(s): {e}")
    # Consider logging the error for further investigation

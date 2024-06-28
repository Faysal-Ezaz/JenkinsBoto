import boto3
import os

# Create a session using environment variables
session = boto3.session.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name="ap-south-1"
)

ec2 = session.resource('ec2')

image_id = "ami-0f58b397bc5c1f2e8"
instance_type = 't2.micro'
count = 1
key_name = 'Work'
security_group = 'sg-0827fcdf7280d4731'

try:
    instances = ec2.create_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        MinCount=count,
        MaxCount=count,
        KeyName=key_name,
        SecurityGroupIds=[security_group]
    )

    print(f"Successfully created EC2 instance(s): {[instance.id for instance in instances]}")
except Exception as e:
    print(f"Error creating EC2 instance(s): {e}")
    # Consider logging the error for further investigation
    # Webhook test2

## The webhook didnot work when I commited changes to test2.py... this is to check exactly that. 

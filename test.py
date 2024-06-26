import boto3

def create_ec2_instance(ami_id, instance_type, security_group_id, key_name):
  """
  Creates an EC2 instance with the specified parameters.

  Args:
      ami_id (str): The ID of the Amazon Machine Image (AMI) to use.
      instance_type (str): The type of EC2 instance to create (e.g., t2.micro).
      security_group_id (str): The ID of the security group to associate with the instance.
      key_name (str): The name of the SSH key pair to use for access.
  """

  # Use session with credentials from instance profile (preferred)
  try:
    session = boto3.session.Session()
  except Exception as e:
    # If instance profile fails, fallback to shared credentials/env variables
    print(f"Failed to use instance profile credentials: {e}")
    session = boto3.session.Session()

  ec2_client = session.client('ec2')

  # Create the instance
  response = ec2_client.run_instances(
      ImageId=ami_id,
      InstanceType=instance_type,
      MinCount=1,
      MaxCount=1,
      SecurityGroupIds=[security_group_id],
      KeyName=key_name
  )

  # Return the instance ID
  return response['Instances'][0]['InstanceId']

# Example usage (replace with your actual values)
ami_id = "ami-xxxxxxxx"
instance_type = "t2.micro"
security_group_id = "sg-xxxxxxxx"
key_name = "your_key_pair"

instance_id = create_ec2_instance(ami_id, instance_type, security_group_id, key_name)

if instance_id:
  print(f"Successfully created EC2 instance with ID: {instance_id}")
else:
  print("Failed to create EC2 instance.")

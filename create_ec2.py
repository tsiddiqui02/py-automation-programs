import boto3

# Set Up EC2 Client
ec2 = boto3.client('ec2')

# Specify Instance Parameters
image_id = 'ami-INSERTAMI' 
instance_type = 't2.micro' 
key_name = 'INSERTKEYNAME' 
security_group_ids = ['sg-INSERTID'] 

# Launch EC2 Instance
response = ec2.run_instances(
    ImageId=image_id, 
    InstanceType=instance_type, 
    KeyName=key_name,
    SecurityGroupIds=security_group_ids, 
    MinCount=1, 
    MaxCount=1
)

# Get Instance ID from Response
instance_id = response['Instances'][0]['InstanceId']

# Wait for Instance to be Running
ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])

# Print Instance Information
instance = ec2.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]
print(f"Instance ID: {instance_id}")
print(f"Public IP Address: {instance.get('PublicIpAddress', 'N/A')}")
print(f"Private IP Address: {instance.get('PrivateIpAddress', 'N/A')}")
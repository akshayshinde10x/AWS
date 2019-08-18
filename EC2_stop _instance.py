import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
#print(response)

instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']

print(instance_id)

print(ec2.stop_instances(InstanceIds=[instance_id]))

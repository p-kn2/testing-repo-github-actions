import boto3

ec2_client = boto3.client(
    'ec2',
    region_name='ap-southeast-2'
)

ec2_client.describe_instances()
print('helo')
response = ec2_client.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Instance ID:", instance['InstanceId'])
        print("State:", instance['State']['Name'])
        print("Instance Type:", instance['InstanceType'])
        print("Private IP:", instance.get('PrivateIpAddress'))
        print("Public IP:", instance.get('PublicIpAddress'))
        print("-----------------------")



s3_client = boto3.client('s3')

response = s3_client.list_buckets()
 
for bucket in response['Buckets']:
  print(bucket['Name'])

# response = s3_client.create_bucket(Bucket = 'boto3-first-bckt33')
# print(response)

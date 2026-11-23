import boto3

s3_client = boto3.client('s3')

response = s3.list_buckets()
 
for bucket in response['Buckets']:
print(bucket['Name'])

// response = s3_client.create_bucket(Bucket = 'boto3-first-bckt33')
// print(response)

import boto3
client=boto3.client('ec2',region_name='us-east-1',aws_access_key_id='AKIAI4DHF5ESPYTBB5PQ',aws_secret_access_key='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')
vpc=client.describe_instances()
print(vpc)

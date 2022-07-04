from urllib import response
import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')
ec2_resource = boto3.resource('ec2', region_name='ap-south-1')

# response = ec2.describe_instances()
# response = list(ec2_resource.instances.all())
response = ec2_resource.Instance('i-0b019d739a0379003').private_ip_address
response1 = ec2_resource.Instance('i-0b019d739a0379003').root_device_name
response2 = ec2_resource.Instance('i-0b019d739a0379003').vpc_id
response3 = ec2_resource.Instance('i-0b019d739a0379003').block_device_mappings
print(response)
print(response1)
print(response2)
for each_item in response3:
    print(each_item['Ebs']['VolumeId'])
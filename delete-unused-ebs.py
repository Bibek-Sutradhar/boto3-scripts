import boto3

ec2_client = boto3.client('ec2', region_name='ap-south-1')
ec2_resource = boto3.resource('ec2', region_name='ap-south-1')

f_ebs_volume={"Name":"status", "Value":["available"]}

#resource
'''
resource = ec2_resource.volumes.filter(Filter=[f_ebs_volume])
for each_res in resource:
    print(each_res.id, each_res.state)
    each_res.delete()
'''
#Client
for each_item in ec2_client.describe_volumes()['Volumes']:
    print(each_item)
    print(each_item['VolumeId'], each_item['State'])
    if not "Tags" in each_item and each_item['State'] == 'available':
        ec2_client.delete_volume(VolumeId=each_item['VolumeId'])


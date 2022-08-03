import boto3
iam = boto3.client('iam')
#ec2 = boto3.client('ec2')


#vpcid = ec2.Vpc('id')
#print(vpcid)

for user in iam.list_users()['Users']:
 print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
 user['UserName'],
 user['UserId'],
 user['Arn'],
 user['CreateDate']
 )
 )

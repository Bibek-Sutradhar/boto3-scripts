import boto3

iam = boto3.client('iam')

created_user = iam.create_user(
    UserName='user1',
    Tags=[
        {
        'Key': 'Env',
        'Value': 'Test'
        }
    ]
)

print("The user created is:: " + created_user)
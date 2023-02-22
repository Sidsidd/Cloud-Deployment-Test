import boto3

ec2 = boto3.client('ec2')
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
subnet = ec2.create_subnet(VpcId=vpc['Vpc']['VpcId'], CidrBlock='10.0.1.0/24')
security_group = ec2.create_security_group(GroupName='MySecurityGroup',
                                            Description='My security group',
                                            VpcId=vpc['Vpc']['VpcId'])
instance = ec2.run_instances(ImageId='ami-0dfcb1ef8550277af',
                              InstanceType='t2.micro',
                              MaxCount=1,
                              MinCount=1,
                              KeyName='MyKeyPair',
                              NetworkInterfaces=[{'SubnetId': subnet['Subnet']['SubnetId'],
                                                   'DeviceIndex': 0,
                                                   'AssociatePublicIpAddress': True,
                                                   'Groups': [security_group['GroupId']]}])

print(instance)

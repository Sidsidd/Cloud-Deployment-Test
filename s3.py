import boto3
s3 = boto3.client('s3')
s3.create_bucket(Bucket='my-project-test-bucket')
s3.upload_file('index.html', 'my-project-test-bucket', 'index.html', ExtraArgs={'ContentType': 'text/html'})
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(instance['Instances'][0]['54.158.213.136'], username='Testproject', key_filename='project-test.pem')
stdin, stdout, stderr = ssh.exec_command('sudo apt-get update')
print(stdout.read().decode())

stdin, stdout, stderr = ssh.exec_command('sudo apt-get install -y nginx')
print(stdout.read().decode())


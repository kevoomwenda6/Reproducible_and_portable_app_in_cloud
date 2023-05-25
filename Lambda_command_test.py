import json
import boto3
import time
import sys
import os

credentials = ["us-west-2","",""]   #region,access_key,secret_key
InstanceId = 'i-057f2ed85a95a0383' #insert your EC2 instance ID
secret_key = ""
access_key = ""
region ="us-west-2"

def send_command_to_master(InstanceId, command, ssm_client):
    print("Ssm run command: ", command)
    response = ssm_client.send_command(
        InstanceIds=[InstanceId],
        DocumentName="AWS-RunShellScript",
        Parameters={'commands': [command]}
    )

def check_instance_availability(ec2_client, instance_id):
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    instance_state = response['Reservations'][0]['Instances'][0]['State']['Name']
    return instance_state == 'running'

def start_instance(ec2_client, instance_id):
    ec2_client.start_instances(InstanceIds=[instance_id])
    print('Starting instance...')
    while not check_instance_availability(ec2_client, instance_id):
        print('Waiting for instance to start...')
        time.sleep(10)
    print('Instance is now running.')

def main():
    ssm_client = boto3.client('ssm',region_name=credentials[0],aws_access_key_id=credentials[1],aws_secret_access_key=credentials[2])
    ec2_client = boto3.client('ec2',region_name=credentials[0],aws_access_key_id=credentials[1],aws_secret_access_key=credentials[2])
    
    if not check_instance_availability(ec2_client, InstanceId):
        start_instance(ec2_client, InstanceId)
    
    send_command_to_master(InstanceId, "curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh", ssm_client)
    send_command_to_master(InstanceId, "sudo service docker start && sudo usermod -a -G docker ubuntu && sudo chmod 666 /var/run/docker.sock && sudo apt install unzip", ssm_client)

    print('Action Completed!  Please check your S3 Bucket ai-4-atmosphere-remote-sensing/collocation-output for the results')
    
if __name__ == "__main__":
    main()


#def get_ec2_instances_id(region,access_key,secret_key):
#    ec2_conn = boto3.resource('ec2',region_name=region,aws_access_key_id=access_key,aws_secret_access_key=secret_key)
    
#    if ec2_conn:
#        for instance in ec2_conn.instances.all():
#            if instance.state['Name'] == 'running' and instance.security_groups[0]['GroupName'] == 'distributed_dl_starly': #insert your security group (i.e. 'default')
#                masterInstanceId = instance.instance_id
#                print("Master Instance Id is ",masterInstanceId)
#        return masterInstanceId
#    else:
#        print('Region failed', region)
#        return None

#def send_command_to_master(InstanceId,command,ssm_client):
#    print("Ssm run command: ",command)
#    response = ssm_client.send_command(InstanceIds=[InstanceId],DocumentName="AWS-RunShellScript",Parameters={'commands': [command]})

#def lambda_handler(event, context):
#    masterInstanceId = InstanceId 
#    ssm_client = boto3.client('ssm',region_name=credentials[0],aws_access_key_id=credentials[1],aws_secret_access_key=credentials[2])
#    send_command_to_master(masterInstanceId,\
#        "curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh",\
#        ssm_client)
    
#    send_command_to_master(masterInstanceId,\
##        "sudo service docker start && sudo usermod -a -G docker ubuntu && sudo chmod 666 /var/run/docker.sock && sudo apt install unzip",\
 #       ssm_client)
#    send_command_to_master(masterInstanceId,\
#        "docker run -v /home/ubuntu/cloud-phase-prediction-main:/root/CloudPhasePrediction -v /home/ubuntu/output_data :/root/output_data  rohansalvi98/cloudphaseprediction sh -c 'cd CloudPhasePrediction && python train.py --training_data_path='./example/training_data/'  --model_saving_path='/root/output_data'' | tee -a /home/ubuntu/result.txt",\
#        ssm_client)
    
#    print('done')
        
#    return {
#        'statusCode': 200,
#        'body': json.dumps('Action Completed!  Please check your S3 Bucket ai-4-atmosphere-remote-sensing/collocation-output for the resutls')
#   }
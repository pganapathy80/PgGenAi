#test app
import boto3
session = boto3.Session(profile_name='796202783574_PGAdministratorAccess')
bedrock = boto3.client(
    service_name="bedrock" ,
    region_name="us-east-1" ,
    
)
#print list of models
print(bedrock.list_foundation_models())
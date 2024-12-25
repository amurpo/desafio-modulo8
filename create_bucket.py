import boto3
import os
import json
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region):
    s3_client = boto3.client('s3', region_name=region)
    try:
        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )
        print(f"✓ Bucket {bucket_name} created successfully in region {region}")
    except ClientError as e:
        print(f"✕ Error creating bucket: {e}")
        raise

def set_bucket_policy(bucket_name, s3_user):
    # Define the bucket policy
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AllowSpecificUserOnly",
                "Effect": "Allow",
                "Principal": {
                    "AWS": s3_user  # ARN del usuario S3 desde la variable de entorno
                },
                "Action": ["s3:PutObject", "s3:GetObject"],
                "Resource": [f"arn:aws:s3:::{bucket_name}/*"]
            }
        ]
    }

    # Convertir el diccionario a JSON
    policy_json = json.dumps(bucket_policy)

    s3_client = boto3.client('s3')
    try:
        s3_client.put_bucket_policy(Bucket=bucket_name, Policy=policy_json)
        print(f"✓ Bucket policy set for {bucket_name}")
    except ClientError as e:
        print(f"✕ Error setting bucket policy: {e}")
        raise

def main():
    # Cargar variables de entorno
    bucket_name = os.environ.get('S3_BUCKET_NAME')
    s3_user = os.environ.get('S3_USER')  # ARN del usuario S3
    region = os.environ.get('AWS_REGION')

    # Validar que las variables de entorno necesarias estén presentes
    if not bucket_name or not s3_user or not region:
        raise ValueError("S3_BUCKET_NAME, S3_USER, and AWS_REGION environment variables are required")

    # Crear el bucket y establecer la política
    create_bucket(bucket_name, region)
    set_bucket_policy(bucket_name, s3_user)

if __name__ == "__main__":
    main()

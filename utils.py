
import boto3
import json
from botocore.exceptions import ClientError
from typing import Dict # used for type hints



class Utils:
    
    #  Returns the value a given secret stored in AWS Secrets Manager
    def get_secret(self, secret_name: str, region_name: str = "us-east-1") -> Dict:
        """
        Returns the value of a given secret.

        Args:
            secret_name (string): The name of the secret as it was defined in AWS Secrets Manager.
            region_name (string)(optional): The name of the scret region defaults to us-east-1 if none given

        Returns:
            dictionary: The secret's value parsed to a dictionary object
        """

        # Create a Secrets Manager client
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            # For a list of exceptions thrown, see
            # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
            raise e

        # Decrypts secret using the associated KMS key.
        secret = get_secret_value_response['SecretString']

        # Converts string to json/dict and returns it
        return json.loads(secret)



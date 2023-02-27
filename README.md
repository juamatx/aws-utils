# aws-utils

This is a utility class with independent functions. The purpose of this class is reusability to avoid re-writting common aws code.

*Note: Each function assummes proper IAM permission. Make sure to provide all necessary permissions*

# Functions:

get_secret(): returns the value of a given secret name stored in AWS Secrets Manager


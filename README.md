Title: AWS Event triggered Project with Lambda function + DynamoDB + S3

Project1: Lambda + S3 + DynamoDB

Steps:

1.Create Lambda function, S3 bucket, DynamoDB Table

2.Give S3 and DynamoDB permissions to Lambda function

  The lambda function will have a default role, on the default role we need to add IAM role policies for S3 and DynamoDB

3.Add Trigger from S3

Result: 
If we make any modification in the S3 bucket(add/update/delete) that data will be modified to dict format(format DynamoDB accepts) and updated in the DynamoDB Table

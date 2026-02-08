Title: AWS EDA with Lambda & Event Bridge

Project1: Lambda + S3 + DynamoDB

Steps:
1.Create Lambda function, S3 bucket, DynamoDB Table
a)Lambda function
![Uploading image.png…]()

b)S3 Bucket

c)DynamoDB table

2.Give S3 and DynamoDB permissions to Lambda function
The lambda function has a default role: 




have to add IAM role policies:


3.Add Trigger



Result: 
If we make any modification in the S3 bucket(add/update/delete) that data will be modified to dict format(format DynamoDB accepts) and updated in the DynamoDB Table

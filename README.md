# AWS Event-Driven Project using Lambda, S3, and DynamoDB

## Overview
This project demonstrates a **basic event-driven architecture on AWS** using **Amazon S3**, **AWS Lambda**, and **Amazon DynamoDB**.  
The system reacts automatically to file-level events in an S3 bucket and synchronizes structured data into a DynamoDB table.

The primary objective of this project is to understand how **AWS Lambda can be triggered by S3 events** and how data flows across AWS services without managing servers.

---

## Architecture Summary
- **Amazon S3** acts as the event source  
- **AWS Lambda** acts as the event processor  
- **Amazon DynamoDB** acts as the persistent data store  

Whenever a file is **created, updated, or deleted** in the S3 bucket, the Lambda function is triggered automatically.

---

## Services Used
- AWS Lambda  
- Amazon S3  
- Amazon DynamoDB  
- AWS Identity and Access Management (IAM)  
- Boto3 (AWS SDK for Python)

---

## Project Flow
1. A JSON file is uploaded or modified in the S3 bucket  
2. S3 generates an event notification  
3. The event triggers the Lambda function  
4. Lambda reads the file content from S3  
5. Data is converted from bytes to string and then to dictionary format  
6. The processed data is stored in DynamoDB  

---

## Setup Instructions

### Step 1: Create AWS Resources
- Create an **S3 bucket**
- Create a **DynamoDB table**
- Create a **Lambda function** using the Python runtime

---

### Step 2: Configure IAM Permissions
The Lambda function uses a **default execution role**.  
Attach the following IAM permissions to the role:
- Read access to the S3 bucket  
- Write access to the DynamoDB table  

This allows the Lambda function to securely interact with both services.

---

### Step 3: Configure S3 Trigger
- Add S3 bucket as Trigger
- Trigger types: `All Modifications`  
- Target service: AWS Lambda  

This ensures the Lambda function is invoked whenever the bucket content changes.

---

## Lambda Function Logic
The Lambda function performs the following operations:
- Retrieves the uploaded JSON file from S3  
- Reads streaming data returned by S3  
- Decodes byte data using UTF-8 encoding  
- Converts the JSON string into a dictionary  
- Inserts the processed data into DynamoDB  

> The Lambda implementation is available in the `lambda_function.py` file.

---

## Key Concepts Demonstrated
- Event-driven architecture  
- Serverless computing  
- AWS service integration  
- Data format transformation  
- IAM-based access control  

---

## Possible Enhancements
- Handle dynamic file names using S3 event metadata  
- Add structured logging and error handling  
- Validate DynamoDB primary keys before insertion  
- Introduce retry mechanisms and Dead Letter Queues (DLQ)  
- Track processing status for better observability  

---

## Conclusion
This project provides a practical introduction to **AWS event-driven workflows** and **serverless architecture**.  
It demonstrates how loosely coupled AWS services can be combined to build scalable and automated systems.

---

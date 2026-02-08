import json
import boto3
client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    response = client.get_object(
        Bucket='438465149928-project1-s3bucket',
        Key='DynamoDB_Samplefile.json',     
)
# convert from streaming data to byte
    json_data = response['Body'].read() #initially data is in byte format(streaming data) and we need to convert it to string format
    print(json_data)
    print(type(json_data))
    #convert data from byte to string
    data_string = json_data.decode('UTF-8') #decode method is used to convert byte data to string data and we need to specify the encoding type which is UTF-8 in this case
    print(data_string)
    print(type(data_string))
    # convert from json string to dictionary
    data_dict =json.loads(data_string) #json.loads() method is used to convert json string to dictionary
    print(data_dict)
    print(type(data_dict))
    
    #insert data to dynamodb
    table = dynamodb.Table('DynamoDB_Samplefile.json')
    table.put_item(Item=data_dict)
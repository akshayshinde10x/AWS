import boto3
# Create a table called Employee
 
dynamodb = boto3.resource('dynamodb', region_name='ap-east-1')
mytable = dynamodb.create_table(TableName= 'Employee', 
KeySchema=[{
	'KeyType': 'HASH',
	'AttributeName': 'Id'},
{
'KeyType': 'RANGE',
'AttributeName': 'Sal'
}
],
AttributeDefinitions=[
{
'AttributeName': 'Id',
'AttributeType': 'N'
},
{
'AttributeName': 'Sal',
'AttributeType': 'N'
}
],
ProvisionedThroughput={
'ReadCapacityUnits': 2,
'WriteCapacityUnits': 2
}
)
# Wait until the table exists.
mytable.meta.client.get_waiter('table_exists').wait(TableName='Employee')
print('Table is ready, please continue to isert data.')
 
# Insert the data into dynamodb table
mytable.put_item(Item={
	'Id': 1,
	'FirstName': 'Akshay',
	'LastName': 'Kumar',
	'Dept': 'Finance',
	'Sal': 1000
	})
mytable.put_item(Item={
	'Id': 1,
	'FirstName': 'Animesh',
	'LastName': 'Dev',
	'Dept': 'IT',
	'Sal': 2000
	})
mytable.put_item(Item={
	'Id': 1,
	'FirstName': 'Nagesh',
	'LastName': 'Shah',
	'Dept': 'Support',
	'Sal': 11000
	})
mytable.put_item(Item={
	'Id': 1,
	'FirstName': 'Suresh',
	'LastName': 'Deep',
	'Dept': 'Finance',
	'Sal': 12000
	})
 
response = mytable.scan()
 
for i in response['Items']:
	print("added item:", i['Id'], ":", i['FirstName'], ":", i['LastName'], ":", i['Dept'], ":", i['Sal'])
import boto3
rds= boto3.client('rds')

try:
	dbs= rds.describe_db_instances()
	for db in dbs['DBInstances']:
		print(db['MasterUsername'])
		print(db['Endpoint']['Address'])
		print(db['Endpoint']['Port'])
		print(db['DBInstanceStatus'])

except Exception as e:
	print(e)
	
	
# response = rds.create_db_instance(
	# DBInstanceIdentifier = 'newDB',
	# MasterUsername = 'akshay',
	# MasterUserPassword = 'akshay1234',
	# DBInstanceClass = 'db.t2.micro',
	# Engine = 'mysql',
	# AllocatedStorage = 5)
	
# print(response)

# response = rds.delete_db_instance(
	# DBInstanceIdentifier = 'database-1',
	# SkipFinalSnapshot = True)
# print(response)
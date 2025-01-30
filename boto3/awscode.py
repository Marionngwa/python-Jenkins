import boto3

# Initialize EC2 client
ec2 = boto3.client("ec2", region_name="us-east-1")

# Define filters correctly
filters = [
    {
        "Name": "tag:Environment",  
        "Values": ["dev"]
    }
]

# Fetch instances with the filter
response = ec2.describe_instances(Filters=filters)

# Extract instance IDs
instance_list = []
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_list.append(instance["InstanceId"])

# Print the list of instance IDs
print(instance_list)

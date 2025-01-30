#creating an s3 bucket and uploading a file to that bucket. 
import boto3

# Initialize S3 client, and create a bucket
client = boto3.client('s3')
client.delete_bucket(Bucket='123-test-boto-bucket')
# client.create_bucket(Bucket= '123-test-boto-bucket')

# #create a file and upload it to an s3 bucket
# # with open('myfile.tx', 'w') as file:
# #     file.write('this bucket was created with boto3')

# client.upload_file(Filename='myfile.tx', 
#                    Bucket='123-test-boto-bucket', 
#                    Key='testing-upload')

# #Download the file from the s3 bucket 
# client.download_file(Bucket='123-test-boto-bucket', 
#                      Key='testing-upload',
#                      Filename='my_local_download.txt')

# with open('my_local_download.txt','r') as file:
#     print(file.read())

# #Deleting the object
# client.delete_object(Bucket='123-test-boto-bucket',
#                      Key='testing-upload',)


#using Resource
#s3 = boto3.resource('s3')
#print(list(s3.buckets.all()))

#bucket = s3.Bucket('123-test-boto-bucket')
#bucket.upload_file(Filename='myfile.tx', Key='another_upload')
#print(list(bucket.objects.all()))
#print(bucket.objects.all().delete())

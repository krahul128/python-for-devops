import boto3           

# tried this way also but it is taking more time to load To be frank I have wrote this code in first then get to know it is more effective 
#s3 = boto3.client("s3")

#response = s3.list_buckets()    


#for item in response["Buckets"]:
   # for key, value in item.items():
     #   if key == "Name":
        #    print(value)
                       
s3 = boto3.client("s3")


response = s3.list_buckets()    

#print(response["Buckets"])

for bucket in response["Buckets"]:
    print(bucket["Name"])   



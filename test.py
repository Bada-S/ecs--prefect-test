import boto3

s3client = boto3.client("s3")
s3 = boto3.resource("s3")

bucket_name = "coiled-prefect"
bucket = s3.Bucket(bucket_name)

for obj in bucket.objects.all():
    filename = obj.key.rsplit("/")[-1]
    s3client.download_file(bucket_name, obj.key, "/txt/" + filename)

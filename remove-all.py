import boto3, os

s3 = boto3.client('s3')

args = {"Bucket": os.environ['BUCKET'],"MaxKeys": 1000 }
next_token = False
while next_token != None:
  if next_token:
    args.update({'ContinuationToken': next_token})
  res= s3.list_objects_v2(**args)
  print "Deleting %s objects %s..%s" % ( len(res['Contents']), res['Contents'][0:1][0]['Key'], res['Contents'][:-1][0]['Key'])
  delres = s3.delete_objects(Bucket=os.environ['BUCKET'],Delete=dict(Objects=map(lambda obj: {"Key": obj['Key']}, res['Contents'])))
  print "%s objects deleted, %s errors" % (len(delres['Deleted']), len(delres.get('Errors',[])))
  next_token =res.get('NextContinuationToken', None)

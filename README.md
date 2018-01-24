# s3-boto3-remove-all
remove all objects in s3 bucket specified as env BUCKET to make.  Runs in docker.  Needless to say, this is quite destructive!

This is actually really slow.  Not because of the python, because there's a maximum speed at which deletes can be issued.  
Once you get into the high tens or hundreds of thousands of items, you may be rate limited, making the speed at which you can 
accomplish bucket cleanup untenable.

An alternative is to adjust the bucket retention policy to a very small amount of time so that the bucket can expire all your 
objects for you.  It takes some time, maybe even 24 hours, for it to happen, but it can clear your bucket for you.

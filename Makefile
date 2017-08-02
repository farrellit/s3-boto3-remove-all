run:
	docker run -e BUCKET --rm -it -v `pwd`:/code boto3 python /code/remove-all.py

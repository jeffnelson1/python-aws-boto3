import boto3
import sys


def main():
    creates3bucket()

def creates3bucket():
    client = boto3.client('s3')
    names = ["netest01", "netest02"]
    for i in names:
        
        create = client.create_bucket(
        ACL='private',
        Bucket=i,
        )

        print(create)


if __name__ == '__main__':
    main()
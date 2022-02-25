import boto3
import sys


def main():
    create_rds_instance()

def create_rds_instance():
    client = boto3.client('rds')

    create = client.create_db_instance(
        DBName='db01-test',
        DBInstanceIdentifier='db-boto3-test-01',
        AllocatedStorage=10,
        DBInstanceClass='db.t2.micro',
        Engine='mysql',
        MasterUsername='admin',
        MasterUserPassword='addPassword',
    )

    print(create)


if __name__ == '__main__':
    main()
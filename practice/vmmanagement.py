from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

from cloudmesh.management.configuration.config import Config

config = Config()

EC2_ACCESS_ID = config['cloudmesh.cloud.aws.credentials.EC2_ACCESS_ID']
EC2_SECRET_KEY = config['cloudmesh.cloud.aws.credentials.EC2_SECRET_KEY']


EC2Driver = get_driver(Provider.EC2)
conn = EC2Driver(EC2_ACCESS_ID, EC2_SECRET_KEY)



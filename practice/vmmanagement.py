from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

import pprint

from cloudmesh.management.configuration.config import Config

config = Config()

EC2_ACCESS_ID = config['cloudmesh.cloud.aws.credentials.EC2_ACCESS_ID']
EC2_SECRET_KEY = config['cloudmesh.cloud.aws.credentials.EC2_SECRET_KEY']


EC2Driver = get_driver(Provider.EC2)
conn = EC2Driver(EC2_ACCESS_ID, EC2_SECRET_KEY)


# retrieve available images and sizes
images = conn.list_images()
#for image in images:
#    pprint.pprint(image)

sizes = conn.list_sizes()

# create node with first image and first size
#node = conn.create_node(name='yourservername', image=images[0], size=sizes[0])


nodes = conn.list_nodes()
for node in nodes:
    pprint.pprint(node)





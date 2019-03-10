from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver


import pprint

from cloudmesh.management.configuration.config import Config

from practice.vmmanagement import VMManager

config = Config()

EC2_ACCESS_ID = config['cloudmesh.cloud.aws.credentials.EC2_ACCESS_ID']
EC2_SECRET_KEY = config['cloudmesh.cloud.aws.credentials.EC2_SECRET_KEY']
IMAGE_ID = config['cloudmesh.cloud.aws.default.image']
SIZE_ID = config['cloudmesh.cloud.aws.default.size']
REGION = config['cloudmesh.cloud.aws.credentials.region']
ACCESS_KEY_NAME = config['cloudmesh.cloud.aws.credentials.EC2_PRIVATE_KEY_FILE_NAME']
SECURITY_GROUP_NAMES = []
SECURITY_GROUP_NAMES.append(config['cloudmesh.cloud.aws.credentials.EC2_SECURITY_GROUP'])

EC2Driver = get_driver(Provider.EC2)
conn = EC2Driver(EC2_ACCESS_ID, EC2_SECRET_KEY, region=REGION)

nodes = conn.list_nodes()
for node in nodes:
    pprint.pprint(node)

vmmanager = VMManager(conn)

if len(nodes) == 0:
    node = vmmanager.create_node("iu-cloudcomputing-test1", IMAGE_ID, SIZE_ID,ACCESS_KEY_NAME, SECURITY_GROUP_NAMES)
else:
    node = nodes[0]

if(node.state.lower() != "running"):
    conn.ex_start(node=node)

#conn.ex_stop(node=node)

conn.destroy_node(node)







del conn







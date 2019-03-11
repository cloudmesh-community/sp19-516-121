from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver


import pprint
import time

from cloudmesh.management.configuration.config import Config

config = Config()


AZURE_SECRET_KEY = config['cloudmesh.cloud.azure.credentials.AZURE_SECRET_KEY']
AZURE_TENANT_ID = config['cloudmesh.cloud.azure.credentials.AZURE_TENANT_ID']
AZURE_SUBSCRIPTION_ID = config['cloudmesh.cloud.azure.credentials.AZURE_SUBSCRIPTION_ID']
AZURE_APPLICATION_ID = config['cloudmesh.cloud.azure.credentials.AZURE_APPLICATION_ID']


AZUREARMDriver = get_driver(Provider.AZURE_ARM)
conn = AZUREARMDriver(tenant_id=AZURE_TENANT_ID,
             subscription_id=AZURE_SUBSCRIPTION_ID,
             key=AZURE_APPLICATION_ID, secret=AZURE_SECRET_KEY)

nodes = conn.list_nodes()
for node in nodes:
    pprint.pprint(node)

time.sleep(10)

if len(nodes) > 0:
    node = nodes[0]
    if node.state.lower() == 'stopped':
        conn.ex_start_node(node)
    elif node.state.lower() == 'running':
        conn.ex_stop_node(node)


nodes = conn.list_nodes()
for node in nodes:
    pprint.pprint(node)






del conn







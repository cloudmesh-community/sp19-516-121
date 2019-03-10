from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver


import pprint

from cloudmesh.management.configuration.config import Config

config = Config()

EC2_ACCESS_ID = config['cloudmesh.cloud.aws.credentials.EC2_ACCESS_ID']
EC2_SECRET_KEY = config['cloudmesh.cloud.aws.credentials.EC2_SECRET_KEY']
IMAGE_ID = config['cloudmesh.cloud.aws.default.image']
SIZE_ID = config['cloudmesh.cloud.aws.default.size']
REGION = config['cloudmesh.cloud.aws.credentials.region']


EC2Driver = get_driver(Provider.AZURE)
conn = EC2Driver(EC2_ACCESS_ID, EC2_SECRET_KEY)


# retrieve available images and sizes
imagesfile = open("aws-images.txt", "w")
sizesfile = open("aws-sizes.txt", "w")

images = conn.list_images()
for image in images:
   imagesfile.write("\n", repr(image))

sizes = conn.list_sizes()
for size in sizes:
  sizesfile.write("\n", repr(size))

imagesfile.close()
sizesfile.close()

size = [s for s in sizes if s.id == SIZE_ID][0]
image = [i for i in images if i.id == IMAGE_ID][0]

# create node with first image and first size
#node = conn.create_node(name='yourservername', image=images[0], size=sizes[0])


nodes = conn.list_nodes()
for node in nodes:
    pprint.pprint(node)


del conn







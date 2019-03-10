import pprint

from cloudmesh.management.configuration.config import Config


class VMManager:
    def __init__(self, driver):
        self.driver = driver

    def create_node(self, node_name, image_id, size_id, access_key_name, security_group_names):
        images = self.driver.list_images()
        sizes = sizes = self.driver.list_sizes()
        size = [s for s in sizes if s.id == size_id][0]
        image = [i for i in images if i.id == image_id][0]
        node = self.driver.create_node(name=node_name, image=image, size=size,
                                       ex_keyname=access_key_name, ex_securitygroup=security_group_names)
        return node

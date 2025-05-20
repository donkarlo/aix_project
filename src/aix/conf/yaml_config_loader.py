import yaml
from yaml import CLoader
from utilityx.conf.file_config_loader import FileConfigLoader


class YamlConfigLoader(FileConfigLoader):
    def _do_init_props(self)->None:
        '''implemented'''
        file_path = self.get_os_path().get_native_os_path()
        with open(file_path, "r") as file:
            self._props:dict = yaml.load(file, Loader=CLoader)
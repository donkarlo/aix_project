from abc import ABC,abstractmethod
from typing import Union
from utilityx.osx.os_path import OsPath


class FileConfigLoader(ABC):
    '''
       This is to load configs files. Currently it works only for yaml files
       @todo: does the path exists?
       @todo: is it the path to a yaml or json or csv etc file? use the right loader for each case
       '''
    _instance = None
    def __new__(cls, *args, **kwargs):
        '''Defines how __init__ should behave'''
        if cls._instance is None:
            cls._instance = super(FileConfigLoader,cls).__new__(cls)
        return cls._instance

    def __init__(self, os_path:OsPath):
        '''
        to load the configs
        :param os_path:
        '''
        self._os_path = os_path

        #init
        self._props = None
        self._do_init_props()

    @abstractmethod
    def _do_init_props(self):
        pass

    def get_prop(self, key:Union[list, str]):
        '''
        get just one property
        :param key: can be a str or a list ['level1','level2',...] in first case this method retrns
        self._props[str] and in the second case self._props['level1']['level2']...
        :return:
        '''
        result = None
        if isinstance(key,str):
            result = self._props[key]
        elif isinstance(key,list):
            result = self._props
            for index in key:
                # Check if the current key exists in the dictionary
                if index in result:
                    # Update result to the value corresponding to the current key
                    result = result[index]
                else:
                    raise KeyError(key)
        return result

    def get_props(self):
        '''
        get all properties
        :return:
        '''
        return self._props

    def get_os_path(self)->OsPath:
        return self._os_path

    def __call__(self, key:Union[list, str]=None):
        '''
        :param key: if the key is none then all _props are returned, if it is a flat list then the related subtree is returned if it is str then the first level node is returned
        :return:
        '''
        if isinstance(key,None):
            return self._props
        elif isinstance(key,str):
            return self.get_prop(key)

    def __getitem__(self, key):
        '''
        :param key:
        :return:
        '''
        return self._props[key]
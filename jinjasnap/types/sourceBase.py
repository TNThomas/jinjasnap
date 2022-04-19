from abc import ABCMeta, abstractclassmethod, abstractmethod
from io import TextIOWrapper
from jinjasnap.types import BundleTypes


class SourceBase(metaclass=ABCMeta):

    @property
    @abstractmethod()
    def ext():
        raise NotImplementedError

    @property
    @abstractmethod()
    def bundle_type():
        raise NotImplementedError

    @abstractclassmethod()
    def bundle(cls, src: str, dst: TextIOWrapper):
        raise NotImplementedError
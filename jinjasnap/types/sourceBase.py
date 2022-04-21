from abc import ABCMeta, abstractclassmethod, abstractmethod, abstractstaticmethod
from fileinput import filename
from io import TextIOWrapper
from jinjasnap.types import BundleTypes


class SourceBase(metaclass=ABCMeta):

    @property
    @abstractmethod()
    def bundle_type():
        raise NotImplementedError
        
    @classmethod()
    def generate_tag(cls, infile: str, outdir: str):
        # file name without path or extension
        infile_name: str = infile.split("/")[-1].split(".")[0]
        outfile: str = f"{outdir}/{infile_name}.{cls.bundle_type}"
        if cls.bundle_type == BundleTypes.SCRIPT:
            return f'<script src="{outfile}" type="application/javascript"></script>'
        elif cls.bundle_type == BundleTypes.STYLE:
            return f'<link rel="stylesheet" href="{outfile}">'
        else:
            return NotImplementedError

    @abstractstaticmethod()
    def bundle(cls, src: str, dst: str, overwrite: bool):
        raise NotImplementedError
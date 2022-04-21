import os
import shutil
from jinjasnap.types import BundleTypes
from jinjasnap.types.sourceBase import SourceBase


class JSSource(SourceBase):

    @property
    def bundle_type():
        return BundleTypes.SCRIPT

    @staticmethod
    def bundle(cls, src: str, dst: str, overwrite: bool):
        if overwrite:
            if os.pathexists(dst):
                os.remove(dst)
            shutil.copy(src, dst)
        else:
            with open(dst, mode="a") as dst_file:
                with open(src, mode="r") as src_file:
                    for line in src_file:
                        dst_file.write(line)
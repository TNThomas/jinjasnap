from jinjasnap.types import BundleTypes
from jinjasnap.types.sourceBase import SourceBase


class JSSource(SourceBase):
    @property
    def ext():
        return "js"

    @property
    def bundle_type():
        return BundleTypes.SCRIPT
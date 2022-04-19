from jinjasnap.types import BundleTypes
from jinjasnap.types.sourceBase import SourceBase


class CSSSource(SourceBase):
    @property
    def ext():
        return "css"

    @property
    def bundle_type():
        return BundleTypes.STYLE
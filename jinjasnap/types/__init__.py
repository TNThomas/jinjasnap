from enum import Enum, unique

from jinjasnap.types.cssSource import CSSSource
from jinjasnap.types.jsSource import JSSource
from jinjasnap.types.sourceBase import SourceBase

@unique()
class BundleTypes(Enum):
    SCRIPT = "js"
    STYLE = "css"

class SourceTypes(Enum):
    CSS = CSSSource
    JS = JSSource
    # LESS = LessSource()
    # SCSS = SassSource()
    # TS = TSSource()
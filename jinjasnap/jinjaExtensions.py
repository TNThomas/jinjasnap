from typing import List
from jinja2 import TemplateSyntaxError, nodes
from jinja2.ext import Extension
from jinja2.runtime import Context

from jinjasnap.types import SourceTypes, SourceBase


class AssetBundleExtension(Extension):
    """
    Allows asset bundles (e.g. CSS or JS) to be defined in Jinja2 templates.
    """

    # a set of names that trigger the extension.
    tags = {"bundle"}

    def __init__(self, environment):
        super().__init__(environment)

        # add the defaults to the environment
        environment.extend(dist_directory="/dist")

    def parse(self, parser) -> List[nodes.Node]:
        """
        Called when the `{% bundle %}` tag is read in a template
        """

        # Get the current line number
        lineno: int = next(parser.stream).lineno
 
        # Get the first argument of our custom 'bundle' tag, a file path
        args = [parser.parse_expression()]

        file_ext: str = args[0].split('.')[-1]
        src_type: SourceBase = SourceTypes[file_ext.upper()]

        # Get the second argument if it exists, an output file for the bundle
        if parser.stream.skip_if("comma"):
            args.append(parser.parse_expression())
        else:
            args.append(None)

        context: Context = nodes.ContextReference()

        # Get the output location for this file type from earlier in the document, if one is already declared
        bundle_ctx = context.get(f"{src_type.bundle_type}_LOC", None)

        result: List[nodes.Node] = []
        is_new_output: bool = False
        if not bundle_ctx:
            # No output location was declared before
            if not args[1]:
                # No output location is declared now
                raise TemplateSyntaxError(f"No output {src_type.bundle_type} file specified and none available in context.", lineno)
            else:
                # This is the first declaration of an output location for this bundlable type.
                is_new_output = True
                # Assign output file for our use now
                bundle_ctx = args[1]
                # nodes.Assign output file so we have it in the context next time we hit a {% bundle %}
                result.extend([
                    nodes.Assign(f"{src_type.bundle_type}_LOC", bundle_ctx),
                    nodes.Const(src_type.generate_tag(args[0], bundle_ctx))
                ])

        else:
            # We have to return a Node, so let's make sure it doesn't mess up the template.
            result = nodes.Const("")
        src_type.bundle(src=args[0], dst=bundle_ctx, overwrite=is_new_output)
        return result

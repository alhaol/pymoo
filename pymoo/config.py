from os.path import dirname, realpath

from pymoo.version import __version__


class Config:
    """
    The configuration of this package in general providing the place
    for declaring global variables.
    """

    # the root directory where the package is located at
    root = dirname(realpath(__file__))

    # whether a warning should be printed if compiled modules are not available
    show_compile_hint = True

    # whether when import a file the doc should be parsed - only activate when creating doc files
    parse_custom_docs = False

    @classmethod
    def data(cls):
        return "http://release.pymoo.org/_static/data/"

        # repo = "master"
        # if 'rc' in __version__:
        #     repo = 'release'
        # elif 'dev' in __version__:
        #     repo = 'develop'
        #
        # return f"https://raw.githubusercontent.com/anyoptimization/pymoo/{repo}/pymoo/data"


# returns the directory to be used for imports
def get_pymoo():
    return dirname(Config.root)

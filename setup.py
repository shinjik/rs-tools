try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
        name = "rs-tools",
        version = "0.0.1",
        author = "Sergey Plastinkin",
        author_email = "splastinkin@griddynamics.com",
        url="http://github.com/shinjik/rs-tools/tree",
        py_modules = ["RackSpaceClient", "RackSpaceManager"]
)


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
        name = "rs-tools",
        version = "0.0.2",
        author = "Sergey Plastinkin",
        author_email = "splastinkin@griddynamics.com",
        url="http://github.com/shinjik/rs-tools/tree",
        #py_modules = ["RackSpaceClient", "RackSpaceManager"],
        packages = ["rstools"],
        package_dir = {'rstools': 'src'},

        scripts = ["scripts/rs-image-delete", "scripts/rs-image-list", "scripts/rs-image-save", 
            "scripts/rs-server-add", "scripts/rs-server-delete", "scripts/rs-server-reboot", 
            "scripts/rs-server-list", "scripts/rs-server-update", "scripts/rs-server-rebuild", "scripts/rs-flavor-list"]

)


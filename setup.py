from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=['controller_configurator_utils'],
	package_dir={'': 'controller_configurator'}
)

setup(**setup_args)

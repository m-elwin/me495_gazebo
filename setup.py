from setuptools import find_packages, setup
from pathlib import Path

def recursive_files(prefix, path):
    """
    Recurse over path returning a list of tuples suitable for use with setuptools data_files.
    :param prefix: prefix path to prepend to the path
    :param path: Path to directory to recurse. Path should not have a trailing '/'
    :return: List of tuples. First element of each tuple is destination path, second element is a list of files to copy to that path
    """
    return [(str(Path(prefix)/subdir),
             [str(file) for file in subdir.glob('*') if not file.is_dir()] ) for subdir in Path(path).glob('**')]

package_name = 'me495_gazebo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/env-hooks', ['env-hooks/me495_gazebo.dsv']),
        *recursive_files('share/' + package_name, "models"),
        *recursive_files('share/' + package_name, "worlds"),
        *recursive_files('share/' + package_name, "launch")
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Matthew Elwin',
    maintainer_email='elwin@northwestern.edu',
    description='Example package for using Gazebo with ROS 2',
    license='GPLv3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

from setuptools import find_packages, setup
from glob import glob

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
        ('share/' + package_name + '/models', glob("models/*.sdf")),
        ('share/' + package_name + '/worlds', glob("worlds/*.sdf"))
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

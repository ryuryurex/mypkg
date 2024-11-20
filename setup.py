from setuptools import setup
<<<<<<< HEAD
import os
from glob import glob
=======
>>>>>>> 7c3505a... make new Repositories

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
<<<<<<< HEAD
    data_files=[  
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
=======
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
>>>>>>> 7c3505a... make new Repositories
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ryusei Noda',
    maintainer_email='noda.ryusei0325@gmail.com',
    description='robosys2024 sample',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
<<<<<<< HEAD
            'talker = mypkg.talker:main',
            'listener = mypkg.listener:main',
            'weather_publisher = mypkg.weather_publisher:main',
            'weather_listener = mypkg.weather_listener:main',
        ],
    },
)

=======
            'talker = mypkg.talker:main', #talker.pyのmain関数という意味
            #'listener = mypkg.listener:main', ←書いておいて後でコメントアウト
        ],
    },
)
>>>>>>> 7c3505a... make new Repositories

# from setuptools import setup

# package_name = 'my_robot_commands'

# setup(
#     name=package_name,
#     version='0.0.1',
#     packages=[],
#     py_modules=[
#         'scripts.move_robot',
#     ],
#     install_requires=['setuptools'],
#     data_files=[
#         ('share/ament_index/resource_index/packages',
#             ['resource/' + package_name]),
#         ('share/' + package_name, ['package.xml']),
#     ],
#     entry_points={
#         'console_scripts': [
#             'move_robot = scripts.move_robot:main',
#         ],
#     },
# )

from setuptools import setup

package_name = 'my_robot_commands'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[
        'scripts.move_robot',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Sophat Sophana',
    author_email='sophatsophana25@gmail.com',
    maintainer='Sophat Sophana',
    maintainer_email='sophatsophana25@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description=(
        'TODO: Package description'
    ),
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move_robot = scripts.move_robot:main',
        ],
    },
)
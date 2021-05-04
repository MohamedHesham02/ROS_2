from setuptools import setup

package_name = '2nd_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mohamed',
    maintainer_email='mo7ameda7med@live.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        "555=2nd_pkg.1st_node:main",
        "333=2nd_pkg.2nd_node:main",
        "222=2nd_pkg.client:main"
        ],
    },
)

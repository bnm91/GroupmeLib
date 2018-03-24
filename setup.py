from setuptools import setup

packages = [
    'GroupmeLib'
]

setup(
    name='GroupmeLib',
    version='0.0.1',
    description='Groupme library for python',
    author='Nixon Ball',
    packages=packages,
    include_package_data=True,
    install_requires=[
        'requests>=2.8.1'
    ]
)

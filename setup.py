from setuptools import setup, find_packages

with open('README.md') as readme:
    long_description = readme.read()

with open('requirements.txt') as requirements_production:
    install_requires = requirements_production.readlines()

setup(
    name='bucketlist',
    version='0.1',
    author='judy njagi',
    decription='Flask-restful api for buckelist',
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    exclude_package_data={'': ['README.md']},
    url='https://github.com/wger-project',
    install_requires='install_requires',
    long_description=long_description,
)

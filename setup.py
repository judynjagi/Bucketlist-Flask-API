from setuptools import setup, find_packages

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='bucketlist',
    version='0.1',
    author='judy njagi',
    decription='Flask-restful api for buckelist',
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    exclude_package_data={'': ['README.md']},
    url='https://github.com/judynjagi/Bucket_list.git',
    install_requires=[
       'flask',
        'flask-restful',
        'flask-migrate',
        'flask-script',
        'flask-sqlalchemy'],
    long_description='long_description',
    zip_safe=False
)

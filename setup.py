from setuptools import setup, find_packages
import re

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('pyfileinfo/pyfileinfo.py').read(),
    re.M
    ).group(1)

setup(
    name='pyfileinfo',
    author='James Campbell',
    author_email='jc@normail.co',
    version=version,
    license='MIT',
    description='file extension info',
    packages=['pyfileinfo'],
    py_modules=['pyfileinfo'],
    keywords=['mimetype', 'file-extension', 'fileinfo', 'file-system', 'drive-info'],
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    include_package_data=True,
    install_requires=[
        'argparse',
        'beautifulsoup4',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'pyfileinfo=pyfileinfo.pyfileinfo:main',
        ],
        },
    url='https://github.com/jamesacampbell/pyfileinfo',
    download_url='https://github.com/jamesacampbell/pyfileinfo/archive/{}.tar.gz'.format(version)
)
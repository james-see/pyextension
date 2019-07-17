from setuptools import setup, find_packages
import re

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('pyextension/pyextension.py').read(),
    re.M
).group(1)

setup(
    name='pyextension',
    author='James Campbell',
    author_email='jc@normail.co',
    version=version,
    license='MIT',
    description='file extension info',
    packages=['pyextension'],
    py_modules=['pyextension'],
    keywords=['mimetype', 'file-extension',
              'fileinfo', 'file-system', 'drive-info'],
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    include_package_data=True,
    install_requires=[
        'argparse',
        'beautifulsoup4',
        'requests',
        'lxml'
    ],
    entry_points={
        'console_scripts': [
            'pyextension=pyextension.pyextension:main',
        ],
    },
    url='https://github.com/jamesacampbell/pyextension',
    download_url='https://github.com/jamesacampbell/pyextension/archive/{}.tar.gz'.format(
        version)
)

from distutils.core import setup
from setuptools import find_packages

setup(
    name='pygramedia',
<<<<<<< HEAD
    version='0.0.1rc1',
=======
    version='0.0.1',
>>>>>>> 97311f7... Add setup script to pypi
    packages=['pygramed'],
    license='MIT',
    long_description='Unofficial API wrapper for Gramedia, the biggest bookstore in Indonesia and based on coroutine python 3.',
    install_requires=['aiohttp==3.4.4'],
    url='https://github.com/Keda87/PyGramedia',
    author='Adiyat Mubarak',
    author_email='adiyatmubarak@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
    ],
    zip_safe=False,
)
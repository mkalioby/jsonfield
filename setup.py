from distutils.core import Command

from setuptools import setup


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


setup(
    name='jsonfield',
    version='2.1.0',
    packages=['jsonfield'],
    license='MIT',
    include_package_data=True,
    author='Dan Koch',
    author_email='dmkoch@gmail.com',
    url='https://github.com/dmkoch/django-jsonfield/',
    description='A reusable Django field that allows you to store validated JSON in your model.',
    long_description=open("README.rst").read(),
    install_requires=['Django >= 1.11', 'six'],
    tests_require=['Django >= 1.11', 'six'],
    cmdclass={'test': TestCommand},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
    ],
)

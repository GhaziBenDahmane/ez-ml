from setuptools import setup, find_packages

version = open('VERSION').read().strip()
license = open('LICENSE').read().strip()

setup(
    name='ez-ml',
    version=version,
    license=license,
    author='Ghazi Ben Dahmen',
    author_email='ghazi.ben.dahmen3@gmail.com',
    url='http://www.github.com/ghazibendahmen/ez-ml',
    description='Most useful ML lib',
    long_description=open('README.md').read().strip(),
    packages=find_packages(),
    install_requires=[
        'pandas',
        'sklearn',
        'matplotlib'
    ],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'ezml = ezml.__main__:main',
        ]
    }
)

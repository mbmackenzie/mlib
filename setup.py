from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='mlib',
    version='0.0.1',
    description='A suite of useful python tricks.',
    long_description=readme,
    author='Matt Mackenzie',
    author_email='mbm2228@columbia.edu',
    url='https://github.com/mbmackenzie/mlib',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
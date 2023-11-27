from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='tools',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    author='LAPAI',
    author_email='sepai.iclr@gmail.com',
    description='Many tools',
    url='https://github.com/sepai-dev/tools',
    keywords='tools',
)

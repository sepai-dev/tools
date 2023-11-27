from setuptools import setup, find_packages

setup(
    name='tools',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies required by your tools
        'requests',
        # other dependencies...
    ],
    author='LAPAI',
    author_email='sepai.iclr@gmail.com',
    description='Many tools',
    url='https://github.com/sepai-dev/tools',
    keywords='tools',
)

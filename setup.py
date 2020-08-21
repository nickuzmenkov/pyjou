from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='pyjou',
    url='https://github.com/jladan/package_demo',
    author='nickuzmenkov',
    author_email='nickuzmenkov@yahoo.com',
    # Needed to actually package something
    packages=['main'],
    # Needed for dependencies
    # install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.0.1',
    # The license can be anything you like
    license='MIT',
    description='A Fluent Journal API',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
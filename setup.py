from setuptools import setup, find_packages

setup(
    name='slushie',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # Add your dependencies here
    ],
    # Other metadata
    author='Your Name',
    description='A description of your package',
    license='MIT',
    keywords='path manipulation',
    url='https://github.com/yourusername/slushie',
)

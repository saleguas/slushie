from setuptools import setup, find_packages

setup(
    name='slushie',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    
    # Dependencies
    install_requires=[
        # Add your dependencies here (e.g., 'numpy>=1.18.5')
    ],
    
    # Metadata
    author='Salvador Aleguas',
    author_email='salvadoraleguas@example.com',  # Add your email here
    description='Slushie: A Python library for relative path manipulation.',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='path sys-path manipulation python-path module-path',
    url='https://github.com/saleguas/slushie',
    
    # Specifying python requires
    python_requires='>=3',
    
    # Classifier (Optional)
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
    ],
)

from setuptools import setup, find_packages

setup(
    name='zont_api',
    version='0.1.0',
    description='Python wrapper for Zont API',
    author='Timur Vafin',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'aiohttp>=3.8.1',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

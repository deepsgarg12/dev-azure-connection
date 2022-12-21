from setuptools import setup

setup(
    name="edgevu",
    version="1.0",
    description='edgevu connection util to read blobs',
    packages=['edgevu'],
    install_requires=[
        "azure.identity",
        "azure-edgevu-blob",
        "pandas"
    ],
    python_requires=">3.6.1"
)
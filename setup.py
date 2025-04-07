from setuptools import setup, find_packages

setup(
    name="dynamic_pricing",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pandas>=1.3.4',
        'numpy>=1.21.2',
        'scikit-learn>=1.0.2',
        'plotly>=5.8.0'
    ],
)
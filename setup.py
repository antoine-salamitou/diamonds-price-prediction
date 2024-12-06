from setuptools import setup, find_packages

setup(
    name="diamonds-price-prediction",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "sphinx>=4.0",
        "sphinx-rtd-theme"
    ],
    extras_require={
        "sphinx": ["sphinx>=4.0", "sphinx-rtd-theme"]
    },
)

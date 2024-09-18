from setuptools import setup, find_packages

setup(
    name="long_clip",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'ftfy',
        'packaging',
        'regex',
        'tqdm',
        'torch',
        'torchvision'
    ],
    url="https://github.com/alzaia/Long-CLIP",
)

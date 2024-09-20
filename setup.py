from setuptools import setup, find_packages

setup(
    name="longclip",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'longclip.model': ['*.gz', '*.txt'],
    },
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

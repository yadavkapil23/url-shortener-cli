from setuptools import setup, find_packages

setup(
    name='url-shortener',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'shr=shortener.__main__:main',
        ],
    },
    author='Kapil',
    description='A CLI tool to shorten URLs.',
    python_requires='>=3.7',
)

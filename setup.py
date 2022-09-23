import setuptools

setuptools.setup(
    name='package',
    version='1.0',
    author='sid',
    description='calculation',
    packages =setuptools.find_packages(),
    classifiers = ["Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT : License",
    "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)
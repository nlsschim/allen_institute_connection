# need to make more robust in the future
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

packages = find_packages()
print(f"Found packages {packages}")

setup(
    name="allen_institute_connection", # Required  
    version="0.1",  # Required
    long_description=long_description, 
    long_description_content_type="text/markdown", 
    url="https://github.com/nlsschim/allen_institute_connection",
    author="Nels Schimek, Humood Alanzi", 
    author_email="nlsschim@uw.edu",
    classifiers=[
        # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 1 - Planning",
        
        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: bioinformatics',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="proteins, function",
    packages=packages,
    python_requires=">=3.10, <4",
    extras_require={ 
        "test": ["coverage", 'pytest'],
    },

    package_data={},
    data_files=None, 
    entry_points={},
)
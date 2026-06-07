# Python
# setup.py for packaging a single script called 'tok3ns'

from setuptools import setup, find_packages

setup(
    name="tok3ns",  # Name of your package
    version="0.1.0",  # Initial version
    description="A Python package with a single script called tok3ns",
    author="James R",
    py_modules=["tok3ns"],  # Single script, no packages
    install_requires=[
        # List any dependencies here, e.g., "requests", "numpy"
        "requests"
    ],
    entry_points={
        "console_scripts": [
            # Creates a command-line executable `tok3ns` that calls main() in tok3ns.py
            "tok3ns=tok3ns:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

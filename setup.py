from setuptools import setup, find_packages


setuptools.setup(
    name="MachPy",
    version="0.1",
    author="Amanda Butler",
    author_email="amanda.butler@yale.edu",
    description='Visualizer for Mach Data from Omega500',
    packages=["Contents"],
    package_data={'Contents': ['cubedat/*.npy']},
    install_requires=[
        'numpy>=1.17',
        'matplotlib<3.4.0',
        'streamlit',
        'yt',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Computational Cosmology",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

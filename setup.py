from setuptools import setup

with open("README.md") as README:
    long_description = README.read()

setup(
    name='nextcord-logging',
    version='1.0',
    description='An exact copy of discord-logging but for Nextcord.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Avaneesh Sharma',
    author_email='super.avaneesh@gmail.com',
    packages=['nextcord_logging'],
    install_requires=['nextcord'],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
    ],
)
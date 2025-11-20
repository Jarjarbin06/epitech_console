#############################
###                       ###
###      Console v2.0     ###
###     ----Line.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from setuptools import setup, find_packages


setup(
    name="Console v2",
    version="0.1.0",
    description="Console tools (animation/colored printing/formating/etc) ",
    long_description=open("README", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Nathan Jarjarbin",
    author_email="nathan.amaraggi@epitech.eu",
    url="https://github.com/Jarjarbin06/Console",
    packages=find_packages(),
    install_requires=[
        # no dependencies
    ],
    package_data={
        "Console v2": ["Console/config.ini", "LICENSE", "setup.py"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.13',  # version where it was coded from
)

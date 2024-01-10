from setuptools import find_packages, setup

with open("README.rst", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="khapitools",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django",
        "khapi",
        "ImageHash",
        "Pillow",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    long_description=long_description,
    long_description_content_type="text/x-rst",
)

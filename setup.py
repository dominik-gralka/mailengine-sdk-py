from setuptools import setup, find_packages

setup(
    name="mailengine-sdk",
    version="0.1.0-dev",
    packages=find_packages(),
    install_requires=["requests"],
    author="Umbratic",
    author_email="contact@umbratic.com",
    description="Python SDK for MailEngine",
    url="https://github.com/your_username/mailengine-python-sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

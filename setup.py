import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flight_scraper",
    version="0.0.2",
    author="kilianplapp",
    description=
    "A python module that allows users to scrape flight price information from a range of airlines.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kilianplapp/flight-scraper",
    packages=['flight_scraper'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
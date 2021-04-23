import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="mbd_pay",
  version="0.1.4",
  author="shaoxyz",
  author_email="shwb95@163.com",
  description="面包多支付SDK - https://mbd.pub/",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/shaoxyz/mbd_pay",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)

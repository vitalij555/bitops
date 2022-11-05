import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name = 'bitops',
  packages=setuptools.find_packages(),
  version = '0.0.3',
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Simple bit manipulations for personal projects',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Vitalij Gotovskij',               # Type in your name
  author_email = 'vitalij@cdeveloper.eu',     # Type in your E-Mail
  url = 'https://github.com/vitalij555/binary-operations',   # Provide either the link to your github or to your website
  # download_url = 'https://github.com/vitalij555/binops/archive/v_0_1_1.tar.gz',
  keywords = ['BINARY', 'OPERATIONS', 'BITWISE', 'MATH', 'BITS', "BYTES"],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
  ],
)

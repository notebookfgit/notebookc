from setuptools import setup, find_packages


with open("README.md","r") as readme_file:
    readme = readme_file.read()
    
    
requirements = []

setup(
      name="noteconvert",
      version="2.0.1",
      author="Bose Oladipo",
      author_email="augustbose@gmail.com",
      description="A package to convert your Jupyter Notebook",
      long_description=readme,
      long_description_content_type="text/markdown",
      url="https://github.com/your_package/homepage/",
      packages=find_packages(),
      install_requires=requirements,
      classifiers=[
              "Programming Language :: Python :: 3.6",
              "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
              ],
)
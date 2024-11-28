import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='lppls-w',
      version='0.6.19',
      description='A Python module for fitting the LPPLS model to data.',
      packages=['lppls-w'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/DrunkenMaster2004/lppls-w',
      python_requires='>=3.7',
      install_requires=[
          'pandas',
          'matplotlib',
          'scipy',
          'xarray',
          'cma',
          'tqdm',
          'numba'
      ],
      zip_safe=False,
      include_package_data=True,
      package_data={'': ['data/*.csv']},
)

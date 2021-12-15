from setuptools import setup

setup(name='datastax',
      version='0.0.1',
      description='A python package to handle dataStructures',
      url='#',
      author='Pritam K',
      author_email='pritamkundu771@gmail.com',
      license='MIT',
      packages=['datastax', 'datastax/linkedlists', 'datastax/trees'],
      zip_safe=False,
      classifiers=[
          "Programming Language :: Python :: 3.10",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Software Development :: Documentation"
      ])

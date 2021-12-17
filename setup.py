from setuptools import setup

setup(name='datastax',
      version='0.0.2',
      packages=['datastax', 'datastax/linkedlists', 'datastax/trees'],
      license='MIT',
      description='A python library to handle dataStructures',
      long_description='This library which supports ADTs like Linkedlists and Trees and its types. This instant '
                       'library is solely written from scratch and requires no additional libraries to be installed. '
                       'It solves the purpose of writing programs for complex data structures from scratch, '
                       'visualizing ADTs and simplify writing its inner architectures',
      url='https://github.com/warmachine028/datastax',
      author='Pritam K',
      author_email='pritamkundu771@gmail.com',
      zip_safe=False,
      classifiers=[
          "Programming Language :: Python :: 3.10",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Topic :: Software Development :: Documentation",
          "Topic :: Software Development :: Libraries :: Python Modules"
      ])

import codecs
import sys

from setuptools import setup

try:
    # https://stackoverflow.com/questions/30700166/python-open-file-error
    with codecs.open("README.md", 'r', errors='ignore') as file:
        readme_contents = file.read()

except Exception as error:
    readme_contents = 'This library which supports ADTs like Linkedlists and Trees and its types. This instant ' \
                      'library is solely written from scratch and requires no additional libraries to be installed. ' \
                      'It solves the purpose of writing programs for complex data structures from scratch, ' \
                      'visualizing ADTs and simplify writing its inner architectures. This Module Supports the ' \
                      'following dataStructures:\n' \
                      '1. Arrays:\n' \
                      '   a. Queue\n' \
                      '   b. Stack\n\n' \
                      '2. LinkedLists:\n' \
                      '   a. Singly Linked List\n' \
                      '   b. Doubly Linked List\n' \
                      '   c. Circular Linked List\n' \
                      '   d. Doubly Circular List\n' \
                      '   e. Queue Representation\n\n' \
                      '3. Trees:\n' \
                      '   a. Binary Tree\n' \
                      '   b. Binary Search Tree\n' \
                      '   c. AVL Tree\n' \
                      '   d. Min Heap Tree\n' \
                      '   e. Max Heap Tree'
    sys.stderr.write("Warning: Could not open README.md due %s\n" % error)

setup(
    name='datastax',
    version='0.0.3',
    packages=[
        'datastax',
        'datastax/arrays',
        'datastax/linkedlists',
        'datastax/trees',
    ],
    license='MIT',
    description='A python library to handle dataStructures',
    long_description=readme_contents,
    long_description_content_type='text/markdown',
    url='https://github.com/warmachine028/datastax',
    author='Pritam K',
    author_email='pritamkundu771@gmail.com',
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)

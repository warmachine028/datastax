import codecs
import sys

from setuptools import setup

import datastax

try:  # https://stackoverflow.com/questions/30700166/python-open-file-error
    with codecs.open("README.md", 'r', errors='ignore', encoding='utf8') as f:
        readme_contents = f.read()

except Exception as error:
    readme_contents = (
        'This library which supports ADTs like LinkedLists and Trees and its '
        'types. This instant library is solely written from scratch and '
        'requires no additional libraries to be installed. It solves the '
        'purpose of writing programs for complex data structures from scratch,'
        ' visualizing ADTs and simplify  writing its inner architectures. This'
        ' Module Supports the following dataStructures:\n'
        '1. Arrays:\n'
        '   a. Queue\n'
        '   b. Stack\n\n'
        '   c. Priority Queue\n\n'
        '2. Lists:\n'
        '   a. Singly Linked List\n'
        '   b. Doubly Linked List\n'
        '   c. Circular Linked List\n'
        '   d. Doubly Circular List\n'
        '   e. Queue\n\n'
        '   f. LRU Cache\n\n'
        '3. Trees:\n'
        '   a. Binary Tree\n'
        '   b. Binary Search Tree\n'
        '   c. AVL Tree\n'
        '   d. Heap Tree\n'
        '   e. Min Heap Tree\n'
        '   f. Expression Tree\n'
        '   e. Threaded Binary Tree\n'
        '   f. Segment Trees\n'
        '       i. Sum Segment Tree\n'
        '      ii. Min Segment Tree\n'
        '   g. Huffman Tree\n'
        '   h. Red Black Tree\n'
        '   i. Fibonacci Tree\n'
        '   j. Splay Tree\n\n'
    )
    sys.stderr.write(f"Warning: Could not open README.md due {error}\n")
setup(
    name='datastax',
    maintainer="Pritam Kundu",
    description='A python library to handle dataStructures',
    long_description=readme_contents,
    long_description_content_type='text/markdown',
    url='https://github.com/warmachine028/datastax',
    author='Pritam K',
    download_url="https://pypi.python.org/pypi/datastax",
    project_urls={
        'Bug Tracker': 'https://github.com/warmachine028/datastax/issues',
        'Documentation':
            'https://github.com/warmachine028/datastax#readme',
        'Source Code': 'https://github.com/warmachine028/datastax',
    },
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",

        "Topic :: Documentation",
        "Topic :: Education :: Testing",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing :: Unit",

        "Typing :: Typed"
    ],
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    test_suite='pytest',
    version=datastax.__version__,
    python_requires='>=3.11',
    packages=[
        'datastax',
        'datastax/Utils',
        'datastax/Arrays',
        'datastax/Arrays/AbstractArrays',
        'datastax/Lists',
        'datastax/Lists/AbstractLists',
        'datastax/trees',
        'datastax/trees/private_trees',
    ],
    author_email='pritamkundu771@gmail.com',
)
# python setup.py sdist bdist_wheel

import codecs
import sys

from setuptools import setup

import datastax

try:  # https://stackoverflow.com/questions/30700166/python-open-file-error
    with codecs.open("README.md", 'r', errors='ignore', encoding='utf8') as f:
        readme_contents = f.read()

except FileNotFoundError as e:
    readme_contents = (
        'This library which supports ADTs like Arrays, LinkedLists and Trees '
        'and its types. This instant library is solely written from scratch '
        'and requires no additional libraries to be installed. It solves the '
        'purpose of writing programs for complex data structures from scratch,'
        ' visualizing ADTs and simplify  writing its inner architectures. This'
        ' Module Supports the following dataStructures:\n'
        '1. Nodes\n'
        '   a. Node\n'
        '   b. Doubly Node\n'
        '   c. Tree Node\n'
        '   d. AVL Node\n'
        '   e. Red-Black Node\n'
        '   f. Splay Node\n'
        '   g. Heap Node\n'
        '   h. Segment Node\n'
        '   i. Huffman Node\n'
        '   j. Threaded Node\n'
        '2. Arrays:\n'
        '   a. Queue\n'
        '   b. Stack\n\n'
        '   c. Priority Queue\n\n'
        '3. Lists:\n'
        '   a. Singly-Linked List\n'
        '   b. Doubly-Linked List\n'
        '   c. Circular-Linked List\n'
        '   d. Doubly-Circular List\n'
        '   e. Queue\n\n'
        '   f. LRU Cache\n\n'
        '4. Trees:\n'
        '   a. Binary Tree\n'
        '   b. Search Trees\n'
        '        i. Binary-Search Tree\n'
        '       ii. AVL Tree\n'
        '      iii. Red-Black Tree\n'
        '       iv. Splay Tree\n'
        '   c. Heap Trees\n'
        '        i. Max-Heap Tree\n'
        '       ii. Min-Heap Tree\n'
        '   d. Segment Trees\n'
        '       i. Sum-Segment Tree\n'
        '      ii. Min-Segment Tree\n'
        '   f. Huffman Tree\n'
        '   g. Fibonacci Tree\n'
        '   h. Expression Tree\n'
        '   g. Threaded-Binary Tree\n\n'
        '5. Tables\n'
        '   a. HuffmanTable'
    )
    sys.stderr.write(f"Warning: Could not open README.md due {e}\n")
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
    python_requires='>3.11',
    packages=[
        'datastax',
        'datastax/Utils',
        'datastax/Utils/Exceptions',
        'datastax/Utils/Warnings',
        'datastax/Arrays',
        'datastax/Arrays/AbstractArrays',
        'datastax/Nodes',
        'datastax/Nodes/AbstractNodes',
        'datastax/Lists',
        'datastax/Lists/AbstractLists',
        'datastax/Trees',
        'datastax/Trees/AbstractTrees',
        'datastax/Tables',
        'datastax/Tables/AbstractTables',
    ],
    author_email='pritamkundu771@gmail.com',
)
# python setup.py sdist bdist_wheel

    updated: Wednesday, 12th July 2023

<div align=center>
    <a href="https://github.com/warmachine028/datastax">
        <img width=200 src="https://github.com/warmachine028/datastax/assets/75939390/2c1ad8f7-b1ed-44aa-9923-307af5a52cfc" alt="datastax">
    </a>
    <p style="font-family: roboto, calibri; font-size:12pt; font-style:italic">Simplicity meets intelligence</p>
    <a href="https://pypi.org/project/datastax">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/datastax?color=blueviolet">
    </a>
    <a href="https://pypi.org/project/datastax/#files"><img alt="PyPI Downloads" src="https://img.shields.io/pypi/dm/datastax.svg?label=Pypi%20downloads"></a>
    <br>
    <a href="https://github.com/warmachine028/datastax/releases/"> 
        <img src="https://img.shields.io/github/v/release/warmachine028/datastax?color=brightgreen">
    </a>
    <a href="https://github.com/warmachine028/datastax/releases/tag/"> 
        <img src="https://img.shields.io/github/v/release/warmachine028/datastax?color=lightgreen&include_prereleases&label=pre%20release"> 
    </a>
    <br>
    <img src="https://img.shields.io/github/stars/warmachine028/datastax">
    <a href= "https://github.com/warmachine028/datastax/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/warmachine028/datastax?color=orange">
    </a>
    <a href="https://github.com/warmachine028/datastax/network/members">
        <img src="https://img.shields.io/github/forks/warmachine028/datastax?color=cyan">
    </a>
    <br>
</div>

# [dataStax](https://github.com/warmachine028/datastax)

## What's New?

- Refactored Array Contents
- Added AbstractArray SubModule to abstract print logic
- Added more test cases for Queues
- Type Checked Arrays and Lists with mypy

## Table of Contents

- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Benefits](#benefits)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [What's Next](#whats-next)

## Introduction

- This library offers a simple yet powerful solution for implementing common abstract data structures.
- With a pure Python implementation, it provides representations of tree, linked list, and array-based data structures
  accessible through a basic command prompt interface.
- The package includes visualization features that enhance the understanding of each data structure.
- Students can greatly benefit from utilizing this package for their learning and educational purposes.
- Please note that this project is currently a work in progress and undergoing active development.

## Problem Statement

- Many CS students encounter difficulties in comprehending the intricate internal architecture of complex
  Abstract Data Types (ADTs) during the initial stages of their B.Tech course.
- When attempting to solve coding challenges that involve writing test cases using these ADTs, it becomes excessively
  burdensome to manually create these data structures from scratch.
- Furthermore, while developing programs that implement these ADTs, numerous errors are encountered due to the
  inability to visualize and understand the underlying processes of these data structures.

## Benefits

- Swift installation process
- Efficient and prompt updates
- Minimal disk space usage due to its small size
- No additional modules or dependencies needed
- Developed entirely from scratch
- Upcoming user-friendly documentation
- Command line demonstration for easy usage

## Requirements

- Runs on latest Python 3.11+
- (Suggesting you to always update to the latest python version)

## Installation

1. Use the python package manager [pip](https://pip.pypa.io/en/stable/) to install datastax.

```bash
pip install datastax
```

## Usage

### Demo

- To get a demo of the library use the following command
    - **Windows**:

  ```bash
  > py -m datastax 
  ```
    - **Unix based systems**:

  ```bash
  $ python3 -m datastax
  ```
    - _Result_
  ```bash
  Available modules are:
  1. LinkedLists
  2. Trees
  3. Arrays
  
  Usage
  > py datastax <data-structure> [data]
  Data Structures:
  ->  trees          Hierarchical DS
  ->  linkedlists    Linear DS
  ->  arrays         Fixed Size Linear DS

  ```
- Then follow as the instruction guides

```bash
> py -m datastax linkedlist 1 2 3 4
  Visuals for LinkedLists:

  1. Singly Linked List:
     HEAD                                         TAIL
 ┌─────╥────┐   ┌─────╥────┐   ┌─────╥────┐   ┌─────╥────┐
 │  1  ║  ----->│  2  ║  ----->│  3  ║  ----->│  4  ║  -----> NULL
 └─────╨────┘   └─────╨────┘   └─────╨────┘   └─────╨────┘


  2. Doubly Linked List:
               HEAD                                                        TAIL
         ┌────╥─────╥────┐   ┌────╥─────╥────┐   ┌────╥─────╥────┐   ┌────╥─────╥────┐
 NULL <-----  ║  1  ║  <------->  ║  2  ║  <------->  ║  3  ║  <------->  ║  4  ║  -----> NULL
         └────╨─────╨────┘   └────╨─────╨────┘   └────╨─────╨────┘   └────╨─────╨────┘
  ...
```

### Practical Usage

- **Queue**

![queue](https://github.com/warmachine028/datastax/assets/75939390/0fe72e7a-7eb9-4ee9-9b7a-6c0f83d98409)

![queue_output](https://github.com/warmachine028/datastax/assets/75939390/daecb209-d459-4374-96e0-816deb08dcde)

------------------------------------
---------------

- **BinaryTree**

![binaryTree](https://github.com/warmachine028/datastax/assets/75939390/7228c4b4-def7-4c6b-9e29-e6e244c2c4c1)

![binaryTree_output](https://github.com/warmachine028/datastax/assets/75939390/2357fa58-3122-47ad-ac7f-f67d72ef6e8c)

---------------------------------------------------

- **MinHeapTree**

![mht](https://github.com/warmachine028/datastax/assets/75939390/1c00a207-9ea0-4965-898f-29e37883fac5)

![mht_output](https://github.com/warmachine028/datastax/assets/75939390/fcfe24d9-6b80-4b16-873c-3f5c3d808d70)

---------------------------------------------------

- **ThreadedBinaryTree**

![tbt](https://github.com/warmachine028/datastax/assets/75939390/ab2f2572-1474-4d82-9138-b8ee85869114)

![tbt_output](https://github.com/warmachine028/datastax/assets/75939390/9e77c5dc-082c-471b-90d5-33792673bdf3)

---------------------------------------------------

- **SumSegmentTree**

![sst](https://github.com/warmachine028/datastax/assets/75939390/7bdcfd6e-37ac-4421-b6d2-acd59cf4976c)

![sst_output](https://github.com/warmachine028/datastax/assets/75939390/3a3f1de2-72e8-4b1d-88c7-40e4dcc11215)

---------------------------------------------------

- **HuffmanTree**

![hft](https://github.com/warmachine028/datastax/assets/75939390/5dc609a6-51c2-4ec9-88ba-c1ea175ef88e)

![hft_output](https://github.com/warmachine028/datastax/assets/75939390/2de13da6-8eaa-4e62-a06a-8dbf91c008a2)

---------------------------------------------------

- **RedBlackTree**

![rbt](https://github.com/warmachine028/datastax/assets/75939390/8d924d6e-d63a-4891-bf9e-c7acdb3775ba)

![rbt_output](https://github.com/warmachine028/datastax/assets/75939390/3af4ceb6-1e68-4906-ba39-db84dbf274f0)

## What's Next

- Enhanced Documentation
- Better TestCases for Huffman Tree
- Better TestCases for Segment Trees
- Test Cases for Fibonacci Tree

    updated: Sunday, 9th July 2023

<div align=center>
    <a href="https://github.com/warmachine028/datastax">
    <img width=200 src="https://github.com/warmachine028/datastax/assets/75939390/2c1ad8f7-b1ed-44aa-9923-307af5a52cfc" alt="datastax"></a>
    <p style="font-family: roboto, calibri; font-size:12pt; font-style:italic"> Simplicity meets intelligence</p>
    <a href="https://pypi.org/project/datastax" ><img alt="PyPI" src="https://img.shields.io/pypi/v/datastax?color=blueviolet"></a>
    <a href="https://pypi.org/project/datastax/#files"><img alt="PyPI Downloads" src="https://img.shields.io/pypi/dm/datastax.svg?label=Pypi%20downloads"></a>
    <br>
    <a href="https://github.com/warmachine028/datastax/releases/"> <img src="https://img.shields.io/github/v/release/warmachine028/datastax?color=brightgreen"></a>
    <a href="https://github.com/warmachine028/datastax/releases/tag/"> <img src="https://img.shields.io/github/v/release/warmachine028/datastax?color=lightgreen&include_prereleases&label=pre%20release"> </a>
    <br>
    <img src="https://img.shields.io/github/stars/warmachine028/datastax">
    <a href= "https://github.com/warmachine028/datastax/blob/main/LICENSE"><img src="https://img.shields.io/github/license/warmachine028/datastax?color=orange"></a>
    <a href="https://github.com/warmachine028/datastax/network/members"><img src="https://img.shields.io/github/forks/warmachine028/datastax?color=cyan"></a>
    <br>
</div>


# [dataStax](https://github.com/warmachine028/datastax)

## What's New?

- Added Mandatory Keyword arguments to avoid confusion in:
  - Arrays 
  - ThreadedBinaryTree 
- Added High Quality PNGs in README.md

## Table of Contents

- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Benefits](#benefits)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [What's Next](#whats-next)

## Introduction

- This is a very simple yet powerful project to implement day to day abstract data structures
- A pure implementation of Python in representing Tree, Linkedlist and Array based datastructures in basic command
  prompt
- It helps visualize each data structure for better understanding
- Students can be beneficial in using this Package
- This project is still under construction

## Problem Statement

- Often at the beginning of B.Tech Course, CS students face a lot of problems understanding the internal architecture of
  complex ADTs.
- While solving coding challenges locally where test cases have to be written using these ADTs, it becomes really
  cumbersome to write these data structures from scratch.
- Also, when writing programs which implements these ADS, we encounter lots of errors just because we are unable to
  preview what's actually going on under the hood.

## Benefits

- Instant installation
- Quick Updates
- Very small size
- No extra modules required
- Written purely from scratch
- Easy Documentation [Upcoming]
- Command Line Demo

## Requirements

- Runs on latest Python 3.7+
- (WARNING: Though the module might run on py 3.7 error free, but it has been tested for 3.9+)
- (Suggesting you to always update to the latest python version)
- This Library requires no extra modules

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

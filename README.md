    updated: Wednesday, 29th December 2021

<div align=center>
    <a href="https://github.com/warmachine028/datastax"><img width=200 src="assets/icon.png" alt="datastax"></a>
    <p style="font-family: roboto, calibri; font-size:12pt; font-style:italic"> Simplicity meets intelligence</p>
    <a href="https://pypi.org/project/datastax" ><img alt="PyPI" src="https://img.shields.io/pypi/v/datastax?color=blueviolet"></a>
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

- Included Priority Queue
- Replaced Bad Implementation of max heap with arrays to true tree implementation
- Added Proper MinHeap DataStructure
- OverFlow and UnderFlow Errors

## Table of Contents

- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Benefits](#benefits)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Whats Next](#what's-next)

## Introduction

- This is a very simple yet powerful project to implement day to day abstract data structures.
- A pure implementation of Python in representing Trees and Linkedlists in basic command prompt

- It helps visualize each data structure for better understanding
- Students can be beneficial in using this Package
- This project is still under construction

## Problem Statement

- Often in the beginning CS students face problems in understanding the internal architecture of ADTs
- While solving coding challenges locally where test cases have to be written using these ADTs, it becomes really
  cumbersome to write these data structures from scratch.
- Often while writing a programs implementing these ADS we encounter lots of errors just because we are unable to
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
  $ python -m datastax
  ```
    - _Result_
  ```bash
  Available modules are:
  1. LinkedLists
  2. Trees
  3. Arrays
  
  Usage
  $ py datastax <data-structure> [data]
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
  Node[1] -> Node[2] -> Node[3] -> Node[4] -> NULL

  2. Doubly Linked List:
  NULL <-> Node[1] <-> Node[2] <-> Node[3] <-> Node[4] <-> NULL
  ...
```

### Practical Usage

```py
from datastax.trees import BinaryTree

bt = BinaryTree([1, 2, 3, 4, 5])
print(bt)

## OUTPUT:
"""
            1           
      ┌─────┴─────┐     
      2           3     
   ┌──┴──┐              
   4     5              
"""
---------------------------------------------------
from datastax.trees import MinHeapTree

MiHT = MinHeapTree([1, 2, 4, 2, 6, 5, 9, 18, 3, 2])
print(MiHT)
## OUTPUT
"""
                        1                       
            ┌───────────┴───────────┐           
            2                       4           
      ┌─────┴─────┐           ┌─────┴─────┐     
      2           2           5           9     
   ┌──┴──┐     ┌──┘                             
  18     3     6                                
"""
```

## What's Next

- Implementation of **Sum Segment Tree, Expression Tree**
- Proper tests using UnitTest Lib
- Enhanced Documentation
- Implementation of Other Abstract data types like **LRU_CACHE, LFU_CACHE, SKIP_LIST**
- If things go accordingly I am planning to implement **threaded binary tree**. Seems a completely impossible task to
  show threads nut I'll try my best
- Beautification of [README.md](README.md)

### Upcoming

```py
from datastax.trees import ThreadedBinaryTree as Tbt

tbt = Tbt(['a', 'b', 'c', 'd', 'e'])
"""
Example 3:                    
                                a
                          ┌─────┴─────┐
                          b    │ └────c
                       ┌──┴──┐ │
                       d─┘ └─e─┘
"""
```

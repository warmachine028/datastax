    updated: Monday, 24th January 2022

<div align=center>
    <a href="https://github.com/warmachine028/datastax">
    <img width=200 src="https://github.com/warmachine028/datastax/blob/main/assets/icon.png" alt="datastax"></a>
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

- Added Threaded Binary Trees
- Added LRU Cache
- Added Proper and effective testcases

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
  Node[1] -> Node[2] -> Node[3] -> Node[4] -> NULL

  2. Doubly Linked List:
  NULL <-> Node[1] <-> Node[2] <-> Node[3] <-> Node[4] <-> NULL
  ...
```

### Practical Usage

- **Queue**

```py
from datastax.arrays import Queue

# Building a Queue Data Structure with fixed capacity
queue = Queue(capacity=5)

# Enqueueing items inside queue
for item in ('item 1', 'item 2'):
    queue.enqueue(item)

# Performing Dequeue Operation 
queue.dequeue()

queue.enqueue('item 3')
print(queue)
```

```shell
$ OUTPUT:

         ┌──────────╥──────────┬──────────┐
FRONT -> │    ╳     ║  item 2  │  item 3  │ <- REAR
         └──────────╨──────────┴──────────┘
      
```

---------------------------------------------------

- **BinaryTree**

```py
from datastax.trees import BinaryTree

bt = BinaryTree([1, 2, 3, 4, 5])
print(bt)
```

```shell
$ OUTPUT:

             1           
       ┌─────┴─────┐     
       2           3     
    ┌──┴──┐              
    4     5              
```

---------------------------------------------------

- **MinHeapTree**

```py
from datastax.trees import MinHeapTree

MiHT = MinHeapTree([1, 2, 4, 2, 6, 5, 9, 18, 3, 2])
print(MiHT)
```

```shell
$ OUTPUT

                        1                       
            ┌───────────┴───────────┐           
            2                       4           
      ┌─────┴─────┐           ┌─────┴─────┐     
      2           2           5           9     
   ┌──┴──┐     ┌──┘                             
  18     3     6    

```

---------------------------------------------------

- **ThreadedBinaryTree**

```py
from datastax.trees import ThreadedBinaryTree as Tbt

tbt = Tbt(['a', 'b', 'c', 'd', 'e'], insertion_logic="BinaryTree")
print(tbt)
```

```shell
$ OUTPUT               
                                   ┌───┐
   ┌───────────────────────────> DUMMY │<──────────────┐
   │                           ┌───┴───┘               │
   │                           a                       │        
   │           ┌───────────────┴───────────────┐       │        
   │           b           │           │       c       │        
   │   ┌───────┴───────┐   │           └───────┴───────┘        
   │   d   │       │   e   │                                    
   └───┴───┘       └───┴───┘                                    

```

## What's Next

- Implementation of **Segment Trees**
- Proper tests using UnitTest Lib
- Enhanced Documentation
- Implementation of Other Abstract data types like **LFU_CACHE, SKIP_LIST**
- Beautification of [README.md](README.md)

### Upcoming

```py
from datastax.trees import SumSegmentTree

st = St([1, 3, 5, 7, 9, 11])
print(st)
```

```shell
$ OUTPUT               
                       36                       
            ┌───────────┴───────────┐           
            9                      27           
      ┌─────┴─────┐           ┌─────┴─────┐     
      4           5          16          11     
   ┌──┴──┐     ┌──┴──┐                          
   1     3     7     9                          
                          
```
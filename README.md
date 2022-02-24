    updated: Thursday, 24th February 2022

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

- Added Sum Segment Tree
- Added Min Segment Tree
- Added Huffman Tree
    - data encoder
    - data decoder
    - Huffman Code
    - Huffman Table
    - compression ratio
    - space saved
- Added Red Black Tree - 🗸 TESTED
- Added Splay Tree - 🗸 TESTED
- Added Delete methods in: 🗸 TESTED
    - BinaryTree
    - BinarySearchTree
    - AVLTree
- Enhanced string representation of all LinkedLists
- Added Custom Comparator for PriorityQueue
- Added name-mangler function for items with multiline string representations
- Added HuffmanTable object for storing and visualizing huffman-table

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

logic = str("BinaryTree")
tbt = Tbt(['a', 'b', 'c', 'd', 'e'], insertion_logic=logic)
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

---------------------------------------------------

- **SumSegmentTree**

```py
from datastax.trees import SumSegmentTree

sst = SumSegmentTree([1, 3, 5, 7, 9, 11])
print(sst)
print(sst.preorder_print())
```

```shell
$ OUTPUT        
                                                
                       36                       
                      [0:5]                     
            ┌───────────┴───────────┐           
            9                      27           
          [0:2]                   [3:5]         
      ┌─────┴─────┐           ┌─────┴─────┐     
      4           5          16          11     
    [0:1]                   [3:4]               
   ┌──┴──┐                 ┌──┴──┐              
   1     3                 7     9              


36 [0:5]
├─▶ 9 [0:2]
│   ├─▶ 4 [0:1]
│   │   ├─▶ 1 
│   │   └─▶ 3 
│   └─▶ 5 
└─▶ 27 [3:5]
    ├─▶ 16 [3:4]
    │   ├─▶ 7 
    │   └─▶ 9 
    └─▶ 11             
                  
```

---------------------------------------------------

- **HuffmanTree**

```py
from datastax.trees import HuffmanTree

string = str("Espresso Express")
hft = HuffmanTree(string)
print(hft)
```

```shell
$ OUTPUT
                                               16                                               
                         0                      │                      1                        
                        ┌───────────────────────┴───────────────────────┐                       
                        7                                               9                       
             0          │          1                         0          │          1            
            ┌───────────┴───────────┐                       ┌───────────┴───────────┐           
            3                       4                       4                       s           
       0    │    1             0    │    1             0    │    1                  5           
      ┌─────┴─────┐           ┌─────┴─────┐           ┌─────┴─────┐                             
      x           2           e           r           E           p                             
      1         0 │ 1         2           2           2           2                             
               ┌──┴──┐                                                                          
               o                                                                                
               1     1       
```

---------------------------------------------------

- **RedBlackTree**

```py
from datastax.trees import RedBlackTree

rbt = RedBlackTree([500, 236, 565, 105, 842, 497, 312, 612, 80])
rbt.delete(236)
print(rbt)
```

```shell
$ OUTPUT                                                                         
                                   500                                      
                  ┌─────────────────┴─────────────────┐                     
                 105                                 612                    
         ┌────────┴────────┐                 ┌────────┴────────┐            
        80                497               565               842           
                       ┌───┘                                                
                     312
                                                                                                                                    
```

## What's Next

- Enhanced Documentation
- Better TestCases for Huffman Tree
- Better TestCases for Segment Trees
- Test Cases for Fibonacci Tree
- Adding of images of trees instead of trees themselves in README 

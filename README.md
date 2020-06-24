# Tomasulo Algorithm Simulator in Python

## Introduction

This project is a simulator of the Tomasulo algorithm.
This powerful algorithm allows for out-of-order execution while keeping the order of the instructions. The instruction is stored in a reservation station until it has all the data needed to compute the instruction. The result will be send back on a Common Data Bus and every object (registers and reservation stations) that needs the data will get it.
Hence the stalling of the machine should be reduced by allowing certain operations to be executed after instructions which were issued after them.

## Building
Download the folder
Build the tomasulo.py file (it's the main file)
You can change the display file according to what you want to see.

The program is working on Sublime Test 3.2.2

## Bibliography

* Computer Architecture: A Quantitative Approach by David A Patterson and John L. Hennessy
* Explanation of the Tomasulo algorithm by J.R. https://www.youtube.com/watch?v=zS9ngvUQPNM&t=392s
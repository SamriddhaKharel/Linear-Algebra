# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 2023

@author: samdm
"""

def calculate_l1_loss(u, v):
    
    return sum(abs(u_i - v_i) for u_i, v_i in zip(u, v))


def calculate_l2_loss(u, v):
   
    return sum((u_i - v_i)**2 for u_i, v_i in zip(u, v))


import random
u = [random.randint(1, 5) for _ in range(5)]
v = [random.randint(1, 6) for _ in range(5)]
print(f"u: {u}")
print(f"v: {v}")

l1_loss = calculate_l1_loss(u, v)
print(f"L1 loss: {l1_loss}")

l2_loss = calculate_l2_loss(u, v)
print(f"L2 loss: {l2_loss}")

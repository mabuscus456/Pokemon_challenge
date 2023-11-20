# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:21:50 2023

@author: mrsch
"""

import pypokedex
import random 
from flask import Flask
from flask import request 

app = Flask(__name__)

random_num = random.randrange(1, 999)

p = pypokedex.get(dex=random_num)

weight = p.weight/10

@app.route("/")
def index():
    return p.types, "weight"
'''    height = p.height / 10
    return print(f'{height} g')
        
    return print("Can you guess the random pokemon?\n")'''

    
@app.route('/fisting')
def index():
    User_guess = request.args.get('guess', "")
    return (
        """<form action="" method="get">
                <input type="text" name="guess">
                <input type="submit" value="Submit">
            </form>"""
            + User_guess)
        
'''@app.route("/<User_guess>")
def guess_validation(User_guess):    
    ug = pypokedex.get(name= User_guess)
        
    if ug.name == p.name :
        print("Congrats! You got it!")
    else:
        print("Try Again")
        pass
        
    print(p.abilities)
        
    prompt = "Can you guess the random pokemon now?\n"
        
    User_guess = input(prompt)
        
    ug = pypokedex.get(name= User_guess)
        
    if ug.name == p.name :
        print("Congrats! You got it!")
    else:
        pass
        
    print(p.base_stats)
        
    prompt = "Can you guess the random pokemon now?\n"
        
    User_guess = input(prompt)
        
    ug = pypokedex.get(name= User_guess)
        
    if ug.name == p.name :
        print("Congrats! You got it!")
    else:
        pass
        
    print(p.sprites)
        
    prompt = "Can you guess the random pokemon now?\n"
        
    User_guess = input(prompt)
    
    ug = pypokedex.get(name= User_guess)
    
    if ug.name == p.name :
        print("Congrats! You got it!")
    else:
        pass
    '''
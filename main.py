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

# Function to generate a new random Pokemon
def get_random_pokemon():
    random_num = random.randrange(1, 999)
    return pypokedex.get(dex=random_num)

# Initialize the game with a random Pokemon
p = get_random_pokemon()
print(p.name)

# Define a route for the root ("/") URL
@app.route("/")
def index():
    # Display initial information about the Pokemon and the guessing form
    return f"Guess the Pokemon's type: {', '.join(p.types)}<br>Weight: {p.weight/10} kg<br><br>" \
           "<form action='/guess' method='post'>" \
           "<label for='guess'>Enter your guess:</label>" \
           "<input type='text' name='guess' id='guess' required>" \
           "<input type='submit' value='Submit'>" \
           "</form>"

# Define a route for the "/guess" URL
@app.route('/guess', methods=['POST'])
def guess():
    global p  # Declare 'p' as a global variable

    # Retrieve the user's guess from the form
    user_guess = request.form.get('guess', "").strip()

    # Check if the user's guess matches the Pokemon's type and weight
    if user_guess.lower() == p.name.lower():
        response = "Congratulations! Your guess is correct."
        p = get_random_pokemon()  # Generate a new random Pokemon for the next round
    else:
        # Provide a hint about the Pokemon's type and weight
        response = f"Sorry, your guess '{user_guess}' is incorrect. Try again.\n"
        response += f"Type: {', '.join(p.types)}\n"
        response += f"Weight: {p.weight/10} kg"

    # Display the response and a link to play again
    return f"{response}<br><br><a href='/'>Play Again</a>"

if __name__ == '__main__':
    app.run()



#My initial idea of an approach for the concept of giving the user more information with each wrong guess:
"""
hints = [f"Hint 1: The pokemon is a(n) {p.type} type Pokemon.",
         "Hint 2: Pokemon has a base Attack stat of {p.base_stats[0]}.",
         "Hint 3: The pokemon's hidden ability is {p.abilities[0]}"]

current_hint_index = 0

Then go on to increment the current hint index with each wrong guess. THus compounding the information they have."""





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

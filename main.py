# Candidate Verification System
from pyscript import display, document

def verify_name(e):
    document.getElementById('result').innerHTML = '' # clears div tag
    firstname = document.getElementById('first_name').value.lower().strip()
    surname = document.getElementById('last_name').value.lower().strip()

    members = ['alexa agnote', 'georgina sarmiento', 'cedric visorde', 'miela eusebio', 'santiago', 'aisha padua'] # listing accepted names of members
    name = firstname + " " + surname # concatenating firstname + surname
    member_checker = name in members # checks if the name is accepted

    display_message = (f'Sorry {name}, your name is not on the list.', f'Congratulations {name}! You are now part of the CommArts Club.') # displaying output
    display(display_message[member_checker], target='result')
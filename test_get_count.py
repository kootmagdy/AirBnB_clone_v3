#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

# Get all states
states = storage.all(State)

# Check if there are any states
if states:
    # Get the first state
    first_state_id = list(states.values())[0].id
    print("First state: {}".format(storage.get(State, first_state_id)))
else:
    print("No states found in the database.")

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

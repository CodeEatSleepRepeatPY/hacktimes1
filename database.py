import pickle
import utils

users = {}

def add(username, password):
    users[username] = utils.hash(password_hash)

def validate(provided_username, provided_password):
    if users[provided_username] == utils.hash(provided_password_hash):
        return True
    else:
        return False

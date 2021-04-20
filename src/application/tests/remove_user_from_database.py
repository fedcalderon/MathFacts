"""This file should only be used when a user needs to be removed for testing purposes.
WARNING: Be careful as to which user you are removing!"""
import src.application.models.database as database


username = 'andy'
password = 'password'

print(database.remove_user(username, password))

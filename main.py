"""The Candidate should build a CRUD application in a Python web framework, that allows a user to login using the Oauth protocol, with github as the provider.

Once logged in, they must be able to create/edit/delete/update their personal

profile, e.g, name, past and actual address, phone number etc.

- Please make sure the repository for the project is publicly hosted on github

- Please make it easy to build, test and run your application

The project review will focus on the following points:

- Clarity and intent within both production code, and test suites

- Predictability of system behaviour

- The amount of code written (less is more)

- Coding standards

- Ease of setup/running"""
from modules.api.app import start_app

if __name__ == "__main__":

    start_app()


#TODO: Create initial user afte rgithub login
#TODO: Update json schema for user
#TODO: test with db


"""Concerns: 
the user should update their personal profile? is that mean they should have update their information on 
github: atm change github information looks  not possible by the github api, got error which not covered in the api 
documentation(can be done with selenium I think but didn't try ) and if it's the case what create from crud should 
does? 
Or just upload their information to the app and the app will store it in the db? I have implemented this way, 
and they also can create new users and update their information."""



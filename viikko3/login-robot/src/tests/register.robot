*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kale  kalle122
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle122
    Output Should Contain  Username is taken

Register With Too Short Username And Valid Password
    Input Credentials  ke  kalle122
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle1  kalle122
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  kall  kalle1
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kall  kalletest
    Output Should Contain  Password must contain numbers
    

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  kale
    Set Password  kalle122
    Set Password Confirmation  kalle122
    Submit Credentials
    Register Should Succeed 

Register With Too Short Username And Valid Password
    Set Username  ke
    Set Password  kalle122
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Invalid Password
    Set Username  kall
    Set Password  kalle1
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  kall
    Set Password  kalle1112
    Set Password Confirmation  kalle112
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registrationx
    Set Username  kale
    Set Password  kalle122
    Set Password Confirmation  kalle122
    Submit Credentials
    Register Should Succeed
    Log Out
    Go To Login page
    Set Username  kale
    Set Password  kalle122
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  kall
    Set Password  kalle1112
    Set Password Confirmation  kalle112
    Submit Credentials
    Register Should Fail With Message  Passwords do not match
    Go To Login page
    Set Username  kall
    Set Password  kalle11122
    Submit Login
    Login Should Fail With Message  Invalid username or password

    

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Submit Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Log Out
    Go To Main Page
    Click Button  Logout
    Go to Login Page

Submit Login
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
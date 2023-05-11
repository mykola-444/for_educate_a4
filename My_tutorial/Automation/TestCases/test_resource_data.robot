*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/Resorces.robot

*** Variables ***


*** Test Cases ***
Robot First Test Case
    Start Browser and Maximize
    Input text  name:jform[name]  TestingWorld
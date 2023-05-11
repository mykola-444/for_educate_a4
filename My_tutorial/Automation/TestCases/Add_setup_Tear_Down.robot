*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/Resources2.robot

*** Variables ***
${URL}  https://www.thetestingworld.com/index.php?option=com_users&view=registration&Itemid=588
${Browser}  Chrome

*** Test Cases ***
Robot First Test Case
    [Setup]  Start Browser and Maximize
    [Teardown]  Close Browser Window
    Input text  name:jform[name]  TestingWorld
    Input text  jform[email1]  fgtr@jhghty.com
    Input text  jform[password1]  89766

Robot Second Test Case
    [Setup]  Start Browser and Maximize
    [Teardown]  Close Browser Window
    Input text  name:jform[name]  TestingWorld

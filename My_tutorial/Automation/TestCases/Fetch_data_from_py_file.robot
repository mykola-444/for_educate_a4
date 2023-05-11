*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/Resorces3.robot

*** Variables ***
${URL}  https://www.thetestingworld.com/index.php?option=com_users&view=registration&Itemid=588
${Browser}  Chrome

*** Test Cases ***
Robot Featch Data
    Concatenate Username and Password  Testing  World
    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window
    # ${ActualURL}=  Get Location
    #Log  ${ActualURL}
    #${PageHTML}=  Get Source
    #Log  ${PageHTML}
    #${Attr}=  Get Element Attribute  name:jform[name]  class
    #Log  ${Attr}
    #${cnt}=  Get Element Count  class:field
    #Log  ${cnt}
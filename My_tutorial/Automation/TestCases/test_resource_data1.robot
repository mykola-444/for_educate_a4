*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/Resorces1.robot

*** Variables ***
${URL}  https://www.thetestingworld.com/index.php?option=com_users&view=registration&Itemid=588
${Browser}  Chrome

*** Test Cases ***
Robot First Test Case
    ${Res}=  Start Browser and Maximize  ${URL}  ${Browser}
    Log  ${Res}
    #Start Browser and Maximize  ${URL}  ${Browser}
    Input text  name:jform[name]  ${Res}

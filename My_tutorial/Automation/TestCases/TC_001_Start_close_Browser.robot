*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Browser}  Chrome
${URL}  https://www.thetestingworld.com/index.php?option=com_users&view=registration&Itemid=588

*** Test Cases ***
Robot First Test Case
    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window
    Input text  name:jform[name]  TestingWorld
    Input text  jform[email1]  fgtr@jhghty.com
    Input text  jform[password1]  89766
    Input text  jform[password2]  89766
    Input text  xpath://input[@name='jform[email2]']  fgtr@jhghty.com
    Clear Element Text  name=jform[name]
    #Close Browser
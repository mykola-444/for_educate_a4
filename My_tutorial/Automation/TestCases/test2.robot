*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${Browser}  Chrome
#${URL}  http://www.facebook.com
${URL}  https://www.thetestingworld.com/index.php?option=com_users&view=login&Itemid=587

*** Test Cases ***
Robot First Test Case
    Open Browser  ${URL}  ${Browser}
    Select Checkbox  remember
    #Maximize Browser Window
    #Select Radio Button  sex  -1
    #Input text  name:jform[name]  TestingWorld
    #Input text  jform[email1]  fgtr@jhghty.com
    #Input text  jform[password1]  89766
    #Input text  jform[password2]  89766
    #Input text  xpath://input[@name='jform[email2]']  fgtr@jhghty.com
    #Clear Element Text  name=jform[name]
    #Close Browser
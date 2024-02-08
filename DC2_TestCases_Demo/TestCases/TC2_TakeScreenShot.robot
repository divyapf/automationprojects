*** Settings ***
Library     RPA.Windows

*** Test Cases ***
Open DC2 application
	Windows Run    dolphicam2.exe
	Set Wait Time   2
	Control Window  executable:dolphicam2.exe
	Set Wait Time   2
	Click   name:INSPECTION

Take Screenshot of DC2
    Screenshot    name:INSPECTION    inspection.png
    ${element}=    Get Element     name:INSPECTION
    Log To Console     ${element.name}
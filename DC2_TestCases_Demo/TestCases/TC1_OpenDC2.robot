*** Settings ***
Library     RPA.Windows


*** Test Cases ***
Open DC2 application
	Windows Run    dolphicam2.exe
	Set Wait Time   2
	Control Window  executable:dolphicam2.exe
	Set Wait Time   2
	Click   name:INSPECTION


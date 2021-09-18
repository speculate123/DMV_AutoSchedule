# DMV_AutoSchedule

The Version of the chromedriver in this repository is 88, if your chrome browser version does not match with this driver, please download from the link below.

https://chromedriver.chromium.org/downloads

This is a auto scheduling program which will auto schedule an NJ DMV appoinment with your desire configuration.

https://telegov.njportal.com/njmvc/AppointmentWizard

At the beginning of the code, you can set up your appointment type, prefered DMV, prefered starting and end time, your information. The program will keep refresh the website every 15 seconds see whether there is time that suits you until found.

Once it finds a time that you want, this program will automaticaly redirect to the reservation page, fill in your information and reserve an appointment. Please note that you can't make an appointment if you already have an appointment cause DMV website won't allow two appointments under same information.

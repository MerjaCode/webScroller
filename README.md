# How to install dependencies for web scroller

This tutorial will guide you through the process of install all of the depedencies to run web_scroller.py on  
Windows 10, by the end you should have google chrome, chromewebdriver, python 3.8.x, and selenium  
installed.
<p>&nbsp;</p>

## Google Chrome installation
---
Use the default web browser to go to this [link](https://www.google.com/chrome/). Click on the download button and follow the  
instructions to install Google Chrome. 
<p>&nbsp;</p>

## Chrome driver download
---
Use a Google Chrome to seach "chrome://version" in the search bar. Find the version number,   
![](./chromeversion.png)  
This is found next to **Google Chrome**. Next go to this [link](https://sites.google.com/chromium.org/driver/downloads)
and download the chromedriver that matches  
your chrome version. Make sure to put it somewhere you can find it again...  
**NOT THE DOWNLOADS FOLDER**.   

After downloading it, use the the search bar in the bottom left to search "environment variables" click on  
the first suggestion. After that, click the environment variables button near the bottom. In the box at the  
top, click on path, then the edit button. Select the new button, then the browse button. Find the folder  
that you downloaded chromedriver in and then click ok.  

Using the search bar again, type "cmd" and select the first suggestion. In that command prompt type  
"chromedriver" and press enter. If this ends in an error, make sure that chromedriver is in the folder you  
added to the path environment variable. If it doesn't end with an error you can move on.
<p>&nbsp;</p>

## Python 3.8 installation
---
Use a web browser to go this [link](https://www.python.org/downloads/release/python-387/), 
scroll all the way down to **Files**, then select ***Windows Installler (64-bit)***  
After it downloads find it with the file explorer and run the executable. In the first page make sure to  
select **Add to PATH**. Then click Recommended install. Follow the rest of the instructions to install  
Python and pip.
<p>&nbsp;</p>

## Install Selenium
---
Open a command prompt by using the search bar at the bottom left and searching cmd. In the command  
prompt type "pip3 install selenium" if it doesn't crash with an error you have successfully installed all of  
the required dependencies for this program.
<p>&nbsp;</p>

## Run web_scroller.py
---
Before you run this file you will have to edit it and add your username and password for the weather  
station. Just scroll down to lines 47 and 48 and change the strings to your username and password.  

Now open a command prompt and cd to the directory this program is in. Once you are there type  

### python3 web_scroller.py

If there are no errors, you have successfully completed the installation and execution of the web scroller.
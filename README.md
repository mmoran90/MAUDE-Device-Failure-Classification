# MAUDE Device Failure Classification

### Installation
To use this project, navigate to where you would like the repo cloned on your machine. Then clone the repo on your device using the commands below:

'git clone https://github.com/mmoran90/ADS-509-Text-Mining.git'
</br>
</br>

### Running the Flask Application
After the repo has been cloned, perform the following steps
   - Open a command prompt (windows) or terminal (Linux/MacOS) and navigate to where the repo was cloned
   - Ensure python3 is installed on your machine (python --version)
     - If python3 is not installed, please do so now  
   - Execute `python app.exe` from command prompt/terminal
     - `app.exe` utiliztes localhost (127.0.0.1 in IPv4)
   - Open a browser and navigate to localhost or `ctrl + click` the link in the command prompt or terminal window

</br>
Now enter any or all fields in the webpage, where the application can predict the most likely medical device failure.
</br>
Additionally, the results of our optimal model can be seen in the models tab at the top of the webpage 
</br>
</br>


### Contributor(s)
* [Marvin Moran](https://github.com/mmoran90)
* [Katie Mears](https://github.com/KatieMears628)
* [Ben Ogle](https://github.com/dsklnr)
</br>

### Methods
Data collection via Webscraping 
</br>

### Technologies
- Selenium 

- SVM

- XGBoost 

- Flask

- HTML

- CSS

</br>

### Problem Statement
The process of applying reported device codes to medical device complaints received from the field is highly manual and time-consuming. 
This leads to inefficiencies, increased chances of human error, and delays in addressing complaints, which can ultimately impact patient safety and regulatory compliance.

Challenges:

- High Volume of Complaints: The influx of complaints can overwhelm staff, leading to backlogs.
- Manual Coding Errors: Human errors in coding can lead to incorrect device codes being applied, affecting data accuracy and regulatory reporting.
- Inconsistent Coding Practices: Variability in how different staff members apply codes can lead to inconsistencies and confusion.
- Time Consumption: The manual process is resource-intensive, diverting staff from more critical tasks.
</br>

### Goals
Develop an automated solution that streamlines the coding process for medical device complaints, ensuring timely, accurate, and consistent application of device codes.
</br>
</br>

### Troubleshooting Flask
You might encounter issues where your interpreter cannot find libraries that are already installed on your machine. If that happens, create a local virtual environment. Below are steps to do so.
</br>
  - Windows
    - Create a new virtual environment
      - `python -m venv myenv`
    - Activate the virtual environment
      - `myenv\Scripts\activate`
  - MacOS/Linux
    - Create a new virtual environment
      - `python -m venv myenv`
    - Activate the virtual environment
      - `source myenv/bin/activate`
      
Now use `pip install <library>` for any missing libraries in your virtual environment
</br>
</br>

### Data Sources
The FDA's MAUDE (Manufacturer and User Facility Device Experience) Database 

https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmaude/search.cfm

# Text to Speech using python 

This is a basic python mirco-project done using Text to Speech Library.

It includes the GUI and CLI version of code in which it both runs on the "pyttsx3" Library

## Installation of TTS library

To install and set up the `pyttsx3` text-to-speech library in Python:

1. Install the library using pip:
   ```
   pip install pyttsx3
   ```

2. Import the library into your script:
   ```python
   import pyttsx3
   ```

3. Initialize the TTS engine:
   ```python
   engine = pyttsx3.init()
   ```

4. Optionally, configure the engine settings:
   ```python
   engine.setProperty('rate', 150)  # Adjust speech rate
   engine.setProperty('volume', 0.9)  # Adjust volume
   engine.setProperty('voice', 'english')  # Select voice
   ```

5. Use the `say()` method to convert text to speech:
   ```python
   engine.say("Hello, world!")
   engine.runAndWait()
   ```

Ensure any necessary dependencies, such as the Microsoft Speech API (SAPI) on Windows, are installed and configured for the library to work correctly.


## Screenshots

This is a basic python script that can be run on the terminal.

![App Screenshot](https://via.placeholder.com/468x30![Screenshot 2024-08-31 142012](https://github.com/user-attachments/assets/ccbbd429-acfe-459c-b1ae-4a45267b1eda)
0?text=App+Screenshot+Here)

This is the GUI veersion of above python code that made using the integration of Tkinter Library generally used to make GUI in python.

![App Screenshot](https://via.placeholder.com/468x![Screenshot 2024-08-31 135238](https://github.com/user-attachments/assets/31f9ce0d-d8be-44ec-89a5-338b5dba7ac9)
300?text=App+Screenshot+Here)

## How to Run CLI version 

NOTE : 

```bash
  Enter the speed of voice [eg.(1x= 120)|(0.5x= 200)|(2x= 400)]:
```
This LOC in "TextToSpeechCLI.py" is used to adjust the speed of the speech the example is given in the line itself. 



# Image Sorter
This is a tool written in Python 3.9 with the tkinter library for GUI implementation. It will sort image files into other locations based on how the images are named. The tool allows for customization of save location and sort method, plus it can save user settings between uses. This was intended for artists who download reference images from the web in large volumes and find themselves with a lot of work when it's time to sort these images for ease of access. 

## Usage
Download the executable and run. The following window appears:
<br>
<p align="center" width="100%">
  <img src="images/imagesorter_window.png?raw=true" alt="Image Sorter window">
</p>

1. Main Folder Location
   > Choose the location of the main folder that sorted images will be placed in. Any image categories will be created as subfolders in this main folder.
2. Main Folder Name
   > Name the main folder. If the name of an already existing folder is selected, the images will be moved to this folder.
3. Find Images to Sort
   > Choose the location of the images that require sorting.
4. Category Number
   > Choose the number of categories (between 1 and 20) that images will be sorted into. The window will dynamically update with fields below this dropdown to accommodate.
5. Image Prefix and Category Name
   > Fill in categories that images with the correct prefix will be sorted into. For example, a_skull.png will be sorted into the Images/Anatomy folder with these settings. If fields are left blank, the images will be deposited in the main folder without being categorized.
6. Saving User Preferences
   > Press the Save Prefs button to save a .txt file in the same location as the executable. This allows the executable to remember user settings the next time it is opened. Keep the executable and the settings .txt in the same directory.
7. Returning to Default Preferences
   > Press the Default Prefs button to remove the settings .txt and reset the window to default settings.
8. Running Image Sorter
   > Press the Sort Images button to sort according to the current input in the window.
9. Quit
   > Press the Quit button to close the program.

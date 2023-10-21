# Auto Font Installer

## Description

This app is a stand-alone executable that automatically looks for and installs all font files in a directory. Simply unzip your fonts, and place them all in one folder. Don't worry if the folders are nested or not. Auto Font Installer will look through the designated directory and all nested folders and will copy any common font file to the Windows Font Directory.

Due to the nature of its task, it needs Admin privileges to access the Windows Font Directory. Therefore, a popup will appear asking for admin rights when you run this application.

## Files

* `build/font_installer`: Application build files
* `dist`: Packaging and distribution related files
* `src`: Source files of this project
* `.gitattributes & .gitignore`: Configuration files for git

## Usage

Follow these steps to successfully install your font files:
1. Download and unzip the font files you want to install. 
2. Place all the unzipped font files/folders in one folder to act as the directory.
3. Run the `build/font_installer` application.
4. On running the application, you will be asked for admin privileges. Grant them to allow the application to install your fonts.

## Disclaimer

This code is provided "as is" without warranties or conditions of any kind, either express or implied. Any unwarranted usage of this code or damages caused from its usage is not intended or the responsibility of the author.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

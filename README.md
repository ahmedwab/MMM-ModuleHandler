# Module: MMM-ModuleHandler [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The `MMM-ModuleHandler` application retrieves and deletes any desired module found on the https://github.com/MichMich/MagicMirror/wiki/3rd-party-modules website

<img src="screenshot.png" alt="Menu">

## Installing the Application
Access your /Magic Mirror folder
```sh
cd ~/MagicMirror/
```
Clone this repository in the modules folder
```sh
git clone https://github.com/ahmedwab/MMM-ModuleHandler
```

## Installing the Application

Ensure that you have the Latest Version of Python 3 installed.
That could be retrieved from https://www.python.org/downloads/

Moreover, to install all the dependencies you can do the following
```sh
	cd ~/MagicMirror/MMM-ModuleHandler
	bash dependencies.sh

```


## Running the application 

To run the application, you must navigate to the application folder 
```sh
cd ~/MagicMirror/MMM-ModuleHandler
```
Then, you can run it using the following command
```sh
pyhton3 controls.py
```
## Using the application

The Menu will look as follows:

<img src="screenshot.png" alt="Menu">
 
You will need to input the module name Example: MMM-TranslatedMessages
  
Then select add or remove

What the application will do:

1. Install the module in the modules folder.
2. Download all the dependenices reuqired
3. Add a generic config similar to the photo below

<img src="screenshot2.png" alt="config">

	



## Project Status

As of now, the application is completed.

Although, any suggestions or changes is highly encouraged.




## Contributing

Contributing is greatly encouraged.

1. Fork the Project
2. Create your Feature Branch 
3. Commit your Changes 
4. Push to the Branch 
5. Open a Pull Request




## License

Distributed under the MIT License. See `LICENSE` for more information.

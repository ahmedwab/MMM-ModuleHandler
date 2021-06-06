# Module: MMM-ModuleHandler

The `MMM-ModuleHandler` module retrieves and deletes any desired module found on the https://github.com/MichMich/MagicMirror/wiki/3rd-party-modules website


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

Moreover, the following dependencies are needed
```sh
	pip3 install requests
	pip3 install re
	pip3 install BeautifulSoup

```


	
	


## Running the application 

To run the application, you must navigate to the application folder 
```sh
cd ~/MagicMirror/MMM-ModuleHandler
```
Then, you can run it using the following command
```sh
pyhton3 MMM-ModuleHandler.py
```
## Using the application

The Menu will display the following options
```sh
Select an option: 

 Add
 Remove
 Quit 

```	
You can type any of the options available

Example: Add

When prompted for a Module name, you can simply input the module name 
Example: MMM-TranslateMessages
The Application will install the module folder limited to the Modules available on https://github.com/MichMich/MagicMirror/wiki/3rd-party-modules.
	



## Project Status

As of now, the application is unable to automatically install the configurations for each installed module.

That could be manually installed using the config/config.js file




## Contributing

Contributing is greatly encouraged.

1. Fork the Project
2. Create your Feature Branch 
3. Commit your Changes 
4. Push to the Branch 
5. Open a Pull Request




## License

Distributed under the MIT License. See `LICENSE` for more information.

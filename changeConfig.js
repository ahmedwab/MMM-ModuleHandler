/* changeConfig
* Author: ahmedwab
* June 2021
*/
const config = require('../config/config.js');
const fs = require('fs');



var myArgs = process.argv.slice(2);
var change = myArgs[0]
var moduleName =myArgs[1];


function addModule(){

    mduleContainer= {module: moduleName,
    position: 'top_right'}
    moduleIndex = config.modules.findIndex(element => element.module == moduleName);
    if( moduleIndex==-1)
        config.modules.push(mduleContainer);
    

}
function removeModule(){

    moduleIndex = config.modules.findIndex(element => element.module == moduleName);
    if( moduleIndex!=-1)
        config.modules.splice(moduleIndex,1)
   

}


if (change=='add'){
    addModule()
}

else if (change=='remove'){
    removeModule()
}

fs.readFile('../config/config.js', 'utf8', function(err, data){
      
    var s = data;
    str = s.split("modules:");
    var end = " /*************** DO NOT EDIT THE LINE BELOW ***************\/ \n if (typeof module !== \"undefined\") {module.exports = config;}";
    configModules = JSON.stringify(config.modules, null, '\t');
    configModules = configModules.replace(/"([^"]+)":/g, '$1:');
    newconfigFile =str[0]+"modules:  \n \t \t" + configModules +" \n }; \n" +end;
    fs.writeFile('../config/config.js', newconfigFile, function (err) {
        if (err) return console.log(err);
        console.log('Configuration file has been changed');
      });
});




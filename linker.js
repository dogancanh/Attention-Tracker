const electron =require("electron");
const {ipcRenderer} = electron;

var idnum;
var course;
ipcRenderer.on("usrid",(event, idvalue) => {
    console.log(idvalue)
     idnum = idvalue;
})
ipcRenderer.on("usrcrs",(event, args) =>{
    course=args
} )

function get_face() {

    console.log(idnum)
    let {PythonShell} = require('python-shell')
    var path = require("path")


    var options = {
        scriptPath: path.join(__dirname, './'),
        pythonPath: 'C:/Users/dhird/AppData/Local/Programs/Python/Python37/python.exe',
        args: [idnum,course]
    };
    PythonShell.run('yuzbulanson.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
    });
}

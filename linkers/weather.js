function get_weather() {

  document.getElementById("city").value = "Hang on..."
  var python = require("python-shell")
  var path = require("path")

  var options = {
    scriptPath : path.join(__dirname, '/../engine/'),
    pythonPath : 'usr/local/bin/python3'
  }

  var record = new python("record-video-480.py", options);

  // record.end(function(err,code,message){
  //   document.getElementById("city").value = "Detect faces";
  // })

} 
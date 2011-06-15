#!/usr/bin/env node
var http = require("http");

var handle = function(req, res) {
  res.writeHead(200, {"Content-Type": "application/json"});
  
  var data = ""
  
  req.on("data", function(chunk) { s += chunk; });
  req.on("end", function() {
    var request = {};
    
    try {
      request = JSON.parse(data);
      
      var result = eval(result.parse[0]);
      
      var response_data = JSON.stringify({
        "result": result,
        "error": null, 
        "id": request.id
      })
    } catch(error) {
      var response_data = JSON.stringify({
        "result": null,
        "error": String(error),
        "id": request.id
      })
    }
    
    res.end(response_data);
  })
}

var port = process.argv[2] || Math.floor(49152 + Math.random() *
                                                 (65535 - 49152 + 1));

http.createServer(handle).listen(port, "localhost");

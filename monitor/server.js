const express = require("express")
const morgan = require("morgan")
const app = express()
const path = require("path")

app.use(morgan("combined"))
app.use(express.static('build/static'));
app.use(express.static('static'));

app.get("/", function(req, res) {
  res.sendFile(path.resolve("./build/index.html"))
});

var server = app.listen(3000, function(){
  console.log("Node.js is listening to PORT:" + server.address().port);
});
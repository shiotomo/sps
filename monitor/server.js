const http = require('http');
const fs = require('fs');

const port = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  const url = "./build" + (req.url.endsWith("/") ? req.url + "index.html" : req.url);

  if (fs.existsSync(url)) {
    fs.readFile(url, (err, data) => {
      if (!err) {
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(data);
      }
    });
  }
});

server.listen(port, () => {
    console.log("To view your app, open this link in your browser: http://localhost:" + port);
});
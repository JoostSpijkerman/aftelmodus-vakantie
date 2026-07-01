const http = require("http");
const fs = require("fs");
const path = require("path");

const root = path.join(__dirname, "..");
const port = 8791;

const types = {
  ".html": "text/html",
  ".json": "application/json",
  ".js": "text/javascript",
  ".png": "image/png"
};

http.createServer((req, res) => {
  let filePath = path.join(root, decodeURIComponent(req.url.split("?")[0]));
  if (filePath.endsWith("/")) filePath = path.join(filePath, "index.html");

  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.writeHead(404);
      res.end("Not found");
      return;
    }
    const ext = path.extname(filePath);
    res.writeHead(200, { "Content-Type": types[ext] || "application/octet-stream" });
    res.end(data);
  });
}).listen(port, () => {
  console.log(`Static server running on http://localhost:${port}`);
});

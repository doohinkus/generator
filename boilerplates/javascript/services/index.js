"use strict";

var fs = require("fs");
var path = require("path");

module.exports = {
  get: function(models) {
    var services = {};

    fs.readdirSync(
      __dirname
    ).filter(function(file) {
      return(file.indexOf(".") !== 0) && (file !== "index.js");
    }).forEach(function(file) {
      var service = require(path.join(__dirname, file))(models);
      services[service.name] = service.methods;
    });

    return services;
  }
}

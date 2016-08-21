"use strict";

var fs = require("fs");
var path = require("path");
var Controller = require(path.join(__dirname, "Controller.js"));

module.exports = {
  get: function(Services, restify) {
    var controllers = [];

    fs.readdirSync(
      __dirname
    ).filter(function(file) {
      return (file.indexOf(".") !== 0) && (file !== "index.js") && (file !== "Controller.js");
    }).forEach(function(file) {
      var controller = require(path.join(__dirname, file))(Controller, Services, restify);
      controllers.push(controller);
    });

    return controllers;
  }
}

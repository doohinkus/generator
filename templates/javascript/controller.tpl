"use strict";

module.exports = function(Controller, Services, restify) {
  var controller = Controller("/{{ name|lower }}");
  controller.get("", function(req, res, next) {
    Services.{{ name }}Service.findAll().then(function({{ name|lower }}s) {
      res.setHeader("content-type", "application/json");
      res.send({{ name|lower }}s);
      next();
    });
  });
  controller.get("/:id", function(req, res, next) {
    Services.{{ name }}Service.findById(req.params.id).then(function({{ name|lower }}) {
      if({{ name|lower }} == null) {
        next(new restify.NotFoundError("{{ name|lower }} not found"));
        return;
      }
      res.setHeader("content-type", "application/json");
      res.send({{ name|lower }});
      next();
    });
  });
  return controller;
}

"use strict";

var _controller = function Controller(base) {
  this.base = base || "";
  this.getEndpoints = {};
  this.postEndpoints = {};
  this.putEndpoints = {};
  this.delEndpoints = {};
};

_controller.prototype.get = function(path, handler) {
  this.getEndpoints[path] = handler;
}

_controller.prototype.post = function(path, handler) {
  this.postEndpoints[path] = handler;
}

_controller.prototype.put = function(path, handler) {
  this.putEndpoints[path] = handler;
}

_controller.prototype.delete = function(path, handler) {
  this.delEndpoints[path] = handler;
}

_controller.prototype.register = function(server) {
  var methods = ["get", "post", "put", "del"]
  for(var i in methods) {
    var method = methods[i];
    for(var path in this[method + "Endpoints"]) {
      server[method](this.base + path, this[method+"Endpoints"][path]);
    }
  }
}

module.exports = function(base) {
  return new _controller(base);
}

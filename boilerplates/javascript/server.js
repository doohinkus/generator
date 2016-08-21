var restify = require("restify");
var serveStatic = require('serve-static-restify');
var models = require("./models");
var services = require("./services").get(models.models);
var controllers = require("./controllers").get(services, restify);
var initialize = require("./util/initialize");

var server = restify.createServer();
server.use(restify.bodyParser({mapParams: false}));
server.pre(serveStatic('public', {'index': "index.html"}));
for(var i in controllers) {
  controllers[i].register(server);
}

module.exports = {
  start: function() {
    models.sequelize.sync().then(function() {
      return initialize(models.models);
    }).then(function() {
      server.listen(8080, function() {
        console.log("%s listening at %s", server.name, server.url);
      });
    });
  }
};

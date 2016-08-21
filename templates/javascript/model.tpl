"use strict";

module.exports = function(sequelize, DataTypes) {
  var {{ name }} = sequelize.define("{{ name }}", {
    {% for field in fields %}{{field.name}}: {{field.dataType}}{% if not loop.last %},{% endif %}
    {% endfor %}
  }, {
    timestamps: false,
    classMethods: {
      associate: function(models) {
        // to be implemented
      }
    }
  });

  return {{ name }};
}

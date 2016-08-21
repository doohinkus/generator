"use strict";

module.exports = function(models) {
  return {
    name: "{{ name }}Service",
    methods: {
      findById: function(id) {
        if(typeof(id) === "string") {
          return this.findById(parseInt(id));
        }
        return models.{{ name }}.findById(id);
      },
      findAll: function() {
        return models.{{ name }}.findAll();
      }
    }
  };
}

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
      },
      save: function({{ name|lower }}) {
        return models.{{ name }}.create({{ name|lower }});
      },
      update: function({{ name|lower }}Id, {{ name|lower }}Changes) {
        return this.findById({{ name|lower }}Id).then(function({{ name|lower }}) {
          for(var i in {{ name|lower }}Changes) {
            {{ name|lower }}[i] = {{ name|lower }}Changes[i];
          }
          return {{ name|lower }}.save();
        });
      },
      delete: function({{ name|lower }}Id) {
        return this.findById({{ name|lower }}Id).then(function({{ name|lower }}) {
          if({{ name|lower}} !== null) {
            return {{ name|lower }}.destroy();
          }
        });
      }
    }
  };
}

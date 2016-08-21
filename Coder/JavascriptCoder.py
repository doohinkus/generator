import os
from AbstractCoder import AbstractCoder
from JavascriptSpecifics import JavascriptSpecifics

class JavascriptCoder(AbstractCoder):
    specifics = JavascriptSpecifics()
    def __init__(self):
        AbstractCoder.__init__(self)
        self.modelTemplate = "/javascript/model.tpl"
        self.serviceTemplate = "/javascript/service.tpl"
        self.controllerTemplate = "/javascript/controller.tpl"

    def createBoilerPlate(self, dst_base_path):
        AbstractCoder.createBoilerPlate(self, dst_base_path, "javascript")

    def createModel(self, dst_base_path, entity):
        template = self.templateEnv.get_template(self.modelTemplate)
        dst = os.path.join(dst_base_path, "models/" + entity["name"] + ".js")
        self.writeToFile(dst, template.render(entity))

    def createService(self, dst_base_path, entity):
        template = self.templateEnv.get_template(self.serviceTemplate)
        dst = os.path.join(dst_base_path, "services/" + entity["name"] + "Service.js")
        self.writeToFile(dst, template.render(entity))

    def createController(self, dst_base_path, entity):
        template = self.templateEnv.get_template(self.controllerTemplate)
        dst = os.path.join(dst_base_path, "controllers/" + entity["name"] + "Controller.js")
        self.writeToFile(dst, template.render(entity))

    def generateServer(self, dst_base_path, models):
        metadata = self.getMetaData(models, JavascriptCoder.specifics)
        self.createBoilerPlate(dst_base_path)
        for entity in metadata["entities"]:
            self.createModel(dst_base_path, entity)
            self.createService(dst_base_path, entity)
            self.createController(dst_base_path, entity)

import os
import shutil
import jinja2

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

class AbstractCoder:
    def __init__(self):
        self.templateLoader = jinja2.FileSystemLoader(searchpath="generator/templates")
        self.templateEnv = jinja2.Environment(loader=self.templateLoader)

    def getModulePath(self):
        return os.path.dirname(os.path.abspath(__file__))

    def createBoilerPlate(self, dst_base_path, language):
        src = os.path.join(self.getModulePath(), "../boilerplates/%s" % (language, ))
        copytree(src, dst_base_path)

    def writeToFile(self, dst, contents):
        with open(dst, "wb") as f:
            f.write(contents)

    def getMetaData(self, models, specifics):
        metadata = {"entities" : []}
        for model in models:
            metadata["entities"].append(model.getMetaData(specifics))
        return metadata

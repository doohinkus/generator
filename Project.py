from Coder.JavascriptCoder import JavascriptCoder
from Model import Model, Field

import os
import os.path
import random
import shutil

class Project:
    def __init__(self, name, language, working_dir):
        if(language == "javascript"):
            self.coder = JavascriptCoder()
        else:
            raise LanguageNotSupportedException(language)
        self.name = name
        self.working_dir = working_dir
        self.models = []

    def addModels(self, models):
        for model in models:
            fields = []
            for field in model["fields"]:
                fields.append(Field(field["name"], field["datatype"]))
            self.models.append(Model(model["name"], fields))

    def build(self):
        randomHex = self.createRandomChars()
        dst = os.path.join(self.working_dir, randomHex)
        if not os.path.exists(dst):
            os.makedirs(dst)
            dst_main = os.path.join(dst, self.name)
            os.makedirs(dst_main)
            self.coder.generateServer(dst_main, self.models)
            shutil.make_archive(dst_main, "zip", dst_main)
            zipFileName = dst_main + ".zip"
            shutil.rmtree(dst_main)
            return zipFileName
        else:
            #recursive build if directory exists
            return self.build()

    def createRandomChars(self):
        return ''.join(random.choice('0123456789ABCDEF') for i in range(16))

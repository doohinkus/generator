class Field:
    def __init__(self, name, datatype):
        self.name = name
        self.datatype = datatype

    def getMetaData(self, specifics):
        return {
            "name": self.name,
            "dataType": specifics.getField(self.datatype)
        }

class Model:
    def __init__(self, name, fields=[]):
        self.name = name
        self.fields = fields

    def addField(self, field):
        self.fields.append(field)

    def getMetaData(self, specifics):
        metadata = {
            "name": self.name,
            "fields": []
        }
        for field in self.fields:
            metadata["fields"].append(field.getMetaData(specifics))
        return metadata

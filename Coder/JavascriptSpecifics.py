class JavascriptSpecifics:
    specifics = {
        "string": "DataTypes.STRING",
        "text": "DataTypes.STRING",
        "integer": "DataTypes.INTEGER",
        "boolean": "DataTypes.BOOLEAN",
        "time": "DataTypes.TIME",
        "date": "DataTypes.DATEONLY"
    }

    def getField(self, field):
        return JavascriptSpecifics.specifics[field]

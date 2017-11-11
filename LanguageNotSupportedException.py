class LanguageNotSupportedException(Exception):
    def __init__(self, language):
        self.language = language
        self.msg = "language not supported: " + language

    def __str__(self):
        return self.msg

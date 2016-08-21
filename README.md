#Rest Api Generator

##Usage
```python
import generator.Coder
from generator.Coder.JavascriptCoder import JavascriptCoder
from generator.Model import Model, Field
import os

if __name__ == "__main__":
    coder = JavascriptCoder()
    dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), "working_dir")
    account = Model("Account", [
        Field("username", "string"),
        Field("password", "string"),
        Field("username", "string"),
        Field("password", "string")
    ])
    blog = Model("Blog", [
        Field("title", "string"),
        Field("body", "text"),
        Field("created", "date")
    ])
    coder.generateServer(dst, [account, blog])
```

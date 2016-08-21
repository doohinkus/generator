#Rest Api Generator

##Usage
```python
from generator.Project import Project
import os

if __name__ == "__main__":
    dst = "working_dir"
    project = Project("Blog", "javascript", dst)
    project.addModels([
        {
            "name": "Account",
            "fields": [
                {"name": "username", "datatype": "string"},
                {"name": "password", "datatype": "string"},
                {"name": "firstname", "datatype": "string"},
                {"name": "lastname", "datatype": "string"}
            ]
        },
        {
            "name": "Blog",
            "fields": [
                {"name": "title", "datatype": "string"},
                {"name": "body", "datatype": "text"},
                {"name": "created", "datatype": "date"}
            ]
        }
    ])
    print project.build()
```

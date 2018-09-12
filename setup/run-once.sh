
#!/usr/bin/env bash

apt install python-pip

pip freeze > requirements.txt

pip install -r setup/requirements.txt

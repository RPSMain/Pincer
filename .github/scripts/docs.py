from os import system as do

do("git clone https://github.com/pincer-org/pincer")
do("cd pincer")
do("cd docs")
do("pip install -U furo sphinx sphinx-design sphinxcontrib-trio sphinxcontrib-mermaid")
do("./make html")

## Testing Gitsubmodules

main.py -> main app entry point

static -> static files (css, js, images, etc)

local_templates -> html templates

local_templates->templates folder is a git submodule

to run this project (Python 3.11):

- create a virtual environment
- install requirements.txt
- run "uvicorn main:app --reload" 
- open http://127.0.0.1:8000/testing_template


notes:
- adding submodule in this project:

git submodule add https://github.com/pauloprax/submodule_test.git templates



## Testing Gitsubmodules

main.py -> main app entry point

static -> static files (css, js, images, etc)

templates -> html templates (from another repository)

to run this project (Python 3.11):

- create a virtual environment
- install requirements.txt
- run "uvicorn main:app --reload" 


notes:
- adding submodule in this project:

git submodule add https://github.com/pauloprax/submodule_test.git templates



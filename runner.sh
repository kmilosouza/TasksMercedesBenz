pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
sleep 5
pytest testcases/
deactivate

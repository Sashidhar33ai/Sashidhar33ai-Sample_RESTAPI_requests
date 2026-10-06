## install fastapi
Execute the below commands in cli:
pip install "fastapi[standard]"
pip freeze > requirements.txt

Once we have written code in main.py, we should execute it by running the below command:
fastapi dev main.py

Normally we can see the o/p in http://127.0.0.0/8080
we can see clearly in docs using the link: http://127.0.0.0/8080/docs
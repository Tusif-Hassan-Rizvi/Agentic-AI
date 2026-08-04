

1.Create virtual env
```bash
python -m venv myenv
```


2. Activate env by going to script and copy bash path


3. Check the package list in env

```bash
pip list
```


4. Install any package

```
pip install fastapi uvicorn
```


5. run server

```bash
uvicorn main:app --reload
```


6. To check API Better way 
```bash
http://127.0.0.1:8000/docs
```


7. To dowload alchemy and psycopg2

```bash
pip install sqlalchemy psycopg2 
```
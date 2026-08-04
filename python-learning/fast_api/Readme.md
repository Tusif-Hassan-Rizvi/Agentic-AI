

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
1. Install UV

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```


2. Initialize UV project

```bash
uv init
```


3. Create virtual environment

```bash
uv venv
```


4. activate virtual env

```bash
.venv\Scripts\activate
```



5. create package with virtual env and requirement.txt file

```bash
uv add -r requirement.txt
```


6. create a package for jupeter notebok

```bash
uv add ipykernel
```





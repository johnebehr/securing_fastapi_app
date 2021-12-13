<div style="text-align:center">
<h1>Securing FastAPI App</h1>
<h2>FastAPI Security and Routing</h2>
</div>
<hr style="border: 3px solid #393e46; width:70%; margin:0 auto;">

### Reference
- [Authentication in FastAPI](https://testdriven.io/blog/fastapi-jwt-auth/)

### Setup 
- Start with the following Python libraries: 
    - <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">fastapi==0.70.0</span>
    - <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">uvicorn==0.15.0</span>
    - <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">pycmd==1.2</span>
- ```shell
  $ # Create the following structure
  $ tree
  .
  ├── LICENSE
  ├── README.md
  ├── app
  │   ├── __init__.py
  │   ├── api.py
  │   ├── auth
  │   │   └── __init__.py
  │   └── model.py
  ├── main.py
  └── requirements.txt
  
  2 directories, 8 files
  ```
  - In <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">main.py</span> define an entrypoint for the app
----------------------------------------------------------------------------
<span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;"></span>

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

### Adding Pydantic models (Schemas)
- Add pydantic schemas for data validation to <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">fastapi-jwt.app.model</span>

### Defining the routes
- Start by importing <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">PostSchema</span> then adding a list of dummy posts and an empty user list variable
    - Add some GET routes to read the fake posts
    - Add a POST route for creating a new post

### JWT Authentication
- Create a JWT token handler and a class to handle bearer tokens 
- Add the following libraries:
    - <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">PyJWT==1.7.1</span>
    - <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">python-decouple==3.3</span>
        - Used for reading environment variables
- JWT Handler
    - The JWT handler will be responsible for signing, encoding, decoding, and returning JWT tokens
    - Add a new module <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">app.auth.auth_handler</span>
----------------------------------------------------------------------------
<span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;"></span>

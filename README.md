# Regex Wizard

### Implementation Process

1. **Select Prompt:**
    For this assessment, the prompt under the name "Regex Wizard" was selected from the prompt library. ![prompt image]()
2. **Obtain the Code:**
    The code was obtained from ai studio, by using the "Get Code" option. The code was the pasted int a python file named [`ai.py`](./ai.py).
3. **Obtain API KEY:**
    - The API key was obtained from the ai studio website.
    - The API key was used under the name `GEMINI_API_KEY` in the code.
3. **Develop the Web Interface:**
  - Created a web interface using Python with Dash.
  - This interface allows users to generate regex they wanted.
  - The web interface can be accessed at `http://localhost:8000/`.
  - The env vars `PORT` can be used to change the port on which the application runs.
  -
4. **Dockerization of Application:**
  - For the application, as base image `python:3.12-slim` was used.
  - Dependencies required are listed in the `requirements.txt` file.
  - The Dockerfile was created to install the necessary dependencies and run the application.
  The Docker image was built with the following command:
  ```bash
    docker build -t regex-wizard .
  ```
### Running the Application

1. **Get the API Key:**
    - Get the API key from the ai studio website.

2. **Build the Docker Image:**
    - Build the Docker image using the following command:
    ```bash
    docker build -t regex-wizard .
    ```

3. **Run the Docker Container:**
    - Run the Docker container using the following command:
    ```bash
    docker run -p 8000:8000 -e GEMINI_API_KEY=<API_KEY> regex-wizard
    ```
    - Replace `<API_KEY>` with the API key obtained from the ai studio website.

### Screenshots

![Regex Gen](./imag/regex-gen.png)


![Regex Result](./imag/regex-result.png)

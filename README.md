## Translation service
> * Backend: Python, FastAPI
> * Database: PostgreSQL
> * Frontend: JavaScript, HTML, Bootstrap, Axios
> * Public API: Open AI ChatGPT-4

### Introduction
* A real-time translation service with FastAPI and GPT-4

### Local Build
1. Go to the `app` folder by `cd app`
2. Run `uvicorn main:app --host 0.0.0.0 --port 8000` in the terminal ([Univorn](https://fastapi.tiangolo.com/deployment/manually/) is a production server of FastAPI)
3. Open [http://localhost:8000/index](http://localhost:8000/index)

### Project Structure

```
..
├── app/                                # FastAPI project

├── templates/                          # Front end
           ├── index.html

├── alembic/                            # Handle PostgreSQL database migrations

├── alembic.ini           
├── Dockerfile
├── requirements.txt
```

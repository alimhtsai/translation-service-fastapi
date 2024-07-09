## Translation service
> * Backend: Python, FastAPI
> * Database: PostgreSQL
> * Frontend: JavaScript, HTML, Bootstrap, Axios
> * Public API: Open AI ChatGPT-4

### Introduction
* A real-time translation service with FastAPI and GPT-4

### Local Build
1. Create a virtual environment `.venv` by running `python3 -m venv .venv`
2. Activate the virtual environment by running `source .venv/bin/activate`(to deactivate by running `deactivate`)
3. (If first time building the project) Install dependencies by running `pip install -r requirements.txt`
4. Go to the `app` folder by running `cd app`
5. Open the pgAdmin4, create a new database, add the configuration to the `.env` file
6. Start the Django app by running `uvicorn main:app --host 0.0.0.0 --port 8000` ([Univorn](https://fastapi.tiangolo.com/deployment/manually/) is a production server of FastAPI)
7. The table `translation_tasks` will be automatically created, as specified in the `models.py` file
8. Open [http://localhost:8000/index](http://localhost:8000/index)

### Project Structure

```
..
├── app/                                # FastAPI project

├── templates/                          # Front end
           ├── index.html

├── requirements.txt
```

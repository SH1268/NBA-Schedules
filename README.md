# NBA-Schedules

## Setup

Initialize environment:
```sh
conda create -n schedules-env python=3.8
```

```sh
conda activate schedules-env
```

Install dependencies:
```sh
pip install -r requirements.txt
```


## Usage

Run the schedules report:
```sh
python app/schedules.py
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
export FLASK_APP=web_app
flask run
```

## Testing

Run testing:

```sh 
pytest
```
FROM apache/airflow:latest-python3.9

ENV DAGDIR=/opt/airflow/dags

WORKDIR ${DAGDIR}

COPY requirements.txt .

ENV PYTHON_VENV=/env

RUN python -m venv $PYTHON_VENV 

ENV PATH="$PYTHON_VENV/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "/opt/airflow/dags/main.py" ]

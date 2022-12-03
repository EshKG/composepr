#
# NOTE: THIS DOCKERFILE IS GENERATED VIA "apply-templates.sh"
#
# PLEASE DO NOT EDIT IT DIRECTLY.
#

FROM python:3.9

WORKDIR /servicedb

COPY ./requirements.txt /servicedb/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /servicedb/requirements.txt

# 
COPY ./main.py /servicedb/

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]
ENTRYPOINT ["python3", "main.py"]

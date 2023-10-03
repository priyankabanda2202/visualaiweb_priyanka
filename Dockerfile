# app/Dockerfile

FROM python:3.11

WORKDIR /app

#RUN apt-get update && apt-get install -y \
 #   build-essential \
  #  curl \
   # software-properties-common \
   # git \
   # && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y nodejs \
    npm                       # note this one

#COPY requirements.txt .
#COPY visual_ai_react_ui/ /visual_ai_react_ui
#COPY .streamlit .
#COPY mockedData.py .
#COPY app.py .

COPY . /app/

RUN cd visual_ai_react_ui && npm install
RUN cd visual_ai_react_ui && npm run build

# RUN pip3 install --trusted-host pypi.org --trusted-host --trusted-host pypi.python.org -r requirements.txt

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5005

HEALTHCHECK CMD curl --fail http://localhost:5005/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=5005", "--server.address=0.0.0.0"]
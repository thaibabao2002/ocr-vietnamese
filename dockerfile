FROM public.ecr.aws/lambda/python:3.10

COPY ./requirements.txt .
COPY OCR_VN/ ./OCR_VN
COPY models/ ./models
COPY ./serverless/lambda_function.py ./lambda_function.py

RUN yum install mesa-libGL -y
RUN pip install --upgrade pip

RUN pip install -r requirements.txt
CMD ["lambda_function.handler"] 
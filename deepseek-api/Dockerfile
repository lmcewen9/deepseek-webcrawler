FROM python:3.13

RUN pip install vllm

CMD ["python", "-m", "vllm.entrypoints.openai.api_server", "--model", "deepseek-ai/deepseek-v3"]
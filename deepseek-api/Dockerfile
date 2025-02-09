FROM python:3.11

RUN pip install vllm

EXPOSE 8000

CMD ["python", "-m", "vllm.entrypoints.openai.api_server", "--model", "deepseek-ai/deepseek-v3"]

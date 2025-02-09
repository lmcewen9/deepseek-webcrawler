FROM nvidia/cuda:12.8.0-base-ubuntu22.04

RUN apt-get update && apt-get install -y python3-pip python3-dev
RUN pip3 install torch torchvision vllm

EXPOSE 8000

CMD ["python", "-m", "vllm.entrypoints.openai.api_server", "--model", "deepseek-ai/deepseek-v3", "--gpu-memory-utilization", "0.9"]

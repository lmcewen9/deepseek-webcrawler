FROM nvidia/cuda:12.8.0-devel-ubuntu22.04

RUN apt-get update && apt-get install -y python3-pip python3-dev
RUN pip3 install vllm

EXPOSE 8000

CMD ["python3", "-m", "vllm.entrypoints.api_server", "--model", "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", "--max-model-len", "2048", "--gpu-memory-utilization", "0.9"]

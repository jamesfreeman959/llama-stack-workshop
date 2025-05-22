# Installation and Setup Guide for LLaMA Stack Projects

This guide provides instructions to install Python 3.11, set up two Python projects (`llama-stack-server` and `llama-stack-workshop`) with virtual environments, install Ollama, pull specific LLaMA models, and configure the projects.

## Prerequisites
- A system with a terminal (Linux, macOS, or Windows with WSL).
- Internet access to download packages and models.
- Administrative privileges for installing software.
- A Tavily API key (for the workshop project).

## Step 1: Install Python 3.11
1. **Linux (Ubuntu/Debian-based)**
   ```bash
   sudo apt update
   sudo apt install -y software-properties-common
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt install -y python3.11 python3.11-venv python3.11-dev
   ```
2. **macOS (using Homebrew)**
   ```bash
   brew install python@3.11
   ```
3. **Windows**
   - Download the Python 3.11 installer from [python.org](https://www.python.org/downloads/release/python-3110/).
   - Run the installer, ensuring to check "Add Python 3.11 to PATH."
   - Verify installation:
     ```bash
     python3.11 --version
     ```

## Step 2: Install Ollama
1. Download and install Ollama:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```
2. Verify installation:
   ```bash
   ollama --version
   ```

## Step 3: Pull LLaMA Models
Run the following commands to pull the required models:
```bash
ollama pull llama3.2:3b-instruct-fp16
ollama pull meta-llama/Llama-Guard-3-8B
```

## Step 4: Start Ollama
Start the Ollama service:
```bash
ollama serve
```
Note: Run this in a separate terminal, as it needs to keep running.

## Step 5: Set Up `llama-stack-server` Project
1. Create and navigate to the project directory:
   ```bash
   mkdir llama-stack-server
   cd llama-stack-server
   ```
2. Create a virtual environment:
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Build the LLaMA stack with the Ollama template:
   ```bash
   INFERENCE_MODEL="llama3.2:3b-instruct-fp16" llama stack build --template ollama --image-type venv
   ```
4. Run the LLaMA stack server:
   ```bash
   llama stack run .venv/lib/python3.11/site-packages/llama_stack/templates/ollama/run-with-safety.yaml --image-type venv
   ```
   Note: Keep this running in a terminal.

## Step 6: Set Up `llama-stack-workshop` Project
1. Create and navigate to the project directory:
   ```bash
   mkdir llama-stack-workshop
   cd llama-stack-workshop
   ```
2. Create a virtual environment:
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Create a `requirements.txt` file:
   ```bash
   echo -e "llama-stack-client\nstreamlit\ndotenv\nrequests\ntavily" > requirements.txt
   ```
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Create a `.env` file:
   ```bash
   echo -e "LLAMA_STACK_SERVER=http://localhost:8321\nINFERENCE_MODEL_ID=llama3.2:3b-instruct-fp16\nSHIELD_ID=meta-llama/Llama-Guard-3-8B\nEMBEDDING_MODEL_ID=all-MiniLM-L6-v2\nTAVILY_SEARCH_API_KEY=<Add Key>" > .env
   ```
6. Replace `<Add Key>` in the `.env` file with your Tavily API key.

## Step 7: Verify Setup
- Ensure the Ollama service is running (`ollama serve`).
- Ensure the `llama-stack-server` is running (from Step 5.4).
- The `llama-stack-workshop` project is now ready for development with the specified dependencies and configuration.

## Notes
- Keep the Ollama service and `llama-stack-server` running in separate terminals.
- Obtain a Tavily API key from [Tavily](https://tavily.com) and update the `.env` file.
- Ensure Python 3.11 is used for all virtual environments to avoid compatibility issues.
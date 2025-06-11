#!/bin/bash

set -e

echo "🧪 Checking for Python 3.11..."

install_python() {
    if command -v python3.11 &>/dev/null; then
        echo "✅ Python 3.11 found: $(python3.11 --version)"
    else
        echo "🔧 Installing Python 3.11..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            if ! command -v brew &>/dev/null; then
                echo "📦 Installing Homebrew..."
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            fi
            brew install python@3.11
        elif [ -f /etc/debian_version ]; then
            sudo apt update
            sudo apt install -y software-properties-common
            sudo add-apt-repository -y ppa:deadsnakes/ppa
            sudo apt update
            sudo apt install -y python3.11 python3.11-venv python3.11-distutils
        elif [ -f /etc/redhat-release ] || [ -f /etc/centos-release ]; then
            sudo dnf install -y python3.11 python3.11-venv python3.11-distutils --skip-unavailable || sudo yum install -y python3.11 python3.11-venv python3.11-distutils --skip-unavailable
        else
            echo "❌ Unsupported OS for Python installation."
            exit 1
        fi
    fi
}

ensure_python_venv_installed() {
    echo "🔍 Checking if Python 3.11 with venv support is available..."

    # Locate python3.11
    if ! command -v python3.11 >/dev/null 2>&1; then
        echo "❌ Python 3.11 not found. Please install it first."
        return 1
    fi

    # Check if venv module works
    if python3.11 -m venv --help >/dev/null 2>&1; then
        echo "✅ venv module is available in Python 3.11."
        return 0
    fi

    echo "⚠️ venv module missing. Attempting to install..."

    # Install venv depending on OS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        if ! command -v brew >/dev/null 2>&1; then
            echo "❌ Homebrew not found. Please install Homebrew: https://brew.sh/"
            return 1
        fi
        brew reinstall python@3.11
        echo "✅ Reinstalled Python 3.11 with venv support."

    elif [ -f /etc/os-release ]; then
        source /etc/os-release
        case "$ID" in
            ubuntu|debian)
                sudo apt update
                sudo apt install -y python3.11-venv
                ;;
            fedora)
                sudo dnf install -y python3.11-venv
                ;;
            rhel)
                sudo yum install -y python3.11-venv
                ;;
            *)
                echo "❌ Unsupported Linux distribution: $ID"
                return 1
                ;;
        esac
        echo "✅ Installed python3.11-venv module."
    else
        echo "❌ Unsupported operating system: $OSTYPE"
        return 1
    fi

    # Final check
    if python3.11 -m venv --help >/dev/null 2>&1; then
        echo "✅ venv is now available."
    else
        echo "❌ Failed to install venv."
        return 1
    fi
}
install_ollama() {
    echo "🧪 Checking for Ollama..."
    if command -v ollama &>/dev/null; then
        echo "✅ Ollama found: $(ollama --version)"
    else
        echo "🔧 Installing Ollama..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            brew install ollama
        elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
            curl -fsSL https://ollama.com/install.sh | sh
        else
            echo "❌ Ollama installation not supported on this OS."
            exit 1
        fi
    fi
}

check_ollama_version(){
    if command -v ollama &>/dev/null; then
        echo "✅ Ollama version: $(ollama --version)"
    else
        echo "❌  Ollama is not installed"
        return 1
    fi
}
start_ollama() {
    # Check if server is responding
    if curl -s http://localhost:11434 | grep -q "Ollama"; then
        echo "✅ Ollama server already running."
        return 0
    fi

    echo "🚀 Starting Ollama server in background..."
    nohup ollama serve > ollama_serve.log 2>&1 &
    OLLO_PID=$!

    echo "⏳ Waiting for Ollama server to be ready..."
    for i in {1..30}; do
        if curl -s http://localhost:11434/v1/models >/dev/null; then
            echo "✅ Ollama server is up!"
            return 0
        fi
        sleep 1
    done

    echo "❌ Timeout: Ollama server did not start in time."
    kill "$OLLO_PID" 2>/dev/null
    return 1
}

pull_model() {
    local model="$1"

    echo "📥 Checking if model '$model' is pulled..."
    if ollama list | grep -q "$model"; then
        echo "✅ Model '$model' is already available."
    else
        echo "⬇️ Pulling model: $model ..."
        ollama pull "$model"
    fi
}

setup_venv_and_run_llama_stack() {
    # Create and enter directory
    mkdir -p llama-stack-server
    cd llama-stack-server

    # Create venv
    python3.11 -m venv .venv
    echo "✅ Virtual environment '.venv' created."

    # Activate venv
    # shellcheck source=/dev/null
    source .venv/bin/activate

    # Upgrade pip
    pip install --upgrade pip

    # Install llama-stack if missing
#    if ! command -v llama &>/dev/null; then
#        echo "Installing llama-stack package..."
#        pip install llama-stack==0.2.8
#    fi
    pip install llama-stack==0.2.8

}

setup_env_and_clone_workshop_repo() {
    # Clone outside current directory
#    CLONE_DIR="../llama-stack-workshop"
#    if [ -d "$CLONE_DIR" ]; then
#        echo "Directory '$CLONE_DIR' already exists. Skipping clone."
#    else
#        echo "Cloning llama-stack-workshop repo into '$CLONE_DIR'..."
#        git clone https://github.com/devninja-in/llama-stack-workshop "$CLONE_DIR"
#    fi
#
#    cd "$CLONE_DIR" || { echo "Failed to cd into $CLONE_DIR"; exit 1; }

    # Create venv
    python3.11 -m venv .venv
    echo "✅ Virtual environment '.venv' created in $CLONE_DIR."

    # Activate venv
    # shellcheck source=/dev/null
    source .venv/bin/activate

    # Upgrade pip and install requirements
    pip install --upgrade pip

    if [ -f requirements.txt ]; then
        echo "Installing dependencies from requirements.txt..."
        pip install -r requirements.txt
        pip install -e .
        echo "✅ Installed requirements."
    else
        echo "⚠️ requirements.txt not found!"
    fi

    # Prompt user for TAVILY_SEARCH_API_KEY
    read -rp "Please enter your TAVILY_SEARCH_API_KEY: " TAVILY_KEY

    cat << EOF > .env
LLAMA_STACK_SERVER=http://localhost:8321
INFERENCE_MODEL_ID=llama3.2:3b-instruct-fp16
SHIELD_ID=llama-guard3:8b
EMBEDDING_MODEL_ID=all-MiniLM-L6-v2
TAVILY_SEARCH_API_KEY=$TAVILY_KEY
EOF

    echo "✅ Created .env file with your TAVILY_SEARCH_API_KEY."
}
stop_ollama_server(){
  if [[ -n "$OLLO_PID" ]] && ps -p "$OLLO_PID" > /dev/null 2>&1; then
    echo "Stopping Ollama server"
    kill "$OLLO_PID"
    wait "$OLLO_PID" 2>/dev/null
    echo "Ollama server Stopped"
  else
    echo "Ollama server not running or PID missing"
  fi
}
go_one_dir_up(){
  cd ..
}
prompt_to_skip_pull_model(){
  while true; do
    read -p "Would you like to skip pulling the models and later provide Ollama server url directly(y/n) :" skip_model_pull
    if [[ "$skip_model_pull" == "n" ]]; then
      echo "Proceeding to pulling the models"
      start_ollama
      pull_model "llama3.2:3b-instruct-fp16"
      break
    elif [[ "$skip_model_pull" == "y" ]]; then
      echo "Please export the correct OLLAMA_URL before starting llama stack server"
      break
    else
      echo "Invalid input. Please enter y/n only"
    fi
  done
}

# Execute all steps
install_python
ensure_python_venv_installed
install_ollama
check_ollama_version
prompt_to_skip_pull_model
#start_ollama
#pull_model "llama3.2:3b-instruct-fp16"
#pull_model "llama-guard3:8b"
setup_env_and_clone_workshop_repo
go_one_dir_up
setup_venv_and_run_llama_stack
stop_ollama_server


echo "🎉 You are ready for the Llama stack workshop !"

# 🤖 Self-Operating Computer (AIOS)

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Status: Active Development](https://img.shields.io/badge/Status-Active%20Development-brightgreen.svg)]()

## Overview

**Self-Operating Computer (AIOS)** is an AI-powered operating system that integrates a powerful Large Language Model (LLM) agent at its core, fundamentally revolutionizing how humans interact with computers. This project ushers in a new era of intelligent computing where the OS truly understands and adapts to user needs.

### Key Features

- 🎯 **LLM-Powered Autonomy**: Leverages state-of-the-art LLMs (GPT-4, Claude, Gemini, Ollama) for intelligent decision-making
- 🖼️ **Vision Capabilities**: Advanced OCR and visual understanding through EasyOCR and YOLOv8
- 🎮 **Screen Control**: Automated desktop interaction via PyAutoGUI and mouse/keyboard control
- 🔄 **Multi-Model Support**: Seamless integration with multiple LLM backends
- 📊 **Screenshot Analysis**: Real-time screen capture and analysis for task execution
- ⚙️ **Configurable**: Extensive configuration options for different use cases
- 🧪 **Evaluation Framework**: Built-in testing and validation pipeline

---

## 📁 Project Structure

```
The-Self-Operating-Computer-A-Computer-LLM-Based-OS/
├── README.md                           # Project documentation
├── LICENSE                             # Apache 2.0 License
├── .env.example                        # Environment configuration template
├── requirements.txt                    # Root dependencies
│
└── Self Operating Computer/            # Main package directory
    ├── setup.py                        # Package installation configuration
    ├── requirements.txt                # Package dependencies
    ├── evaluate.py                     # Testing and evaluation module
    │
    └── operate/                        # Core package
        ├── __init__.py                 # Package initialization
        ├── main.py                     # Entry point
        ├── operate.py                  # Main operation logic
        ├── config.py                   # Configuration management
        ├── exceptions.py               # Custom exceptions
        │
        ├── models/                     # Model weights and configurations
        │   └── weights/
        │       └── best.pt             # YOLOv8 model weights
        │
        ├── utils/                      # Utility functions
        │   ├── __init__.py
        │   ├── vision.py              # OCR and vision processing
        │   ├── interaction.py         # Desktop automation
        │   ├── llm_interface.py       # LLM integrations
        │   └── screenshot.py          # Screenshot capture
        │
        └── tests/                      # Unit tests (recommended structure)
            ├── __init__.py
            └── test_operate.py         # Core tests
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip/conda package manager
- OpenAI API key or alternative LLM provider
- Display/screen support (Windows, macOS, Linux)

### Installation

#### Option 1: Direct Installation

```bash
# Clone the repository
git clone https://github.com/ImSuvodeep/The-Self-Operating-Computer-A-Computer-LLM-Based-OS.git
cd The-Self-Operating-Computer-A-Computer-LLM-Based-OS

# Install dependencies
pip install -r requirements.txt
cd "Self Operating Computer"
pip install -e .
```

#### Option 2: Using setup.py

```bash
cd "Self Operating Computer"
pip install .
```

### Configuration

1. **Create environment file**:
   ```bash
   cp .env.example .env
   ```

2. **Configure your LLM provider** in `.env`:
   ```env
   # OpenAI Configuration
   OPENAI_API_KEY=your_openai_api_key_here
   
   # Alternative: Google Generative AI
   GOOGLE_API_KEY=your_google_api_key_here
   
   # Alternative: Anthropic
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   
   # Alternative: Local Ollama
   OLLAMA_MODEL=mistral
   ```

### Usage

#### Basic Usage

```bash
# Run with default GPT-4 with OCR
operate --prompt "Go to GitHub and open the trending repositories"

# Or using the Python module
python -m operate.main --prompt "Your task here"
```

#### Advanced Usage

```bash
# Specify a different model
operate -m gpt-4-vision --prompt "Take a screenshot and tell me what's on screen"

# Use alternative models
operate -m claude-3 --prompt "Your task"
operate -m gemini-pro --prompt "Your task"
operate -m ollama-local --prompt "Your task"

# Run with custom configuration
operate --config custom_config.yaml --prompt "Your task"
```

#### Evaluation/Testing

```bash
# Evaluate model performance
python evaluate.py --model gpt-4-with-ocr

# Test specific model
python evaluate.py -m claude-3
```

---

## 📚 Core Components

### 1. **Main Module** (`operate.py`)
- Orchestrates the LLM agent with desktop control
- Manages screenshot capture and analysis
- Handles task planning and execution
- Implements reasoning loops and refinement

### 2. **Configuration** (`config.py`)
- Centralized settings management
- Model-specific parameters
- API endpoint configuration
- Performance tuning options

### 3. **Vision Processing** (utils)
- OCR capabilities via EasyOCR
- Object detection via YOLOv8
- Screen understanding and analysis
- Text extraction from UI elements

### 4. **Desktop Automation** (utils)
- Mouse and keyboard control
- Window management
- Screenshot capture and processing
- System interaction APIs

### 5. **LLM Interfaces** (utils)
- OpenAI GPT-4/GPT-4V integration
- Google Generative AI support
- Anthropic Claude integration
- Local Ollama support
- Extensible interface for custom models

---

## 🔧 Configuration Guide

### Model Selection

Edit `operate/config.py` to configure your preferred LLM:

```python
# Available models
AVAILABLE_MODELS = {
    "gpt-4-with-ocr": GPT4VisionModel,
    "gpt-4-turbo": GPT4TurboModel,
    "claude-3": ClaudeModel,
    "gemini-pro": GeminiModel,
    "ollama-local": OllamaModel,
}
```

### Performance Tuning

```python
# In config.py
CONFIG = {
    "screenshot_interval": 1.0,      # Seconds between screenshots
    "ocr_confidence_threshold": 0.5, # OCR confidence level
    "vision_model": "yolov8",        # Vision model to use
    "max_iterations": 10,            # Maximum reasoning iterations
    "api_timeout": 30,               # API call timeout
}
```

---

## 📦 Dependencies

### Core Dependencies
- **OpenAI**: `openai>=1.2.3` - GPT-4V integration
- **Anthropic**: `anthropic` - Claude models
- **Google**: `google-generativeai>=0.3.0` - Gemini integration
- **Ollama**: `ollama>=0.1.6` - Local LLM support

### Vision & Automation
- **EasyOCR**: `easyocr==1.7.1` - Optical Character Recognition
- **YOLOv8**: `ultralytics==8.0.227` - Object detection
- **PyAutoGUI**: `PyAutoGUI==0.9.54` - Desktop automation
- **Pillow**: `Pillow==10.1.0` - Image processing

### Utilities
- **python-dotenv**: `python-dotenv==1.0.0` - Environment management
- **pydantic**: `pydantic>=2.4.2` - Data validation
- **aiohttp**: `aiohttp==3.9.1` - Async HTTP client

See `Self Operating Computer/requirements.txt` for the complete list.

---

## 🧪 Testing & Evaluation

Run the evaluation suite to benchmark model performance:

```bash
# Default evaluation (GPT-4 with OCR)
python evaluate.py

# Test specific model
python evaluate.py --model claude-3

# Full evaluation pipeline
python -m pytest tests/ -v
```

**Test Cases Include**:
- Navigation tasks (e.g., "Go to GitHub.com")
- Media interaction (e.g., "Play a YouTube video")
- Custom objectives with screenshot validation

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
cd "Self Operating Computer"
pip install -e ".[dev]"

# Run tests
pytest tests/
```

---

## 📋 Roadmap

- [ ] Multi-window and multi-display support
- [ ] Improved reasoning and planning algorithms
- [ ] Enhanced error recovery mechanisms
- [ ] Support for more LLM providers
- [ ] Web interface for task management
- [ ] Mobile device integration
- [ ] Collaborative multi-agent scenarios
- [ ] Comprehensive logging and monitoring

---

## ⚠️ Important Notes

### Security & Privacy

- **Never commit API keys** - Use `.env` files and `.gitignore`
- **Screenshot data** is processed locally; verify your LLM provider's privacy policy
- **Automated execution** - Review and test objectives before running
- **API costs** - Monitor your LLM provider usage and costs

### System Requirements

- Minimum 4GB RAM (8GB recommended)
- Modern processor with multi-core support
- Display server access (X11 for Linux, native for Windows/macOS)
- Stable internet connection for API calls

### Limitations

- Currently supports single-monitor setups
- Some UI elements may not be OCR-readable
- API rate limits depend on provider
- OCR accuracy varies with screen resolution and font

---

## 🐛 Troubleshooting

### Common Issues

**Q: "OPENAI_API_KEY not found"**
```bash
# Solution: Create and populate .env file
echo "OPENAI_API_KEY=your_key_here" > .env
```

**Q: Screenshot capture fails**
```bash
# Solution: Ensure display server is running
# Linux: export DISPLAY=:0
# macOS/Windows: Should work natively
```

**Q: OCR accuracy is poor**
```bash
# Solution: Increase screenshot resolution or use better display scaling
# Check config.py for OCR settings
```

### Getting Help

- 📖 Check existing [Issues](https://github.com/ImSuvodeep/The-Self-Operating-Computer-A-Computer-LLM-Based-OS/issues)
- 💬 Create a new [Issue](https://github.com/ImSuvodeep/The-Self-Operating-Computer-A-Computer-LLM-Based-OS/issues/new) with details
- 📝 Review [Documentation](docs/) for advanced usage

---

## 📄 License

This project is licensed under the **Apache License 2.0** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [OpenAI GPT-4V](https://openai.com/)
- Vision capabilities powered by [EasyOCR](https://github.com/JaidedAI/EasyOCR) and [YOLOv8](https://github.com/ultralytics/ultralytics)
- Desktop automation using [PyAutoGUI](https://github.com/asweigart/pyautogui)
- Community contributions and feedback

---

## 📞 Contact & Support

- **Author**: [@ImSuvodeep](https://github.com/ImSuvodeep)
- **Repository**: [GitHub](https://github.com/ImSuvodeep/The-Self-Operating-Computer-A-Computer-LLM-Based-OS)
- **Issues**: [Report a bug](https://github.com/ImSuvodeep/The-Self-Operating-Computer-A-Computer-LLM-Based-OS/issues)
- **Discussions**: [Join discussions](https://github.com/ImSuvodeep/The-Self-Operating-Computer-A-Computer-LLM-Based-OS/discussions)

---

## 🚀 Quick Reference

| Command | Description |
|---------|-------------|
| `operate --prompt "task"` | Run with default model |
| `operate -m gpt-4-vision --prompt "task"` | Specify model |
| `evaluate.py` | Run test suite |
| `pip install -e .` | Install in development mode |
| `python -m pytest tests/` | Run unit tests |

---

**Last Updated**: 2025-09-15 | **Status**: Active Development | **Python**: 3.9+

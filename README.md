# ReqSpector

ReqSpector is a powerful CLI tool designed to analyze system requirements and provide priliminary assessments.

## Features

- Take system requirements directly from user input
- Provide a feedback (low, medium, high) for the following categories:
  - Completeness
  - Clarity
  - Testability
  - Ambiguity Check
  - Feasibility
  - Dependencies mentioned
- Take file inputs from txt, md and pdf formats
- Offline Fallback -> Ollama local LLM support
- API integration
- Multiline requirement input support
- Tabular output format

## Installation

Clone this repository and install the required dependencies:

```bash
git clone ---
pip install -r requirements.txt
```

## Usage
Run the tool using the command line:

```bash
python reqspector.py
```



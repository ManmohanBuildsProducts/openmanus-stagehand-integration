# OpenManus + Stagehand Integration

A powerful integration that combines OpenManus automation with Stagehand for streamlined LinkedIn connection requests.

## Overview

This project automates LinkedIn connection requests by integrating OpenManus with Stagehand. It allows you to:
- Send personalized connection requests at scale
- Track request status and acceptance rates
- Customize message templates
- Schedule automation runs

# 🤖 OpenManus + Stagehand Integration

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Experimental](https://img.shields.io/badge/Status-Experimental-orange.svg)]()
[![Made with: Cursor](https://img.shields.io/badge/Made%20with-Cursor-blue.svg)](https://cursor.sh/)

Integration between [OpenManus](https://github.com/mannaandpoem/OpenManus) (open-source version of Manus) and [Stagehand](https://docs.stagehand.dev/get_started/introduction) for browser automation tasks. This project demonstrates how to connect these powerful tools to create AI-powered browser automation workflows.

![System Diagram](docs/images/architecture.png)

## ⚠️ AI-Generated Code Disclaimer

> **IMPORTANT**: This project was created by a product manager with no prior coding experience, using [Cursor](https://cursor.sh/) and its AI capabilities. The code, documentation, and architecture were generated with assistance from large language models.
>
> While efforts have been made to follow best practices, this code should be reviewed by experienced developers before use in any production environment. There may be errors, inefficiencies, or security issues that need addressing.
>
> This was built as a rapid solution to handle 1600+ LinkedIn connection requests and is shared as a practical example rather than production-ready software.

## 📋 Table of Contents

- [Background](#background)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [LinkedIn Connection Automation](#linkedin-connection-automation)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## 🌟 Background

After posting about an internship opening, I received over 1600 LinkedIn connection requests that would have been tedious to process manually. As a product manager interested in AI and automation, I decided to build a solution using OpenManus (an open-source version of Manus) and Stagehand (a browser automation tool).

This integration demonstrates how non-technical professionals can leverage AI tools to create practical automation solutions without extensive coding knowledge.

## 🏗️ Architecture

This integration connects OpenManus (AI agent framework) with Stagehand (browser automation) to create a powerful workflow:

1. OpenManus provides the AI agent capabilities and task management
2. Stagehand controls the browser to interact with LinkedIn
3. The integration scripts coordinate between these tools


┌─────────────┐ ┌──────────────┐ ┌──────────────┐
│ OpenManus │────▶│ Integration │────▶│ Stagehand │
│ AI Agent │ │ Layer │ │ Browser │
└─────────────┘ └──────────────┘ └──────────────┘
│
▼
┌──────────────┐
│ LinkedIn │
│ Automation │
└──────────────┘



## 📋 Prerequisites

- Python 3.9+ 
- Node.js 16+
- [OpenManus](https://github.com/mannaandpoem/OpenManus) installed
- [Stagehand](https://docs.stagehand.dev/get_started/introduction) installed
- LinkedIn account
- Chrome or Chromium browser

## 🔧 Installation

1. Clone this repository:

```bash
git clone https://github.com/ManmohanBuildsProducts/openmanus-stagehand-integration.git
cd openmanus-stagehand-integration
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Set up configuration files:

```bash
cp .env.example .env
cp config/config.example.toml config/config.toml
```

4. Edit the configuration files with your credentials and preferences.

## ⚙️ Configuration

### OpenManus Configuration

Configure OpenManus by editing `config/config.toml`:

```toml
# OpenManus API configuration
[llm]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "YOUR_API_KEY"  # Replace with your actual API key
```

### LinkedIn Credentials

Create a `.env` file with your LinkedIn credentials:

LINKEDIN_EMAIL=your_email@example.com
LINKEDIN_PASSWORD=your_password



**IMPORTANT:** Never commit this file to version control.

## 🚀 Usage

The basic usage flow:

1. Start the OpenManus server (see [OpenManus documentation](https://github.com/mannaandpoem/OpenManus))
2. Run the integration script:

```bash
python scripts/run_linkedin_automation.py
```

3. The script will:
   - Connect OpenManus with Stagehand
   - Launch a browser instance
   - Log into LinkedIn
   - Process connection requests based on your configuration

## 🔗 LinkedIn Connection Automation

This project was built to solve a specific use case: processing 1600+ LinkedIn connection requests after posting about an internship opening.

### Features:

- **Automated login:** Securely logs into LinkedIn
- **Connection request processing:** Accepts or rejects based on configurable criteria
- **Selective messaging:** Optionally sends a welcome message to accepted connections
- **Rate limiting:** Built-in delays to avoid triggering LinkedIn's anti-automation systems
- **Progress tracking:** Logs activity and maintains state between sessions

### Example:

```python
# Configure the automation parameters
automation_config = {
    "max_connections": 100,  # Process up to 100 connections per session
    "delay_between_actions": 3,  # Wait 3 seconds between actions
    "auto_accept_all": True,  # Accept all connection requests
    "send_welcome_message": False  # Don't send welcome messages
}

# Run the automation
run_linkedin_automation(automation_config)
```

## 🛠️ Customization

### Filtering Connection Requests

You can customize the acceptance criteria by modifying the `should_accept_connection` function in `scripts/linkedin_automation.py`:

```python
def should_accept_connection(profile_data):
    """
    Custom logic to determine if a connection request should be accepted.
    
    Args:
        profile_data (dict): Data extracted from the LinkedIn profile
        
    Returns:
        bool: True if the connection should be accepted, False otherwise
    """
    # Example: Accept if they have "Product Manager" in their title
    if "product manager" in profile_data.get("title", "").lower():
        return True
        
    # Example: Accept if they're from a specific company
    if "desired company" in profile_data.get("company", "").lower():
        return True
        
    # Default behavior
    return automation_config.get("auto_accept_all", False)
```

## 🔍 Troubleshooting

### Common Issues

#### LinkedIn Security Verification

If you encounter security verification during automation:

1. The script will pause and notify you
2. Complete the verification manually on your device
3. The automation will continue once verification is complete

#### Rate Limiting

If LinkedIn detects unusual activity:

1. Increase the delay between actions in your configuration
2. Run the automation for shorter sessions
3. Consider adding randomized delays

## 👥 Contributing

Contributions are welcome! As this project was AI-generated, it particularly benefits from:

1. Code reviews and improvements
2. Security enhancements
3. Additional features and use cases
4. Documentation improvements

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenManus](https://github.com/mannaandpoem/OpenManus) team for creating an accessible AI agent framework
- [Stagehand](https://docs.stagehand.dev) team for their browser automation tools
- [Cursor](https://cursor.sh/) for enabling non-technical professionals to create code with AI assistance

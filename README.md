# OpenManus + Stagehand Integration

A powerful integration that combines OpenManus automation with Stagehand for streamlined LinkedIn connection requests.

## Overview

This project automates LinkedIn connection requests by integrating OpenManus with Stagehand. It allows you to:
- Send personalized connection requests at scale
- Track request status and acceptance rates
- Customize message templates
- Schedule automation runs

## Getting Started

### Prerequisites

- Python 3.8 or higher
- A LinkedIn account
- Stagehand API access

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/openmanus-stagehand-integration.git
   cd openmanus-stagehand-integration
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Copy the example environment file and fill in your details:
   ```
   cp .env.example .env
   ```

## Configuration

Edit the `.env` file with your credentials:

```
LINKEDIN_USERNAME=your_email@example.com
LINKEDIN_PASSWORD=your_password
STAGEHAND_API_KEY=your_api_key
```

Additional configuration options can be found in the `config` directory.

## Usage

Run the main script to start the automation:

```
python scripts/linkedin_automation.py
```

Check the `examples` folder for more specific use cases.

## Documentation

For detailed documentation, see the `docs` directory.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on contributing to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
#!/usr/bin/env python3
"""
LinkedIn Connection Requests Example

This example demonstrates how to use the OpenManus-Stagehand integration
to send LinkedIn connection requests to a list of prospects.

Created with AI assistance through Cursor.
"""

import asyncio
import json
import os
import sys
import logging
from pathlib import Path

# Add the project root to the path so we can import from scripts
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.linkedin_automation import run_automation

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("example")

async def main():
    """Run the example script"""
    # Example prospect data - in a real scenario, you might import from CSV or database
    prospects = [
        {
            "first_name": "Sample",
            "last_name": "User",
            "name": "Sample User",
            "profile_url": "https://www.linkedin.com/in/sampleuser",
            "company": "Example Company",
            "title": "Product Manager",
            "industry": "Technology",
            "interest": "AI",
            "connection_degree": 2,
            "mutual_connections": 3
        },
        {
            "first_name": "Test",
            "last_name": "Person",
            "name": "Test Person",
            "profile_url": "https://www.linkedin.com/in/testperson",
            "company": "Demo Inc.",
            "title": "Marketing Director",
            "industry": "Marketing",
            "interest": "Growth",
            "connection_degree": 2,
            "mutual_connections": 1
        }
    ]
    
    # Create a temporary prospects file
    temp_prospects_file = "examples/temp_prospects.json"
    with open(temp_prospects_file, "w") as f:
        json.dump(prospects, f, indent=2)
    
    # Create a sample configuration
    config = {
        "linkedin": {
            "login_url": "https://www.linkedin.com/login",
            "connection_limit": 2,  # Limiting to just 2 for the example
            "delay_between_requests": [5, 10],  # Shorter delays for testing
            "headless": False,
            "retry_attempts": 1
        },
        "prospects_path": temp_prospects_file,
        "message_templates": [
            "Hi {{first_name}}, I noticed your work at {{company}} and would love to connect! This is an example message."
        ],
        "stagehand": {
            "browserless_token": os.environ.get("STAGEHAND_BROWSERLESS_TOKEN", ""),
            "timeout_ms": 30000,
            "viewport": {
                "width": 1280,
                "height": 800
            }
        },
        "openmanus": {
            "api_key": os.environ.get("OPENMANUS_API_KEY", ""),
            "base_url": os.environ.get("OPENMANUS_BASE_URL", "https://api.openmanus.ai"),
            "model": "gpt-4o"
        }
    }
    
    # Save the configuration to a temporary file
    temp_config_file = "examples/temp_config.json"
    with open(temp_config_file, "w") as f:
        json.dump(config, f, indent=2)
    
    try:
        logger.info("Starting LinkedIn connection request example")
        
        # In a real implementation, you would run the automation here
        # Since this is just an example, we'll add a simulation step
        
        logger.info("This example would normally call the automation code")
        logger.info("For a real run, uncomment the next line:")
        # results = await run_automation(temp_config_file)
        
        # Instead, we'll just simulate the results
        logger.info("Simulating automation results...")
        results = {
            "total": 2,
            "successful": 2,
            "failed": 0,
            "skipped": 0,
            "start_time": "2023-06-01T12:00:00",
            "end_time": "2023-06-01T12:01:30"
        }
        
        logger.info(f"Example complete! Result: {json.dumps(results, indent=2)}")
        logger.info(f"Successful connections: {results['successful']}/{results['total']}")
        
    finally:
        # Clean up temporary files
        for temp_file in [temp_config_file, temp_prospects_file]:
            if os.path.exists(temp_file):
                os.remove(temp_file)
                logger.info(f"Cleaned up temporary file: {temp_file}")

if __name__ == "__main__":
    asyncio.run(main()) 
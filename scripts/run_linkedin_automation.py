#!/usr/bin/env python3
"""
Run LinkedIn Automation

This script initializes and runs the LinkedIn automation process,
connecting OpenManus with Stagehand and handling the high-level workflow.

Created with AI assistance through Cursor.
"""

import asyncio
import os
import logging
import json
import argparse
from dotenv import load_dotenv

# Import the linkedin_automation module
from linkedin_automation import run_automation

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/linkedin_runner.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("linkedin_runner")

# Load environment variables
load_dotenv()

async def main():
    """Main function to parse arguments and run the automation"""
    parser = argparse.ArgumentParser(description="Run LinkedIn automation")
    parser.add_argument("--config", 
                        type=str, 
                        default="config/linkedin_config.json",
                        help="Path to the configuration file")
    parser.add_argument("--output", 
                        type=str, 
                        default="data/results.json",
                        help="Path to save the results")
    
    args = parser.parse_args()
    
    # Ensure the logs directory exists
    os.makedirs("logs", exist_ok=True)
    
    # Ensure the data directory exists for the results
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    
    logger.info(f"Running LinkedIn automation with config: {args.config}")
    
    try:
        # Run the automation
        results = await run_automation(args.config)
        
        # Save results
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
            
        logger.info(f"Results saved to {args.output}")
        logger.info(f"Automation complete! Sent {results.get('successful', 0)} connection requests")
        
    except Exception as e:
        logger.error(f"Error running automation: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(main())

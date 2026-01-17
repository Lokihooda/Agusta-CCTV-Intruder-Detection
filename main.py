#!/usr/bin/env python3
"""
Agusta CCTV Intruder Detection System
Main application entry point
"""

import os
import sys
import yaml
import logging
import argparse
from pathlib import Path

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from camera_handler import CameraHandler
from detector import FaceDetector
from recognizer import FaceRecognizer
from alarm_system import AlarmSystem
from database import VisitorDatabase


def load_config(config_path='config.yaml'):
    """Load configuration from YAML file"""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def setup_logging(config):
    """Setup logging configuration"""
    log_config = config.get('logging', {})
    log_file = log_config.get('log_file', 'logs/agusta.log')
    log_level = log_config.get('log_level', 'INFO')
    
    # Create logs directory if it doesn't exist
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    
    logging.basicConfig(
        level=getattr(logging, log_level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger('Agusta')


def create_directories(config):
    """Create necessary directories"""
    directories = [
        config['logging']['snapshot_path'],
        config['database']['path'].rsplit('/', 1)[0],
        'data/visitors',
        'logs',
        'models/face_detector',
        'models/face_recognizer'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)


def main():
    """Main application function"""
    parser = argparse.ArgumentParser(
        description='Agusta CCTV Intruder Detection System'
    )
    parser.add_argument(
        '--config',
        default='config.yaml',
        help='Path to configuration file'
    )
    parser.add_argument(
        '--camera',
        type=int,
        help='Camera index to use (overrides config)'
    )
    args = parser.parse_args()
    
    # Load configuration
    try:
        config = load_config(args.config)
    except FileNotFoundError:
        print(f"Error: Configuration file '{args.config}' not found!")
        print("Please create a config.yaml file or specify a valid config path.")
        sys.exit(1)
    
    # Setup logging
    logger = setup_logging(config)
    logger.info("Starting Agusta CCTV Intruder Detection System")
    
    # Create necessary directories
    create_directories(config)
    
    # Initialize components
    try:
        logger.info("Initializing components...")
        
        # Database
        db = VisitorDatabase(config['database']['path'])
        
        # Face detector and recognizer
        detector = FaceDetector(config)
        recognizer = FaceRecognizer(config, db)
        
        # Alarm system
        alarm = AlarmSystem(config)
        
        # Camera handler
        camera_handler = CameraHandler(config, detector, recognizer, alarm)
        
        logger.info("All components initialized successfully")
        
        # Start monitoring
        logger.info("Starting camera monitoring...")
        camera_handler.start()
        
    except KeyboardInterrupt:
        logger.info("Received shutdown signal")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)
    finally:
        logger.info("Shutting down Agusta system")
        if 'camera_handler' in locals():
            camera_handler.stop()


if __name__ == '__main__':
    main()

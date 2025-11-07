#!/usr/bin/env python3
"""
Simple script to run the Calculator Web Application
"""

import os
import sys
import subprocess

def main():
    """Main function to run the web application"""
    print("🧮 Calculator Web Application")
    print("=" * 40)
    
    # Check if Flask is installed
    try:
        import flask
        print("✅ Flask is installed")
    except ImportError:
        print("❌ Flask not found. Installing dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed")
    
    # Check if app.py exists
    if not os.path.exists("app.py"):
        print("❌ app.py not found!")
        return
    
    print("🚀 Starting Calculator Web Application...")
    print("📱 Open your browser and go to: http://localhost:8000")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 40)
    
    # Run the Flask application
    try:
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Calculator Web Application stopped!")
    except Exception as e:
        print(f"❌ Error running application: {e}")

if __name__ == "__main__":
    main()

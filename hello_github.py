"""
GitHub Learning Platform Sandbox
A simple sandbox script to output system environments and greet developers.
"""

import sys
import os

def main():
    print("=========================================")
    print("Welcome to your GitHub Introduction Repo!")
    print("=========================================")
    print(f"Python interpreter: {sys.version}")
    print(f"Current Directory: {os.getcwd()}")
    print("Status: Active and Ready for Experiments.")
    print("=========================================")

if __name__ == "__main__":
    main()

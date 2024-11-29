import argparse
import sys
from config import DB_DETAILS


def main(env):
    # env = sys.argv[1]
    db_details = DB_DETAILS[env]
    print(db_details)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the application.")
    
    # Add an argument with a default value
    parser.add_argument(
        "environment", 
        nargs="?", 
        default="dev",  # Default parameter
        help="Specify the environment (e.g., dev, prod, test). Default is 'dev'."
    )
    
    args = parser.parse_args()
    main(args.environment)
    # main()
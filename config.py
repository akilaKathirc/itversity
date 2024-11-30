from dotenv import load_dotenv
import os

# Loads variables from .env into os.environ
load_dotenv() 

DB_DETAILS = {
"dev":
{
    "SOURCE_DB":{
        "DB_TYPE": "mysql",
        "DB_HOST": "localhost",
        "DB_NAME": os.environ.get("SOURCE_DB"),
        "DB_USER": os.environ.get("SOURCE_DB_USER"),
        "DB_PASS": os.environ.get("SOURCE_DB_PASS")
    },
    "TARGET_DB":{
        "DB_TYPE": "postgres",
        "DB_HOST": "localhost",
        "DB_NAME": os.environ.get("TARGET_DB"),
        "DB_USER": os.environ.get("TARGET_DB_USER"),
        "DB_PASS": os.environ.get("TARGET_DB_PASS")
    }
}

}





import sys
import shutil
import boto3

env = str(sys.argv[1])

if env == "dev":
    shutil.copyfile("../envs/backend-local.env", "../backend/.env")
    shutil.copyfile("../envs/backend-local.env", "../.env")

elif env == "prod":
    shutil.copyfile("../envs/backend-prod.env", "../.env")
    ssm = boto3.client("ssm")
    f = open("../.env", "a")

    # POSTGRES_USER
    db_user = ssm.get_parameter(Name="/prod/database/user", WithDecryption=True)
    f.write("POSTGRES_USER=" + db_user["Parameter"]["Value"] + "\n")

    # POSTGRES_PASSWORD
    db_password = ssm.get_parameter(Name="/prod/database/password", WithDecryption=True)
    f.write("POSTGRES_PASSWORD=" + db_password["Parameter"]["Value"] + "\n")

    # POSTGRES_HOST
    db_endpoint = ssm.get_parameter(Name="/prod/database/endpoint", WithDecryption=True)
    db_host = db_endpoint["Parameter"]["Value"].split(":")[0]
    f.write("POSTGRES_HOST=" + db_host + "\n")

    # POSTGRES_PORT
    db_port = db_endpoint["Parameter"]["Value"].split(":")[1]
    f.write("POSTGRES_PORT=" + db_port + "\n")

    # POSTGRES_DB
    db_name = ssm.get_parameter(Name="/prod/database/db", WithDecryption=True)
    f.write("POSTGRES_DB=" + db_name["Parameter"]["Value"] + "\n")

    f.close()
    shutil.copyfile("../.env", "../backend/.env")

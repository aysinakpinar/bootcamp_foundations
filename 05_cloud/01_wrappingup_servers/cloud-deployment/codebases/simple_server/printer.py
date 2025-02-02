import os

print("I print out the secret password")
if "SECRET_PASSWORD" in os.environ:
    # `os.environ` is a dictionary of all the environment variables
    print(os.environ["SECRET_PASSWORD"])
else:
    print("But there is no SECRET_PASSWORD environment variable set")

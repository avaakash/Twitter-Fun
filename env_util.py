import json

def getEnv():
    environ_secrets = []
    f = open("env.json")
    env = json.load(f)
    f.close()
    
    environ_secrets.append(env.get("CONSUMER_KEY", ""))
    environ_secrets.append(env.get("CONSUMER_SECRET", ""))
    environ_secrets.append(env.get("ACCESS_TOKEN", ""))
    environ_secrets.append(env.get("ACCESS_SECRET", ""))

    return environ_secrets


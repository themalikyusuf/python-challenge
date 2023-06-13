import requests

def create_github_token(username, password):
    url = 'https://api.github.com/authorizations'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    data = {
        'scopes': ['repo'],
        'note': 'GitHub Token for Automation'
    }
    response = requests.post(url, auth=(username, password), headers=headers, json=data)
    if response.status_code == 201:
        token = response.json().get('token')
        print('GitHub Token created:', token)
        return token
    else:
        print('Failed to create GitHub Token:', response.json().get('message'))

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print('Usage: python create_token.py TIKODUDE_USERNAME TIKODUDE_PASSWORD')
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        create_github_token(username, password)

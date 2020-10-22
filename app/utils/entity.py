import requests

def update_entity(enity_id, url, token, data):
    response = requests.post(
        f'{url}/states/{enity_id}',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        },
        json={
            'state': 'new smessage',
            'attributes': data
        }
    )

    if response.status_code == 200:
        return response.json()
    
    return response.content
import requests

def update_entity(entity_id, url, token, data):
    response = requests.post(
        f'{url}/states/{entity_id}',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        },
        json={
            'state': 'received',
            'attributes': data
        }
    )

    if response.status_code == 200:
        return response.json()
    
    return response.content
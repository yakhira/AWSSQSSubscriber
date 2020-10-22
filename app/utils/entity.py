import requests
import logging

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
        logging.info(response.json())
        return True
    
    logging.error(response.content)
    return False
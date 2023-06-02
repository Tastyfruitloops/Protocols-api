import argparse
import json
import requests

with open('config.json', 'r') as f:
    j = json.load(f)
token, api_v = j.values()


def make_request(request):
    resp = requests.get(request).json()
    if 'error' in resp.keys():
        raise ValueError(resp['error']['error_msg'])
    return resp['response']


def get_user_by_screen(screen):
    id_by_screen_name_req = f"https://api.vk.com/method/users.get?user_ids={screen}" \
                            f"&access_token={token}&v={api_v}"
    try:
        resp = make_request(id_by_screen_name_req)
        if len(resp) == 0:
            raise ValueError(f"No user with screen name {screen}")
        return resp[0]
    except ValueError as e:
        print(e)
        exit(1)


def get_friends(link: str):
    screen_name = link[link.rfind('/') + 1:]
    user = get_user_by_screen(screen_name)

    friends_list_req = f"https://api.vk.com/method/friends.get?user_id={user['id']}" \
                       f"&order=hints&fields=nickname,domain&access_token={token}&v={api_v}"

    resp = make_request(friends_list_req)

    output = f"Кол-во друзей пользователя {user['first_name']} {user['last_name']}: {resp['count']}\n"
    friends = resp['items']
    for friend in friends:
        output += f'Имя: {friend["first_name"]}\nФамилия: {friend["last_name"]}\n\n'
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-link", required=True)
    cnsl_args = parser.parse_args().__dict__

    result = get_friends(cnsl_args["link"])
    print(result)

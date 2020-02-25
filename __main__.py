from slackclient import SlackClient
from jwtdecoder import jwt_module
from config import Config
import argparse


def get_field(jwt, value):
    field = jwt.jwt_decode(value)
    if '401' in field:
        print('401 Unauthorized')
        exit(1)
    else:
        return field


def check_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--jwt_token', help='JWT token needed.', required=True)
    args = parser.parse_args()
    return args


def send_slack_message(message, channel, author, icon):
    slack_client = SlackClient(Config().get_slack_token())
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=message,
        username=author,
        icon_emoji=icon
    )

    greeting = "Sending: {0} to channel {1}".format(message, channel)
    print(greeting)
    return {"Result": greeting}


def main(args):
    jwt_object = args.jwt_token
    public_key = Config().get_jwt_public_key()
    alg = Config().get_jwt_algorithm()
    jwt = jwt_module(public_key, alg, jwt_object)
    message = get_field(jwt, 'Message')
    channel = get_field(jwt, 'Channel')
    author = get_field(jwt, 'AuthorName')
    icon = get_field(jwt, 'Icon')
    send_slack_message(message, channel, author, icon)

#-----------main Code-------------
args = check_arguments()
main(args)
# slack_message_jwt_git
- This service will receive a jwt string  and will trigger slack message using slack app

### Prerequisites

- It supports RS256 , RS512 Algorithm
- You can create the encoded jwt using https://jwt.io/, use this payload as example:

{
 "Message": "Error on CED",
 "Channel": "GJXDW7PKJ",
 "AuthorName": "CED BOT",
 "Icon": ":error:"
}

- Create public key file (pem) file and add it into env variable (JWT_PK).
- You will need three env variables:
   - JWT_ALG=RS256
   - JWT_PK=pk.pem
   - SLACK_TOKEN=xoxb-xxxxxxxxxxxx-vxxpxxxxxxxxxx


### Prerequisites

- cryptography==2.7
- pem==19.2.0
- PyJWT==1.7.1
- slackclient==1.2.1


### Installing

Clone the repo using gitbash or git for linux:

https://gitforwindows.org/

Example:
git git@github.com:reabarca78/slack_message_jwt_git.git

### Pre steps

pip install -r requirements.txt


### Details of the files

- _main_.py                : main code.
- config.py                : read the env variables. 
- jwtdecoder.py            : jwt decoder functions.
- jwtnotation.txt          : Example of the payload.


### Run it , you can create a Openwhisk server less function and send it the parameter in a web action.

https://console.bluemix.net/docs/openwhisk/openwhisk_actions.html#creating-python-actions


- python --jwt_token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


## Authors

* **Roy Abarca** - *Initial work* - rabarca@asys.co.cr

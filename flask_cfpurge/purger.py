import requests, json

class Purger():
    
    def __init__(self, app, **args):
        self.app = app
        print(args)
        if args['cf_auth_key'] == None:
            self.auth_key = self.app.cf_auth_key
        else:
            self.auth_key = args['auth_key']
        if args['auth_email'] == None:
            self.auth_email = self.app.cf_auth_email
        else:
            self.auth_email = args['cf_auth_email']
    
    def purge_all(self, zone):
        headers = {
            'Content-Type': 'application/json',
            'X-Auth-Key': self.auth_key,
            'X-Auth-Email': self.auth_email
        }
        data = {
            'purge_everything': True
        }
        response = requests.post('https://api.cloudflare.com/client/v4/zones/{}/purge_cache'.format(zone), data=json.dumps(data), headers=headers)
        res_data = json.loads(response.content)
        if res_data['success'] == True:
            print('Purged All')
            return True
        else:
            return False
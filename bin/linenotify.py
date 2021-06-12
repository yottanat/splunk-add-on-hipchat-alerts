#!/usr/local/bin/python+
# -*- coding: utf-8 -*-
import requests
import sys,json

def notify(payload):
    # url = 'https://notify-api.line.me/api/notify'
    # token = 'seitgHNDlcJLoKYgv8FoWHNndJVtkslQ2WFYgmMcop4'
    setting = payload.get('configuration')
    send_message(setting)
    url = setting.get('base_url')
    token = setting.get('auth_token')
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
    # msg = 'Login Fail Alert'
    msg = setting.get('message')
    r = requests.post(url, headers=headers , data = {'message':msg})
    print(r.text)

def send_message(settings):
    print("DEBUG Sending message with settings %s" % settings, file=sys.stderr)
    with open('config_text.txt', 'w') as f:
        for element in settings:
            f.write(element + "\n")
        f.close()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--execute":
        payload = json.loads(sys.stdin.read())
        with open('payload_text.txt', 'w') as f:
            for element in payload:
                f.write(element + "\n")
            f.close()
        success = notify(payload)
        if not success:
            print >> sys.stderr, "FATAL Failed trying to send room notification"
            sys.exit(2)
        else:
            print >> sys.stderr, "INFO Room notification successfully sent"
    else:
        print >> sys.stderr, "FATAL Unsupported execution mode (expected --execute flag)"
        sys.exit(1)
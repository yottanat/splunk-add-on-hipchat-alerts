# Line alert settings

action.line = [0|1]
* Enable line notification

action.line.param.room = <string>
* Name of the room to send the notification to
* (required)

action.line.param.message = <string>
* The message to send to the line room. 
* (required)

action.line.param.message_format = [html|text]
* The format of the room notification (optional)
* Default is "html"
* (optional)

action.line.param.auth_token = <string>
* Override line API auth token from global alert_actions config
* (optional)

action.line.param.notification_type = [message|card]
* Specify whether to send the notification as a plain message or a card using the new lineConnect API. 



[linenotify]

param.base_url = <string>
* linenotify API base URL - adjust if you're using you own server on premise
* https://notify-api.line.me/api/notify

param.auth_token = <string>
* linenotify OAuth2 token 
* see "seitgHNDlcJLoKYgv8FoWHNndJVtkslQ2WFYgmMcop4"

param.notification_type = [message|card]
* Specify whether to send the notification as a plain message or a card using the new linenotify API. 

param.card_icon = <string>
* If notification_type is card, this URL will be supplied for the icon of the card. 

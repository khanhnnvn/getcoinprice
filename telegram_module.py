# import config
import requests
def telegram_send_to(chat_id, noi_dung,api):
	header={'Content-Type': 'application/json'}
	body="""{
			"chat_id":\""""+str(chat_id)+"""\",
			"text":\""""+noi_dung+"""\"
			}"""
	r=requests.post(api,data=body,headers=header,timeout=30)
	return r.content
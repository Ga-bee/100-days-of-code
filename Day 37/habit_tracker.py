import requests as rq
import datetime
import replace as re
TOKEN = '<token>'
USERNAME = '<username>'
GRAPHID = "graph1"
url = "https://pixe.la/v1/users"
user_params = {
    'token': TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor': 'yes'

}

###########################create user###################################
# response = rq.post(url=url, json=user_params)
# a = response.raise_for_status()

graph_endpoint = f"{url}/{USERNAME}/graphs"

graph_param = {
    "X-USER-TOKEN":"<>"
}

graph_config ={
    "id":GRAPHID,
    "name":"gabeegraph",
    "unit": "pages",
    "type":"int",
    "color":"shibafu"
}
hoje = datetime.datetime.now()
# hoje_f = hoje.replace('-','')
hoje_f = hoje.strftime("%Y%m%d")
# print(aa)
########################create graph #################################################
# response = rq.post(url=graph_endpoint,json=graph_config ,headers=graph_param)
# print(response.text)

# quantidade = int(input("Quanto vc quer adicionar hoje?"))
post_pixel_url = f"{graph_endpoint}/{GRAPHID}"

# graph_pixels = {
#     "date":f"{hoje_f}",
#     "quantity":f"{quantidade}"
# }

##########################Create Pixel###################################

# response = rq.post(url=post_pixel_url,headers=graph_param,json=graph_pixels)
# print(response.text)

#######################update pixel ##################################
update_url = f"{post_pixel_url}/20230531"
update_params = {
    'quantity': '1'
}
# response = rq.put(url=update_url,headers=graph_param,json=update_params)
# print(response.text)
###############################delete pixel################################
delete_url = f"{post_pixel_url}/20230531"

response = rq.delete(url=delete_url,headers=graph_param)
print(response.text)

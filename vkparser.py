import vk_api
import csv

valid_id = 402310205
task_id = 4405955

token = 'vk1.a.mpN2wZ6Imv9A3vNJ1gHaZM_M2cu0V5gIVjy9WenR4q9h9qwYetFxQ_HV45GILA_Ncmo6LrF1sZo7WMEBexoqQKG1T19ZQLxJjN1sYNwuwhE15-IpoUCM-iR5XUXoCONSFrRJVmIBiOcKWFlHz0-oxU5j7Nybhbo_3VKfgTFBoto53eoWfASaqjg6LCzP_UPzbpcAk-_Zn4no4BalDTA4nw'

session = vk_api.VkApi(token=token)
vk = session.get_api()

all_friends = set()

def get_user_friends(user_id):
    friends = session.method("friends.get", {'user_id': user_id})
    count = friends['count']
    
    for i in friends['items']:
        all_friends.add(i)
       
    for i in friends['items']:
        try:
            friends_of_friends = session.method('friends.get', {'user_id': i})
            for item in friends_of_friends['items']:
                all_friends.add(item)    
        except:
            continue    

def write_csv(data):
    with open('all_friends.csv', 'w', encoding='utf-8') as file:
        for i in data:
            file.writelines(str(i)+'\n')
                  

get_user_friends(valid_id)
write_csv(all_friends)
print('done')



    




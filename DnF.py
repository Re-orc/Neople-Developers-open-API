import requests
import json


servers,cname = str(input('서버와 케릭터 이름을입력해주세요 : ')).split()
if servers == '카인':
    servers = 'cain'

class Nexon_game():
    
    def __init__(self):
        self.sv = servers
        self.cn = cname
        self.key = {'apikey':'',}
        
    def chracter_info(self):
        url = requests.get('https://api.neople.co.kr/df/servers/'+self.sv+
                           '/characters?characterName='+self.cn+
                           '&wordType=match',params=self.key)

        chr_info = json.loads(url.text)
        print(chr_info['rows'][0]['characterName'],
              chr_info['rows'][0]['level'],
              chr_info['rows'][0]['jobName'],
              chr_info['rows'][0]['jobGrowName'],end =' ')
        self.characterId = chr_info['rows'][0]['characterId']

    def Buff_skill(self):
        url2 = requests.get('https://api.neople.co.kr/df/servers/'+self.sv+
                            '/characters/'+self.characterId+
                            '/skill/buff/equip/equipment?',params=self.key)

        self.buff_skill_item = json.loads(url2.text)
        print(self.buff_skill_item['adventureName'],
              self.buff_skill_item['guildName'],
              self.buff_skill_item['skill']['buff']['skillName'])
        try:
            for i in range(len(self.buff_skill_item['skill']['buff']['equipment'])):
                print(self.buff_skill_item['skill']['buff']['equipment'][i]['slotName'],
                  str(self.buff_skill_item['skill']['buff']['equipment'][i]['itemAvailableLevel'])+
                      self.buff_skill_item['skill']['buff']['equipment'][i]['itemRarity'],
                      self.buff_skill_item['skill']['buff']['equipment'][i]['itemName'])
        except:
            pass
        
    def avatar(self):
        url3 = requests.get('https://api.neople.co.kr/df/servers/'+self.sv+
                            '/characters/'+self.characterId+
                            '/equip/avatar?',params=self.key)
        buff_skill_avatar = json.loads(url3.text)
        try:
            print(buff_skill_avatar['avatar'][0]['slotName'],
                  buff_skill_avatar['avatar'][0]['itemName'],
                  buff_skill_avatar['avatar'][0]['emblems'][0]['itemName']+'\n',
                  buff_skill_avatar['avatar'][1]['slotName'],
                  buff_skill_avatar['avatar'][1]['itemName'],
                  buff_skill_avatar['avatar'][1]['emblems'][0]['itemName']+'\n',
                  buff_skill_avatar['avatar'][2]['slotName'],
                  buff_skill_avatar['avatar'][2]['itemName'],
                  buff_skill_avatar['avatar'][2]['emblems'][0]['itemName']+'\n',
                  buff_skill_avatar['avatar'][3]['slotName'],
                  buff_skill_avatar['avatar'][3]['itemName'],
                  buff_skill_avatar['avatar'][3]['emblems'][0]['itemName'],)
        except IndexError:
            print('아바타 없음')
        except TypeError:
            print('아바타 없음')

    def Creature(self):
        url4 = requests.get('https://api.neople.co.kr/df/servers/'+self.sv+
                            '/characters/'+self.characterId+
                            '/skill/buff/equip/creature?',params=self.key)
        buff_skill_creature = json.loads(url4.text)
        try:
            print(buff_skill_creature['skill']['buff']['creature'][0]['itemName'],
                  buff_skill_creature['skill']['buff']['creature'][0]['skill']['levelupCondition'])
        except TypeError:
            print('크리쳐 없음')

    def Buff_set_option(self):

        for i in range(len(self.buff_skill_item['skill']['buff']['equipment'])):
            self.setitems_number = self.buff_skill_item['skill']['buff']['equipment'][i]['setItemId'] 

        url5 = requests.get('https://api.neople.co.kr/df/setitems/'+self.setitems_number+'?',params=self.key)
        set_items = json.loads(url5.text)
        self.buff_Name = self.buff_skill_item['skill']['buff']['skillName']


        set3_explain = set_items['setItemOption'][0]['explain']
        set6_explain = set_items['setItemOption'][1]['explain']
        set9_explain = set_items['setItemOption'][2]['explain']

        if self.buff_Name in set3_explain:
            print(set_items['setItemOption'][0]['explain'])
        elif self.buff_Name in set6_explain:
            print(set_items['setItemOption'][1]['explain'])
        else:
            print(set_items['setItemOption'][2]['explain'])

        
    def Item_Buff_Value(self):
        for i in range(len(self.buff_skill_item['skill']['buff']['equipment'])):
            itemId = self.buff_skill_item['skill']['buff']['equipment'][i]['itemId']
            url6 = requests.get('https://api.neople.co.kr/df/items/'+itemId+'?',params=self.key)
            itemReinforceSkill = json.loads(url6.text)

            print(itemReinforceSkill)
            
'''
            
            try:             
                if itemReinforceSkill['itemReinforceSkill'][0]['levelRange'][0]['value'] != ' ':
                    print(itemReinforceSkill['itemReinforceSkill'][0]['levelRange'][0]['value'])
            except KeyError:
                #itemReinforceSkill['itemReinforceSkill'][0]['skills'][0]['value'] != ' '
                print(itemReinforceSkill['itemReinforceSkill'][0]['skills'][0]['value'])
'''                    
        
if __name__ == '__main__':
    DnF = Nexon_game()
    DnF.chracter_info()
    DnF.Buff_skill()
    DnF.avatar()
    DnF.Creature()
    DnF.Buff_set_option()
    #DnF.Item_Buff_Value()

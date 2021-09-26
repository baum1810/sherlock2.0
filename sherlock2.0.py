import requests
import praw 
import os
from os import system
from time import sleep
import colorama
from colorama import Fore, Back, Style
from mojang import MojangAPI
colorama.init(autoreset=True)






def cls():
    os.system("cls")

    
    


def username():
    username = input("Username\n> ")
    cls()
    print(f"{Fore.GREEN}searching for {username} on websides")
    print("")  
    print("")
    
    if (username.find(' ') != -1):
        data = username.split(" ")
        username1 = (f"{data[0]}-{data[1]}")
        username2 = (f"{data[0]}_{data[1]}")
        username3 = (f"{data[0]}+{data[1]}")
        username4 = (f"{data[0]}.{data[1]}")
        username5 = (f"{data[0]}{data[1]}")
        usernamelist = {username1, username2, username3, username4, username5}
        for username in usernamelist:
        
            r = requests.get(f'https://github.com/{username}')
        
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}GitHub account {username} found")
            
                r = requests.get(f'https://api.github.com/users/{username}')    
                text = r.text    
                    
                split_name_two = text
                split_name_three = split_name_two.find('"name"')
                split_name_four = split_name_two.find('"company"')
                split_name_five = (split_name_two[(split_name_three):(split_name_four)])
                split_name_six = split_name_five.replace('"name":','')
                split_name_seven = split_name_six.replace('"','')
                split_name_eight = split_name_seven.replace(',','')
                
                
                # COMPANY
                split_company_two = text
                split_company_three = split_company_two.find('"company"')
                split_company_four = split_company_two.find('"blog"')
                split_company_five = (split_company_two[(split_company_three):(split_company_four)])
                split_company_six = split_company_five.replace('"company":','')
                split_company_seven = split_company_six.replace('"','')
                split_company_eight = split_company_seven.replace(',','')
                
                # BLOG
                split_blog_two = text
                split_blog_three = split_blog_two.find('"blog"')
                split_blog_four = split_blog_two.find('"location"')
                split_blog_five = (split_blog_two[(split_blog_three):(split_blog_four)])
                split_blog_six = split_blog_five.replace('"blog":','')
                split_blog_seven = split_blog_six.replace('"','')
                split_blog_eight = split_blog_seven.replace(',','')
                
                # LOCATION
                split_location_two = text
                split_location_three = split_location_two.find('"location"')
                split_location_four = split_location_two.find('"email"')
                split_location_five = (split_location_two[(split_location_three):(split_location_four)])
                split_location_six = split_location_five.replace('"location":','')
                split_location_seven = split_location_six.replace('"','')
                split_location_eight = split_location_seven.replace(',','')
                
                # EMAIL
                split_email_two = text
                split_email_three = split_email_two.find('"email"')
                split_email_four = split_email_two.find('"hireable"')
                split_email_five = (split_email_two[(split_email_three):(split_email_four)])
                split_email_six = split_email_five.replace('"email":','')
                split_email_seven = split_email_six.replace('"','')
                split_email_eight = split_email_seven.replace(',','')
                
                # HIREABLE
                split_hireable_two = text
                split_hireable_three = split_hireable_two.find('"hireable"')
                split_hireable_four = split_hireable_two.find('"bio"')
                split_hireable_five = (split_hireable_two[(split_hireable_three):(split_hireable_four)])
                split_hireable_six = split_hireable_five.replace('"hireable":','')
                split_hireable_seven = split_hireable_six.replace('"','')
                split_hireable_eight = split_hireable_seven.replace(',','')
                
                # BIO
                split_bio_two = text
                split_bio_three = split_bio_two.find('"bio"')
                split_bio_four = split_bio_two.find('"twitter_username"')
                split_bio_five = (split_bio_two[(split_bio_three):(split_bio_four)])
                split_bio_six = split_bio_five.replace('"bio":','')
                split_bio_seven = split_bio_six.replace('"','')
                split_bio_eight = split_bio_seven.replace(',','')
                
                # TWITTER USERNAME
                split_twitter_user_two = text
                split_twitter_user_three = split_twitter_user_two.find('"twitter_username"')
                split_twitter_user_four = split_twitter_user_two.find('"public_repos"')
                split_twitter_user_five = (split_twitter_user_two[(split_twitter_user_three):(split_twitter_user_four)])
                split_twitter_user_six = split_twitter_user_five.replace('"twitter_username":','')
                split_twitter_user_seven = split_twitter_user_six.replace('"','')
                split_twitter_user_eight = split_twitter_user_seven.replace(',','')
                
                # PUBLIC REPOS
                split_public_repos_two = text
                split_public_repos_three = split_public_repos_two.find('"public_repos"')
                split_public_repos_four = split_public_repos_two.find('"public_gists"')
                split_public_repos_five = (split_public_repos_two[(split_public_repos_three):(split_public_repos_four)])
                split_public_repos_six = split_public_repos_five.replace('"public_repos":','')
                split_public_repos_seven = split_public_repos_six.replace('"','')
                split_public_repos_eight = split_public_repos_seven.replace(',','')
                
                # LOCATION
                split_public_gists_two = text
                split_public_gists_three = split_public_gists_two.find('"public_gists"')
                split_public_gists_four = split_public_gists_two.find('"followers"')
                split_public_gists_five = (split_public_gists_two[(split_public_gists_three):(split_public_gists_four)])
                split_public_gists_six = split_public_gists_five.replace('"public_gists":','')
                split_public_gists_seven = split_public_gists_six.replace('"','')
                split_public_gists_eight = split_public_gists_seven.replace(',','')
                
                # FOLLOWERS
                split_followers_two = text
                split_followers_three = split_followers_two.find('"followers"')
                split_followers_four = split_followers_two.find('"following"')
                split_followers_five = (split_followers_two[(split_followers_three):(split_followers_four)])
                split_followers_six = split_followers_five.replace('"followers":','')
                split_followers_seven = split_followers_six.replace('"','')
                split_followers_eight = split_followers_seven.replace(',','')
                
                # FOLLOWING
                split_following_two = text
                split_following_three = split_following_two.find('"following"')
                split_following_four = split_following_two.find('"created_at"')
                split_following_five = (split_following_two[(split_following_three):(split_following_four)])
                split_following_six = split_following_five.replace('"following":','')
                split_following_seven = split_following_six.replace('"','')
                split_following_eight = split_following_seven.replace(',','')
                
                
                
                
                
                
                
                result = f'''    | NAME: {split_name_eight}
    |
    | COMPANY: {split_company_eight}
    |
    | BLOG: {split_blog_eight}
    |
    | LOCATION: {split_location_eight}
    |
    | EMAIL: {split_email_eight}
    |
    | HIREABLE: {split_hireable_eight}
    |
    | BIO: {split_bio_eight}
    |
    | Twitter Username: {split_twitter_user_eight}
    |
    | Public Repos: {split_public_repos_eight}
    |
    | Public Gists: {split_public_gists_eight}
    |
    | Followers {split_followers_eight}
    |
    | Following: {split_following_eight}
    |
                '''
                
                print(result)
            else:
                pass
                #print(f"[-] github account {username} not found")
            
            
        
            
            r = requests.get(f'https://api.roblox.com/users/get-by-username?username={username}')    
            a = r.text
            if a.find('Id') == -1:
                pass
                #print(f"[-] roblox account {username} not found")
            else:
                
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Roblox account {username} found")
                r = requests.get(f'https://api.roblox.com/users/get-by-username?username={username}')  
                text = r.text
                username_to_id_one = text.find(',')
                username_to_id_two = (text[:(username_to_id_one)])
                username_to_id_four = username_to_id_two.find(':')
                username_to_id_five = (username_to_id_two[username_to_id_four:])
                username_to_id_six = username_to_id_five.replace(':', '')
                r = requests.get(f'https://users.roblox.com/v1/users/{username_to_id_six}') 
                
                
                text = r.text
                r = requests.get(f'https://inventory.roblox.com/v2/users/{username_to_id_six}/inventory')
                
                if (r.text.find('You are not authorized') != -1):
                    private_inventory = "Yes"
                else:
                    private_inventory = "No"
                baum_phrase_all_description = text[16:] # "created"
                baum_phrase_all_description_two = baum_phrase_all_description.find('"created"')
                baum_phrase_all_description_three = baum_phrase_all_description[:baum_phrase_all_description_two]
                baum_phrase_all_description_four = (len(baum_phrase_all_description_three)) - 1
                baum_phrase_all_description_five = baum_phrase_all_description_three[:baum_phrase_all_description_four]
                
                # CREATED
                baum_phrase_all_created = text.find('"created"')
                baum_phrase_all_created_one = text.find('"isBanned"')
                baum_phrase_all_created_two = text[baum_phrase_all_created:baum_phrase_all_created_one]
                baum_phrase_all_created_three = baum_phrase_all_created_two.replace('"created"', '').replace('"', '').replace(':', '').replace(',', '')
                
                # BANNED
                baum_phrase_all_isbanned_one = text.find('"isBanned"')
                baum_phrase_all_isbanned_two = text.find('"externalAppDisplayName"')
                baum_phrase_all_isbanned_three = text[baum_phrase_all_isbanned_one:baum_phrase_all_isbanned_two]
                baum_phrase_all_isbanned_four = baum_phrase_all_isbanned_three.replace('"isbanned"', '').replace(',', '').replace(':', '')
                baum_phrase_all_isbanned_five = baum_phrase_all_isbanned_four[10:]
                print(f"    | Banned: {baum_phrase_all_isbanned_five}")
                print(f"    | Createt:  {baum_phrase_all_created_three}")
                print(f"    | Private Inventory:  {private_inventory}")
                
                
                if baum_phrase_all_description_five == '"':
                    pass
                else:
                    print(f"    | Description: {baum_phrase_all_description_five}\n")
                    
            
        
            
            
        
        
            r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{username}')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Minecraft account {username} found")
                uuid = MojangAPI.get_uuid(username)
                profile = MojangAPI.get_profile(uuid)
                servers = MojangAPI.get_blocked_servers()
                drop_timestamp = MojangAPI.get_drop_timestamp(username)
                print("    | UUID: ", uuid)
                print("    | Skin Url: ", profile.skin_url)
                print("    | Blocked servers: " + f"{len(servers)}\n")
                
                
                
            else:
                pass
                #print(f"[-] minecraft account {username} not found")   
        
                    
        
            r = requests.get(f'https://replit.com/@{username}')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Repl.it account {username} found")
                
            else:
                pass
                #print(f"[-] repl.it account {username} not found")     
        
        
        
                    
            r = requests.get(f'https://passport.twitch.tv/usernames/{username}')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Twitch account {username} found")
                
            else:
                #print(f"[-] twitch account {username} not found")   
                pass
                
            
            
            
            try:    
                r = requests.get(f'https://www.picuki.com/profile/{username}')
                if r.status_code == 200:
                    print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Instagram account {username} found ")
                    if (r.text.find('Profile is private.') != -1):
                        print("    | profile is private")
                    else:
                        print("    | profile is not private")  
                
                    
                else:
                    #print(f"[-] instagram account {username} not found")   
                    pass
            except:
                pass
            r = requests.get(f"https://pastebin.com/u/{username}")
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Pastebin account {username} found")
               
            else:
                #print(f"[-] pastebin account {username} not found")   
                pass
            
            reddit = praw.Reddit(client_id="kt0mOVA3DjN_EGbjjPmqLQ",
                                    client_secret="yd6hJBRDCTjrpBsObruuxkHy3lSgfA",
                                    user_agent='Username checker (by /u/impshum)')
            try:
                
                user = reddit.redditor(username)
                if user.id:
                    print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Reddit account {username} found")
            except:
                #print(f"[-] reddit account {username} not found")
                pass
            r = requests.get(f'https://www.patreon.com/{username}')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Patreon account {username} found")
                
            else:
                #print(f"[-] patreon account {username} not found")   
                pass
            r = requests.get(f'https://gfycat.com/@{username}')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}GFCAT account {username} found")
                
            else:
                #print(f"[-] gfycat account {username} not found")   
                pass
                
            r = requests.get(f'https://forum.hackthebox.eu/profile/{username}')    
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}HackTheBox account {username} found")
                
            else:
                #print(f"[-] hackthebox account {username} not found")    
                pass
                
                
                
            r = requests.get(f'https://open.spotify.com/user/{username}')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Spotify account {username} found")
                
            else:
                #print(f"[-] spotify account {username} not found")     
                pass
                
            r = requests.get(f'https://de.xhamster.com/users/{username}')    
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}XHamster account {username} found")
                
            else:
                #print(f"[-] xhamster account {username} not found")    
                pass
                
                
                
            r = requests.get(f'https://community.cloudflare.com/u/{username}')    
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}CloudFlare account {username} found")
                
            else:
                #print(f"[-] cloudflare account {username} not found")    
                pass
                
                
            r = requests.get(f'https://pypi.org/user/{username}')    
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Pypi account {username} found")
                
            else:
                #print(f"[-] pypi account {username} not found")      
                pass    
            if (username.find('.') != -1):
                pass
            elif (username.find(':') != -1):
                pass
            elif (username.find('@') != -1):
                pass        
            elif (username.find('"') != -1):
                pass
            elif (username.find('+') != -1):
                pass        
            elif (username.find('-') != -1):
                pass        
            elif (username.find(',') != -1):
                pass
            elif (username.find(';') != -1):
                pass
            
            
                
            else:
                try:
                    r = requests.get(f'https://{username}.tumblr.com/')    
                    if r.status_code == 200:
                        print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Tumblr account {username} found")
                        
                    else:
                        #print(f"[-] tumblr account {username} not found")
                        pass
                except:
                    pass
            r = requests.get(f'https://itch.io/profile/{username}')    
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Itch.io account {username} found")
                
            else:
                #print(f"[-] itch.io account {username} not found")        
                pass  
                
            r = requests.get(f'https://in.pinterest.com/{username}')    
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Pinterest account {username} found")
                
            else:
                #print(f"[-] pinterest account {username} not found")     
                pass      
                
            r = requests.get(f'https://fortnitetracker.com/profile/all/{username}')    
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Fortnite account {username} found")
                
            else:
                #print(f"[-] fortnite account {username} not found")      
                pass
            if (username.find('.') != -1):
                pass
            elif (username.find(':') != -1):
                pass
            elif (username.find('@') != -1):
                pass        
            elif (username.find('"') != -1):
                pass
            elif (username.find('+') != -1):
                pass        
            elif (username.find('-') != -1):
                pass        
            elif (username.find(',') != -1):
                pass
            elif (username.find(';') != -1):
                pass
            else:
                
                headers = {
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
                    "Accept": "*/*",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Referer": "https://accounts.snapchat.com/",
                    "Cookie": "xsrf_token=PlEcin8s5H600toD4Swngg; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                    }
                
                url = "https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={}&xsrf_token=PlEcin8s5H600toD4Swngg".format(username)
                
                r = requests.post(url, headers=headers)
                data = r.json()
                
                status = data.get("reference").get("status_code")
                sugestions = data.get("reference").get("suggestions")
                
                if status == "OK":
                    #print(f"[-] Snapchat account {username} not found")
                    pass
                elif status == "TAKEN":
                    print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}SnapChat account {username} found")
                        
                
            r = requests.get(f'https://scratch.mit.edu/users/{username}')    
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Scratch account {username} found")
                
            else:
                #print(f"[-] scratch account {username} not found")    
                pass
            
            r = requests.get(f'https://www.chess.com/member/{username}')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Chess.com account {username} found")
                
            else:
            # print(f"[-] chess account {username} not found")    
                pass
            r = requests.get(f'https://hub.docker.com/v2/users/{username}')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Docker account {username} found")
                
            else:
                #print(f"[-] docker account {username} not found") 
                pass
            
            
            r = requests.get(f'https://www.skypli.com/profile/{username}')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Skype account {username} found")
                
            else:
                #print(f"[-] skype account {username} not found") 
                pass    
                
            
            r = requests.get(f'https://forums.opera.com/user/{username}')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Opera account {username} found")
                
            else:
            # print(f"[-] forums.opera account {username} not found") 
            
                pass   
            
            
            
            r = requests.get(f'https://trello.com/1/Members/{username}?fields=activityBlocked%2CavatarUrl%2Cbio%2CbioData%2Cconfirmed%2CfullName%2CidEnterprise%2CidMemberReferrer%2Cinitials%2CmemberType%2CnonPublic%2Cproducts%2Curl%2Cusername')    
            
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}trello account {username} found")
            else:
                pass    
            
            
            
            r = requests.get(f'https://www.xvideos.com/profiles/{username}')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}xvideos account {username} found")
            else:
                pass
            
            
        
            headers = { "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}
        
            r = requests.get(f'https://www.xboxgamertag.com/search/{username}', headers=headers)
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}xbox account {username} found")
            else:
                pass
                
                
                
            r = requests.get(f'https://apex.tracker.gg/apex/profile/origin/{username}/overview')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}apex account {username} found")
            else:
                pass
                
                
            
            r = requests.get(f'https://themeforest.net/user/{username}')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}themeforest account {username} found")
            else:
                pass
                
                
            r = requests.get(f'https://giphy.com/channel/{username}')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}giphy account {username} found")
            else:
                pass
                
                
            r = requests.get(f'https://www.pornhub.com/users/{username}')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}pornhub account {username} found")
            else:
                pass       
                
                
            r = requests.get(f'https://cash.app/${username}')    
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}cash app account {username} found")
            else:
                pass     
                
                
                
        
        
        
        
################################################################################### email check #########################################################################################################################    
   
            print("")
            print("")
            print("searching websides for possible emails")
            
            
            
            
            r = requests.get(f"https://wasteland.rfc822.org/cgi-bin/mail?inbox={username}&id=1")
            if r.text == "":
                pass
            else:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@wasteland.zz.de found")
            
            
            protonURL = "https://mail.protonmail.com/api/users/available?Name={}".format(username)
            
            headers = { "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
                        "Accept": "application/vnd.protonmail.v1+json",
                        "Accept-Language": "en-US,en;q=0.5",
                        "Accept-Encoding": "gzip, deflate",
                        "Referer": "https://mail.protonmail.com/create/new?language=en",
                        "x-pm-appversion": "Web_3.16.19",
                        "x-pm-apiversion": "3",
                        "Cache-Control": "no-cache",
                        "Pragma": "no-cache",
                        "DNT": "1", "Connection": "close"}
            
            try:
            
                chkProton = requests.get(protonURL, headers=headers, timeout=3)
            
                if chkProton.status_code == 409:
                    chkProton = chkProton.json()
                    exists = chkProton['Error']
                    if exists == "Username already used":
                        print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@protonmail.com found")
                else:
                    pass  
            except:
                pass
            
            
            
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0', 'Referer': 'https://account.mail.ru/signup?from=main&rf=auth.mail.ru'}
            mailRU = ["mail.ru", "bk.ru", "inbox.ru", "list.ru", "internet.ru"]
            
            
            
            for maildomain in mailRU:
                try:
                    
                    mailruMail = "{}@{}".format(username, maildomain)
                    data = {'email': mailruMail}
            
                    chkMailRU = requests.post('https://account.mail.ru/api/v1/user/exists', headers=headers, data=data)
                    
            
                    if chkMailRU.status_code == 200:
                        exists = chkMailRU.json()['body']['exists']
                        if exists:
                            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@{maildomain} found")
                        else: 
                            pass
            
            
                except:
                    pass
                    
            
            
            
            
            
            
            yahooURL = "https://login.yahoo.com:443/account/module/create?validateField=yid"
            yahooCookies = {"B": "10kh9jteu3edn&b=3&s=66", "AS": "v=1&s=wy5fFM96"}  # 13 8
            
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
                    "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate",
                    "Referer": "https://login.yahoo.com/account/create?.src=ym&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd&authMechanism=primary&specId=yidReg",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest",
                    "DNT": "1", "Connection": "close"}
            
            
            yahooPOST = {"specId": "yidReg", "crumb": "bshN8x9qmfJ", "acrumb": "wy5fFM96", "yid": username}
            
            
            try:
                yahooChk = requests.post(yahooURL, headers=headers, cookies=yahooCookies, data=yahooPOST, timeout=5)
            
                if '"IDENTIFIER_EXISTS"' in yahooChk.text:
                    print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@yahoo.com found")
                else:
                    pass
            except:
                pass
            
            
            
            try:
            
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
                
                tutaMail = ["tutanota.com", "tutanota.de", "tutamail.com", "tuta.io", "keemail.me"]
                
                for maildomain in tutaMail:
                
                
                
                    targetMail = "{}@{}".format(username, maildomain)
                    tutaURL = "https://mail.tutanota.com/rest/sys/mailaddressavailabilityservice?_body="
                
                    tutaCheck = requests.get('{}%7B%22_format%22%3A%220%22%2C%22mailAddress%22%3A%22{}%40{}%22%7D'.format(tutaURL, username,maildomain),headers=headers, timeout=5)
                
                    if tutaCheck.status_code == 200:
                        exists = tutaCheck.json()['available']
                
                        if exists == "0":
                            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@{maildomain} found")
                        else:
                            pass
            except:
                pass
            
            try:
            
                    _sreq = HTMLSession()
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
                    liveLst = ["outlook.com", "hotmail.com"]
                    url_template = 'https://signup.live.com/?username={}@{}&uaid=f746d3527c20414d8c86fd7f96613d85&lic=1'
                    
                    for maildomain in liveLst:
                        
                        liveChk = _sreq.get(url_template.format(username, maildomain), headers=headers)
                        liveChk.html.render(sleep=10)
                    
                        if "suggLink" in liveChk.html.html:
                            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@{maildomain} found")
                        else:
                                
                            pass 
            except:
                pass
            try:
                headers = {
                    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36",
                    "Referer": "https://www.zoho.com/",
                    "Origin": "https://www.zoho.com"
                }
                
                zohoURL = "https://accounts.zoho.com:443/accounts/validate/register.ac"
                zohoPOST = {"username": username, "servicename": "VirtualOffice", "serviceurl": "/"}
                
                
                try:
                    zohoChk = requests.post(zohoURL, headers=headers, data=zohoPOST, timeout=10)
                    if zohoChk.status_code == 200:
                        if zohoChk.json()['error']['username'] == 'This username is taken':
                            
                            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@zohomail.com found")
                except:
                    pass
            except:
                pass
            
            
            eclipsoLst = ["eclipso.eu",
                        "eclipso.de",
                        "eclipso.at",
                        "eclipso.ch",
                        "eclipso.be",
                        "eclipso.es",
                        "eclipso.it",
                        "eclipso.me",
                        "eclipso.nl",
                        "eclipso.email"]
            
            headers = {"User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36",
                    'Referer': 'https://www.eclipso.eu/signup/tariff-5',
                    'X-Requested-With': 'XMLHttpRequest'}
            
            
            for maildomain in eclipsoLst:
                try:
                    targetMail = "{}@{}".format(username, maildomain)
            
                    eclipsoURL = "https://www.eclipso.eu/index.php?action=checkAddressAvailability&address={}".format(
                        targetMail)
                    chkEclipso = requests.get(eclipsoURL, headers=headers, timeout=5)
            
                    if chkEclipso.status_code == 200:
                        if '>0<' in chkEclipso.text:
                            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@{maildomain} found")
            
                except Exception as e:
                    pass
            
            firemailDomains = ["firemail.at", "firemail.de", "firemail.eu"]
            
            headers = {"User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36",
                    'Referer': 'https://firemail.de/E-Mail-Adresse-anmelden',
                    'X-Requested-With': 'XMLHttpRequest'}
            
            for firemailDomain in firemailDomains:
                try:
                    targetMail = "{}@{}".format(username, firemailDomain)
            
                    firemailURL = "https://firemail.de/index.php?action=checkAddressAvailability&address={}".format(targetMail)
                    chkFiremail = requests.get(firemailURL, headers=headers, timeout=10)
            
                    if chkFiremail.status_code == 200:
                        if '>0<' in chkFiremail.text:
                            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@{maildomain} found")
                except:
                    pass
            
            
            
            startmailURL = "https://mail.startmail.com:443/api/AvailableAddresses/{}%40startmail.com".format(username)
            headers = {"User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36",
                    "X-Requested-With": "1.94.0"}
            
            
            try:
                chkStartmail = requests.get(startmailURL, headers=headers, timeout=10)
            
                if chkStartmail.status_code == 404:
                    print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@startmail.com found")
            
            except:
                pass    
            
            
            print("")
            print("")
            print("Finished scann")
    else:
        r = requests.get(f'https://github.com/{username}')
        
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}GitHub account {username} found")
        
            r = requests.get(f'https://api.github.com/users/{username}')    
            text = r.text    
                
            split_name_two = text
            split_name_three = split_name_two.find('"name"')
            split_name_four = split_name_two.find('"company"')
            split_name_five = (split_name_two[(split_name_three):(split_name_four)])
            split_name_six = split_name_five.replace('"name":','')
            split_name_seven = split_name_six.replace('"','')
            split_name_eight = split_name_seven.replace(',','')
            
            
            # COMPANY
            split_company_two = text
            split_company_three = split_company_two.find('"company"')
            split_company_four = split_company_two.find('"blog"')
            split_company_five = (split_company_two[(split_company_three):(split_company_four)])
            split_company_six = split_company_five.replace('"company":','')
            split_company_seven = split_company_six.replace('"','')
            split_company_eight = split_company_seven.replace(',','')
            
            # BLOG
            split_blog_two = text
            split_blog_three = split_blog_two.find('"blog"')
            split_blog_four = split_blog_two.find('"location"')
            split_blog_five = (split_blog_two[(split_blog_three):(split_blog_four)])
            split_blog_six = split_blog_five.replace('"blog":','')
            split_blog_seven = split_blog_six.replace('"','')
            split_blog_eight = split_blog_seven.replace(',','')
            
            # LOCATION
            split_location_two = text
            split_location_three = split_location_two.find('"location"')
            split_location_four = split_location_two.find('"email"')
            split_location_five = (split_location_two[(split_location_three):(split_location_four)])
            split_location_six = split_location_five.replace('"location":','')
            split_location_seven = split_location_six.replace('"','')
            split_location_eight = split_location_seven.replace(',','')
            
            # EMAIL
            split_email_two = text
            split_email_three = split_email_two.find('"email"')
            split_email_four = split_email_two.find('"hireable"')
            split_email_five = (split_email_two[(split_email_three):(split_email_four)])
            split_email_six = split_email_five.replace('"email":','')
            split_email_seven = split_email_six.replace('"','')
            split_email_eight = split_email_seven.replace(',','')
            
            # HIREABLE
            split_hireable_two = text
            split_hireable_three = split_hireable_two.find('"hireable"')
            split_hireable_four = split_hireable_two.find('"bio"')
            split_hireable_five = (split_hireable_two[(split_hireable_three):(split_hireable_four)])
            split_hireable_six = split_hireable_five.replace('"hireable":','')
            split_hireable_seven = split_hireable_six.replace('"','')
            split_hireable_eight = split_hireable_seven.replace(',','')
            
            # BIO
            split_bio_two = text
            split_bio_three = split_bio_two.find('"bio"')
            split_bio_four = split_bio_two.find('"twitter_username"')
            split_bio_five = (split_bio_two[(split_bio_three):(split_bio_four)])
            split_bio_six = split_bio_five.replace('"bio":','')
            split_bio_seven = split_bio_six.replace('"','')
            split_bio_eight = split_bio_seven.replace(',','')
            
            # TWITTER USERNAME
            split_twitter_user_two = text
            split_twitter_user_three = split_twitter_user_two.find('"twitter_username"')
            split_twitter_user_four = split_twitter_user_two.find('"public_repos"')
            split_twitter_user_five = (split_twitter_user_two[(split_twitter_user_three):(split_twitter_user_four)])
            split_twitter_user_six = split_twitter_user_five.replace('"twitter_username":','')
            split_twitter_user_seven = split_twitter_user_six.replace('"','')
            split_twitter_user_eight = split_twitter_user_seven.replace(',','')
            
            # PUBLIC REPOS
            split_public_repos_two = text
            split_public_repos_three = split_public_repos_two.find('"public_repos"')
            split_public_repos_four = split_public_repos_two.find('"public_gists"')
            split_public_repos_five = (split_public_repos_two[(split_public_repos_three):(split_public_repos_four)])
            split_public_repos_six = split_public_repos_five.replace('"public_repos":','')
            split_public_repos_seven = split_public_repos_six.replace('"','')
            split_public_repos_eight = split_public_repos_seven.replace(',','')
            
            # LOCATION
            split_public_gists_two = text
            split_public_gists_three = split_public_gists_two.find('"public_gists"')
            split_public_gists_four = split_public_gists_two.find('"followers"')
            split_public_gists_five = (split_public_gists_two[(split_public_gists_three):(split_public_gists_four)])
            split_public_gists_six = split_public_gists_five.replace('"public_gists":','')
            split_public_gists_seven = split_public_gists_six.replace('"','')
            split_public_gists_eight = split_public_gists_seven.replace(',','')
            
            # FOLLOWERS
            split_followers_two = text
            split_followers_three = split_followers_two.find('"followers"')
            split_followers_four = split_followers_two.find('"following"')
            split_followers_five = (split_followers_two[(split_followers_three):(split_followers_four)])
            split_followers_six = split_followers_five.replace('"followers":','')
            split_followers_seven = split_followers_six.replace('"','')
            split_followers_eight = split_followers_seven.replace(',','')
            
            # FOLLOWING
            split_following_two = text
            split_following_three = split_following_two.find('"following"')
            split_following_four = split_following_two.find('"created_at"')
            split_following_five = (split_following_two[(split_following_three):(split_following_four)])
            split_following_six = split_following_five.replace('"following":','')
            split_following_seven = split_following_six.replace('"','')
            split_following_eight = split_following_seven.replace(',','')
            
            
            
            
            
            
            
            result = f'''    | NAME: {split_name_eight}
    |
    | COMPANY: {split_company_eight}
    |
    | BLOG: {split_blog_eight}
    |
    | LOCATION: {split_location_eight}
    |
    | EMAIL: {split_email_eight}
    |
    | HIREABLE: {split_hireable_eight}
    |
    | BIO: {split_bio_eight}
    |
    | Twitter Username: {split_twitter_user_eight}
    |
    | Public Repos: {split_public_repos_eight}
    |
    | Public Gists: {split_public_gists_eight}
    |
    | Followers {split_followers_eight}
    |
    | Following: {split_following_eight}
    |
              
            '''   
            print(result)
        else:
                pass
                #print(f"[-] github account {username} not found")
            
            
        
            
        r = requests.get(f'https://api.roblox.com/users/get-by-username?username={username}')    
        a = r.text
        if a.find('Id') == -1:
            pass
            #print(f"[-] roblox account {username} not found")
        else:
            
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Roblox account {username} found")
            r = requests.get(f'https://api.roblox.com/users/get-by-username?username={username}')  
            text = r.text
            username_to_id_one = text.find(',')
            username_to_id_two = (text[:(username_to_id_one)])
            username_to_id_four = username_to_id_two.find(':')
            username_to_id_five = (username_to_id_two[username_to_id_four:])
            username_to_id_six = username_to_id_five.replace(':', '')
            r = requests.get(f'https://users.roblox.com/v1/users/{username_to_id_six}') 
            
            
            text = r.text
            r = requests.get(f'https://inventory.roblox.com/v2/users/{username_to_id_six}/inventory')
            
            if (r.text.find('You are not authorized') != -1):
                private_inventory = "Yes"
            else:
                private_inventory = "No"
            baum_phrase_all_description = text[16:] # "created"
            baum_phrase_all_description_two = baum_phrase_all_description.find('"created"')
            baum_phrase_all_description_three = baum_phrase_all_description[:baum_phrase_all_description_two]
            baum_phrase_all_description_four = (len(baum_phrase_all_description_three)) - 1
            baum_phrase_all_description_five = baum_phrase_all_description_three[:baum_phrase_all_description_four]
            
            # CREATED
            baum_phrase_all_created = text.find('"created"')
            baum_phrase_all_created_one = text.find('"isBanned"')
            baum_phrase_all_created_two = text[baum_phrase_all_created:baum_phrase_all_created_one]
            baum_phrase_all_created_three = baum_phrase_all_created_two.replace('"created"', '').replace('"', '').replace(':', '').replace(',', '')
            
            # BANNED
            baum_phrase_all_isbanned_one = text.find('"isBanned"')
            baum_phrase_all_isbanned_two = text.find('"externalAppDisplayName"')
            baum_phrase_all_isbanned_three = text[baum_phrase_all_isbanned_one:baum_phrase_all_isbanned_two]
            baum_phrase_all_isbanned_four = baum_phrase_all_isbanned_three.replace('"isbanned"', '').replace(',', '').replace(':', '')
            baum_phrase_all_isbanned_five = baum_phrase_all_isbanned_four[10:]
            print(f"    | Banned: {baum_phrase_all_isbanned_five}")
            print(f"    | Createt:  {baum_phrase_all_created_three}")
            print(f"    | Private Inventory:  {private_inventory}")
            
            
            if baum_phrase_all_description_five == '"':
                pass
            else:
                print(f"    | Description: {baum_phrase_all_description_five}\n")
                
        
        
        
        
        
        
        r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{username}')
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Minecraft account {username} found")
            uuid = MojangAPI.get_uuid(username)
            profile = MojangAPI.get_profile(uuid)
            servers = MojangAPI.get_blocked_servers()
            drop_timestamp = MojangAPI.get_drop_timestamp(username)
            print("    | UUID: ", uuid)
            print("    | Skin Url: ", profile.skin_url)
            print("    | Blocked servers: " + f"{len(servers)}\n")
            
            
            
        else:
            pass
            #print(f"[-] minecraft account {username} not found")   
        
                
        
        r = requests.get(f'https://replit.com/@{username}')
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Repl.it account {username} found")
            
        else:
            pass
            #print(f"[-] repl.it account {username} not found")     
        
        
        
                
        r = requests.get(f'https://passport.twitch.tv/usernames/{username}')
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Twitch account {username} found")
            
        else:
            #print(f"[-] twitch account {username} not found")   
            pass
            
        
        
        
        try:    
            r = requests.get(f'https://www.picuki.com/profile/{username}')
            if r.status_code == 200:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Instagram account {username} found ")
                if (r.text.find('Profile is private.') != -1):
                    print("    | profile is private")
                else:
                    print("    | profile is not private")  
            
                
            else:
                #print(f"[-] instagram account {username} not found")   
                pass
        except:
            pass
        r = requests.get(f"https://pastebin.com/u/{username}")
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Pastebin account {username} found")
            
        else:
            #print(f"[-] pastebin account {username} not found")   
            pass
        
        reddit = praw.Reddit(client_id="kt0mOVA3DjN_EGbjjPmqLQ",
                                client_secret="yd6hJBRDCTjrpBsObruuxkHy3lSgfA",
                                user_agent='Username checker (by /u/impshum)')
        try:
            
            user = reddit.redditor(username)
            if user.id:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Reddit account {username} found")
        except:
            #print(f"[-] reddit account {username} not found")
            pass
        r = requests.get(f'https://www.patreon.com/{username}')
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Patreon account {username} found")
            
        else:
            #print(f"[-] patreon account {username} not found")   
            pass
        r = requests.get(f'https://gfycat.com/@{username}')
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}GFCAT account {username} found")
            
        else:
            #print(f"[-] gfycat account {username} not found")   
            pass
            
        r = requests.get(f'https://forum.hackthebox.eu/profile/{username}')    
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}HackTheBox account {username} found")
            
        else:
            #print(f"[-] hackthebox account {username} not found")    
            pass
            
            
            
        r = requests.get(f'https://open.spotify.com/user/{username}')
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Spotify account {username} found")
            
        else:
            #print(f"[-] spotify account {username} not found")     
            pass
            
        r = requests.get(f'https://de.xhamster.com/users/{username}')    
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}XHamster account {username} found")
            
        else:
            #print(f"[-] xhamster account {username} not found")    
            pass
            
            
            
        r = requests.get(f'https://community.cloudflare.com/u/{username}')    
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}CloudFlare account {username} found")
            
        else:
            #print(f"[-] cloudflare account {username} not found")    
            pass
            
            
        r = requests.get(f'https://pypi.org/user/{username}')    
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Pypi account {username} found")
            
        else:
            #print(f"[-] pypi account {username} not found")      
            pass    
        if (username.find('.') != -1):
            pass
        elif (username.find(':') != -1):
            pass
        elif (username.find('@') != -1):
            pass        
        elif (username.find('"') != -1):
            pass
        elif (username.find('+') != -1):
            pass        
        elif (username.find('-') != -1):
            pass        
        elif (username.find(',') != -1):
            pass
        elif (username.find(';') != -1):
            pass
        
        
            
        else:
            try:
                r = requests.get(f'https://{username}.tumblr.com/')    
                if r.status_code == 200:
                    print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Tumblr account {username} found")
                    
                else:
                    #print(f"[-] tumblr account {username} not found")
                    pass
            except:
                pass
        r = requests.get(f'https://itch.io/profile/{username}')    
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Itch.io account {username} found")
            
        else:
            #print(f"[-] itch.io account {username} not found")        
            pass  
            
        r = requests.get(f'https://in.pinterest.com/{username}')    
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Pinterest account {username} found")
            
        else:
            #print(f"[-] pinterest account {username} not found")     
            pass      
            
        r = requests.get(f'https://fortnitetracker.com/profile/all/{username}')    
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Fortnite account {username} found")
            
        else:
            #print(f"[-] fortnite account {username} not found")      
            pass
        if (username.find('.') != -1):
            pass
        elif (username.find(':') != -1):
            pass
        elif (username.find('@') != -1):
            pass        
        elif (username.find('"') != -1):
            pass
        elif (username.find('+') != -1):
            pass        
        elif (username.find('-') != -1):
            pass        
        elif (username.find(',') != -1):
            pass
        elif (username.find(';') != -1):
            pass
        else:
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
                "Accept": "*/*",
                "Accept-Language": "en-US,en;q=0.5",
                "Referer": "https://accounts.snapchat.com/",
                "Cookie": "xsrf_token=PlEcin8s5H600toD4Swngg; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==",
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                }
            
            url = "https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={}&xsrf_token=PlEcin8s5H600toD4Swngg".format(username)
            
            r = requests.post(url, headers=headers)
            data = r.json()
            
            status = data.get("reference").get("status_code")
            sugestions = data.get("reference").get("suggestions")
            
            if status == "OK":
                #print(f"[-] Snapchat account {username} not found")
                pass
            elif status == "TAKEN":
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}SnapChat account {username} found")
                    
            
        r = requests.get(f'https://scratch.mit.edu/users/{username}')    
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Scratch account {username} found")
            
        else:
            #print(f"[-] scratch account {username} not found")    
            pass
        
        r = requests.get(f'https://www.chess.com/member/{username}')
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Chess.com account {username} found")
            
        else:
        # print(f"[-] chess account {username} not found")    
            pass
        r = requests.get(f'https://hub.docker.com/v2/users/{username}')
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Docker account {username} found")
            
        else:
            #print(f"[-] docker account {username} not found") 
            pass
        
        
        r = requests.get(f'https://www.skypli.com/profile/{username}')
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Skype account {username} found")
            
        else:
            #print(f"[-] skype account {username} not found") 
            pass    
            
        
        r = requests.get(f'https://forums.opera.com/user/{username}')
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}Opera account {username} found")
            
        else:
        # print(f"[-] forums.opera account {username} not found") 
        
            pass   
        
        
        
        r = requests.get(f'https://trello.com/1/Members/{username}?fields=activityBlocked%2CavatarUrl%2Cbio%2CbioData%2Cconfirmed%2CfullName%2CidEnterprise%2CidMemberReferrer%2Cinitials%2CmemberType%2CnonPublic%2Cproducts%2Curl%2Cusername')    
        
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}trello account {username} found")
        else:
            pass    
        
        
        
        r = requests.get(f'https://www.xvideos.com/profiles/{username}')
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}xvideos account {username} found")
        else:
            pass
        
        
        
        headers = { "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}
        
        r = requests.get(f'https://www.xboxgamertag.com/search/{username}', headers=headers)
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}xbox account {username} found")
        else:
            pass
            
            
            
        r = requests.get(f'https://apex.tracker.gg/apex/profile/origin/{username}/overview')
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}apex account {username} found")
        else:
            pass
            
            
        
        r = requests.get(f'https://themeforest.net/user/{username}')
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}themeforest account {username} found")
        else:
            pass
            
            
        r = requests.get(f'https://giphy.com/channel/{username}')
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}giphy account {username} found")
        else:
            pass
            
            
        r = requests.get(f'https://www.pornhub.com/users/{username}')
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}pornhub account {username} found")
        else:
            pass       
            
            
        r = requests.get(f'https://cash.app/${username}')    
        if r.status_code == 200:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}cash app account {username} found")
        else:
            pass     
            
            
            
        
        
        
        
############################################################################### email check #########################################################################################################################    
   
        print("")
        print("")
        print("searching websides for possible emails")
        
        
        
        
        r = requests.get(f"https://wasteland.rfc822.org/cgi-bin/mail?inbox={username}&id=1")
        if r.text == "":
            pass
        else:
            print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@wasteland.zz.de found")
        
        
        protonURL = "https://mail.protonmail.com/api/users/available?Name={}".format(username)
        
        headers = { "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
                    "Accept": "application/vnd.protonmail.v1+json",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate",
                    "Referer": "https://mail.protonmail.com/create/new?language=en",
                    "x-pm-appversion": "Web_3.16.19",
                    "x-pm-apiversion": "3",
                    "Cache-Control": "no-cache",
                    "Pragma": "no-cache",
                    "DNT": "1", "Connection": "close"}
        
        try:
        
            chkProton = requests.get(protonURL, headers=headers, timeout=3)
        
            if chkProton.status_code == 409:
                chkProton = chkProton.json()
                exists = chkProton['Error']
                if exists == "Username already used":
                    print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@protonmail.com found")
            else:
                pass  
        except:
            pass
        
        
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0', 'Referer': 'https://account.mail.ru/signup?from=main&rf=auth.mail.ru'}
        mailRU = ["mail.ru", "bk.ru", "inbox.ru", "list.ru", "internet.ru"]
        
        
        
        for maildomain in mailRU:
            try:
                
                mailruMail = "{}@{}".format(username, maildomain)
                data = {'email': mailruMail}
        
                chkMailRU = requests.post('https://account.mail.ru/api/v1/user/exists', headers=headers, data=data)
                
        
                if chkMailRU.status_code == 200:
                    exists = chkMailRU.json()['body']['exists']
                    if exists:
                        print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@{maildomain} found")
                    else: 
                        pass
        
        
            except:
                pass
                
        
        
        
        
        
        
        yahooURL = "https://login.yahoo.com:443/account/module/create?validateField=yid"
        yahooCookies = {"B": "10kh9jteu3edn&b=3&s=66", "AS": "v=1&s=wy5fFM96"}  # 13 8
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
                "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate",
                "Referer": "https://login.yahoo.com/account/create?.src=ym&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd&authMechanism=primary&specId=yidReg",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest",
                "DNT": "1", "Connection": "close"}
        
        
        yahooPOST = {"specId": "yidReg", "crumb": "bshN8x9qmfJ", "acrumb": "wy5fFM96", "yid": username}
        
        
        try:
            yahooChk = requests.post(yahooURL, headers=headers, cookies=yahooCookies, data=yahooPOST, timeout=5)
        
            if '"IDENTIFIER_EXISTS"' in yahooChk.text:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@yahoo.com found")
            else:
                pass
        except:
            pass
        
        
        
        try:
        
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
            
            tutaMail = ["tutanota.com", "tutanota.de", "tutamail.com", "tuta.io", "keemail.me"]
            
            for maildomain in tutaMail:
            
            
            
                targetMail = "{}@{}".format(username, maildomain)
                tutaURL = "https://mail.tutanota.com/rest/sys/mailaddressavailabilityservice?_body="
            
                tutaCheck = requests.get('{}%7B%22_format%22%3A%220%22%2C%22mailAddress%22%3A%22{}%40{}%22%7D'.format(tutaURL, username,maildomain),headers=headers, timeout=5)
            
                if tutaCheck.status_code == 200:
                    exists = tutaCheck.json()['available']
            
                    if exists == "0":
                        print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@{maildomain} found")
                    else:
                        pass
        except:
            pass
        
        try:
        
                _sreq = HTMLSession()
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
                liveLst = ["outlook.com", "hotmail.com"]
                url_template = 'https://signup.live.com/?username={}@{}&uaid=f746d3527c20414d8c86fd7f96613d85&lic=1'
                
                for maildomain in liveLst:
                    
                    liveChk = _sreq.get(url_template.format(username, maildomain), headers=headers)
                    liveChk.html.render(sleep=10)
                
                    if "suggLink" in liveChk.html.html:
                        print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@{maildomain} found")
                    else:
                            
                        pass 
        except:
            pass
        try:
            headers = {
                "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36",
                "Referer": "https://www.zoho.com/",
                "Origin": "https://www.zoho.com"
            }
            
            zohoURL = "https://accounts.zoho.com:443/accounts/validate/register.ac"
            zohoPOST = {"username": username, "servicename": "VirtualOffice", "serviceurl": "/"}
            
            
            try:
                zohoChk = requests.post(zohoURL, headers=headers, data=zohoPOST, timeout=10)
                if zohoChk.status_code == 200:
                    if zohoChk.json()['error']['username'] == 'This username is taken':
                        
                        print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@zohomail.com found")
            except:
                pass
        except:
            pass
        
        
        eclipsoLst = ["eclipso.eu",
                    "eclipso.de",
                    "eclipso.at",
                    "eclipso.ch",
                    "eclipso.be",
                    "eclipso.es",
                    "eclipso.it",
                    "eclipso.me",
                    "eclipso.nl",
                    "eclipso.email"]
        
        headers = {"User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36",
                'Referer': 'https://www.eclipso.eu/signup/tariff-5',
                'X-Requested-With': 'XMLHttpRequest'}
        
        
        for maildomain in eclipsoLst:
            try:
                targetMail = "{}@{}".format(username, maildomain)
        
                eclipsoURL = "https://www.eclipso.eu/index.php?action=checkAddressAvailability&address={}".format(
                    targetMail)
                chkEclipso = requests.get(eclipsoURL, headers=headers, timeout=5)
        
                if chkEclipso.status_code == 200:
                    if '>0<' in chkEclipso.text:
                        print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@{maildomain} found")
        
            except Exception as e:
                pass
        
        firemailDomains = ["firemail.at", "firemail.de", "firemail.eu"]
        
        headers = {"User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36",
                'Referer': 'https://firemail.de/E-Mail-Adresse-anmelden',
                'X-Requested-With': 'XMLHttpRequest'}
        
        for firemailDomain in firemailDomains:
            try:
                targetMail = "{}@{}".format(username, firemailDomain)
        
                firemailURL = "https://firemail.de/index.php?action=checkAddressAvailability&address={}".format(targetMail)
                chkFiremail = requests.get(firemailURL, headers=headers, timeout=10)
        
                if chkFiremail.status_code == 200:
                    if '>0<' in chkFiremail.text:
                        print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@{maildomain} found")
            except:
                pass
        
        
        
        startmailURL = "https://mail.startmail.com:443/api/AvailableAddresses/{}%40startmail.com".format(username)
        headers = {"User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36",
                "X-Requested-With": "1.94.0"}
        
        
        try:
            chkStartmail = requests.get(startmailURL, headers=headers, timeout=10)
        
            if chkStartmail.status_code == 404:
                print(f"{Fore.BLUE}[{Fore.WHITE}+{Fore.BLUE}] {Fore.GREEN}{username}@startmail.com found")
        
        except:
            pass    
            
            
            print("")
            print("")
            print("Finished scann")
    
def credits():
    cls()
    print("Createt by baum\nDiscord: baum#2873\nGithub: https://github.com/baum1810")
    print("")
    print("inspired by:\nhttps://github.com/sherlock-project/sherlock\nhttps://github.com/sharsil/mailcat\nhttps://github.com/megadose/holehe")
    print("\nHelped with phrasing Arclight#7615")    
    system("pause")
    chooose()
    
def websides():
    print("""
    Websides: 
    https://github.com
    https://roblox.com
    https://minecraft.net
    https://replit.com
    https://twitch.com
    https://picuki.com
    https://pastebin.com
    https://reddit.com
    https://.patreon.com
    https://gfycat.com
    https://forum.hackthebox.eu
    https://spotify.com
    https://de.xhamster.com
    https://community.cloudflare.com/
    https://pypi.org
    https://tumblr.com
    https://itch.io
    https://in.pinterest.com/
    https://fortnitetracker.com
    https://snapchat.com
    https://scratch.mit.edu
    https://chess.com
    https://hub.docker.com
    https://skypli.com
    https://forums.opera.com
    https://trello.com
    https://xvideos.com
    https://xboxgamertag.com
    https://apex.tracker.gg
    https://giphy.com
    https://www.pornhub.com
    https://cash.app/
    
    
    Emails: 
    wasteland.zz.de
    protonmail.com
    mail.ru
    bk.ru
    inbox.ru
    list.ru
    internet.ru
    yahoo.com
    tutanota.com
    tutanota.de
    tutamail.com
    tuta.io
    keemail.me
    outlook.com
    hotmail.com
    zohomail.com
    eclipso.eu
    eclipso.de
    eclipso.at
    eclipso.ch
    eclipso.be
    eclipso.es
    eclipso.it
    eclipso.me
    eclipso.nl
    eclipso.email
    firemail.at
    firemail.de
    firemail.eu
    startmail.com
    
    
    """)
    
    system("pause")
    chooose()
    
    
    
def chooose():
    cls()
    choose = input("[1] Username, checks on multible websides if the account exist\n[2] Email, checks on wich websides the email is registered\n[3] Credits\n[4] websides, showes you wich websides and email providers are used in the check\n> ")
    if choose == "1":
        cls()
        username()
        
    elif choose == "2":
        cls()
        print("comming soon")
        system("pause")
        chooose()
        
        
    elif choose == "3":
        credits()
        
    elif choose == "4":
        cls()
        websides()
 
 
 
chooose()

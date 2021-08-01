import os
try:
    import InstagramAPI
    import sys
    import time
    import random
    import requests
    from instabot import Bot
    from colorama import Fore
    from instagram_private_api import Client
    from instagram_private_api_extensions import pagination
    import uuid
except:
    os.system('pip install instagram_private_api')
    os.system('pip install instagram_private_api_extensions')
    os.system('pip install InstagramAPI')
    os.system('pip install sys')
    os.system('pip install time')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install instabot')
    os.system('pip install colorama')

w = Fore.WHITE
m = Fore.MAGENTA
r = Fore.RED
c = Fore.CYAN
R = Fore.RESET

print(f'''
      {w}╔═══════════════════════════════════════╗
      {w}║  {m}███████╗    ██╗         ███╗   ███╗{w}  ║
      {w}║  {m}╚════██║    ██║         ████╗ ████║{w}  ║
      {w}║  {m}    ██╔╝    ██║         ██╔████╔██║{w}  ║
      {w}║  {m}   ██╔╝     ██║         ██║╚██╔╝██║{w}  ║
      {w}║  {m}   ██║      ███████╗    ██║ ╚═╝ ██║{w}  ║
      {w}║  {m}   ╚═╝      ╚══════╝    ╚═╝     ╚═╝{w}  ║
      {w}║             {r}IG Cleaner              {w}  ║
      {w}╚══════════════════7lM══════════════════╝
     [{r}1{w}] {c}Delete Post {w}[{r}2{w}] {c}UnFollow {w}[{r}3{w}] {c}Delete DM
        {w}[{r}4{w}] {c}Delete Bio {m}& {c}name {w}[{r}5{w}] {c}UnSave All ''')
num = input('                     NUMBER : ')

#UnFollow 1
if num == '2':
    def GetAllFollowing(bot, user_id):
        following = []
        next_max_id = True
        while next_max_id:
            if next_max_id is True:
                next_max_id = ''
            _ = bot.getUserFollowings(user_id, maxid=next_max_id)
            following.extend(bot.LastJson.get('users', []))
            next_max_id = bot.LastJson.get('next_max_id', '')
        following = set([_['pk'] for _ in following])
        return following

    def GetAllFollowers(bot, user_id):
        followers = []
        next_max_id = True
        while next_max_id:
            if next_max_id is True:
                next_max_id = ''
            _ = bot.getUserFollowers(user_id, maxid=next_max_id)
            followers.extend(bot.LastJson.get('users', []))
            next_max_id = bot.LastJson.get('next_max_id', '')
        followers = set([1])
        return followers


    if __name__ == '__main__':
        print('\nYour account must not have a secure')
        username = str(input("user : "))
        password = str(input("pass : "))
        time.sleep(1)
        num_unfollows = int(input("\nHow many you want delete ? : "))
        time.sleep(1)
        max_delay = int(input("\nTime for delete ( best time 5 ) : "))

        ig = InstagramAPI(username, password)

        success = ig.login()
        if not success:
            print('error log in Try again')
            print('the pass is erorr or the account have a secure !')
            sys.exit()

        ig.getSelfUsernameInfo()
        self_id = ig.LastJson['user']['pk']

        followers = GetAllFollowers(ig, self_id)

        following = GetAllFollowing(ig, self_id)


        print('your following {}'.format(len(following)))
        print('your followers {}'.format(len(followers)))

        time.sleep(1)

        unreciprocated = following - followers
        free_followers = followers - following

        for _ in list(unreciprocated)[:min(len(unreciprocated), num_unfollows)]:
            ig.getUsernameInfo(str(_))
            print('account {} done delete'.format(ig.LastJson['user']['username']))
            ig.unfollow(str(_))
            ni = random.choice([1, 2, 3, 4, 5])
            time.sleep(max_delay + ni)

#Delete Post 2
if num == '1':
    user = input('username : ')
    password = input('password : ')

    log = Bot()

    s = requests.Session()
    log.login(username=user, password=password)
    os.system("clear")

    headerr = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '274',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',
        'x-instagram-ajax': '1cb44f68ffec',
        'x-requested-with': 'XMLHttpRequest'
    }

    url = 'https://www.instagram.com/accounts/login/ajax/'

    data = {
        'username': user,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }

    loginreq = s.post(url, data=data, headers=headerr)

    if ('"authenticated": false') in loginreq.text:
        print('Login Failed')
        exit()
    elif ('"authenticated": true') in loginreq.text:
        print('Done lgin | ' + user)

    print('\nIf you login Successfuly Then Don not skip this else try to forget your password')
    print(' ')

    print('Get Post Wait ')
    time.sleep(6)

    try:
        media = log.get_total_user_medias(log.user_id)
    except:
        pass

    print("[ " + str(len(media)) + " ]" + " Posts Found")

    for ids in media:
        sp = ids.split("_")
        id = sp[0]

        head = {
            "content-type": "application/x-www-form-urlencoded", "x-instagram-ajax": "bffcb3f0082e",
            "accept": "*/*",
            "referer": "https://www.instagram.com/p/", "accept-language": "en-US,en;q=0.9,fa;q=0.8",
            "origin": "https://www.instagram.com", "x-csrftoken": loginreq.cookies['csrftoken'],
            "user-agent": "Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36"
        }

        urls = "https://www.instagram.com/create/" + id + "/delete/"

        delete_ps = s.post(urls, headers=head, cookies=loginreq.cookies)

        if ('{"did_delete":true,"status":"ok"}' in delete_ps.text):
            print("Deleted : " + str(ids))
            time.sleep(2)
        else:
            print("Faild : " + str(ids))
            time.sleep(2)

        time.sleep(3)

    print('Done delete All posts')

#UnSave 3
if num == '5':
    user_name = input('username : ')
    password = input('password : ')

    api = Client(user_name, password)

    items=[]
    for results in pagination.page(api.saved_feed, args={}):
       if results.get('items'):
            items.extend(results['items'])

    print("Starting unsaving posts.....")

    for i,x in enumerate(items):
       z = items[i]['media']['pk']
       api.unsave_photo(media_id=z)
       time.sleep(1)
       print("Unsaved: ", z)

#DM cleaner 4
if num == '3':
    def out():
        print("+" + "-" * 10 + "Close" + "-" * 10 + "+")
        input("[$] Click Enter To Exit...")


    os.system('cls')
    os.system('color a')
    rs = requests.session()
    uid = str(uuid.uuid4())
    successfully_deleted = 0
    error_deleted = 0
    All = 0

    print("""
        █████╗ ██████╗ ██████╗ 
       ██╔══██╗██╔══██╗██╔══██╗
       ╚█████╔╝██████╔╝██████╔╝
       ██╔══██╗██╔═══╝ ██╔══██╗
       ╚█████╔╝██║     ██║  ██║
        ╚════╝ ╚═╝     ╚═╝  ╚═╝        
          [ DM Cleaner ]      
    """)
    print("instagram [ @T8PR ] Follow Me <3")
    print("+" + "-" * 10 + "DM-Cleaner" + "-" * 10 + "+")
    user = input("[?] Enter Your Username : ")
    Pass = input("[?] Enter Your Password : ")
    try:
        slp = int(input("[?] Enter The Sleep : "))
    except ValueError:
        print("[-] Just Numbers !!")
        out()
        sys.exit()

    url = 'https://i.instagram.com/api/v1/accounts/login/'
    headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'
    }
    data = {
        'uuid': uid,
        'password': Pass,
        'username': user,
        'device_id': uid,
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_countn': '0'
    }

    LOG = rs.post(url, data=data, headers=headers)
    if LOG.text.find('is_private') >= 0:
        rs.headers.update({ 'X-CSRFToken': LOG.cookies['csrftoken'] })
        sid = LOG.cookies['sessionid']
        print(f"[+] Login Was Success To @{user}")
        print("+" + "-" * 10 + "Delete" + "-" * 10 + "+")


        def clear():
            global successfully_deleted, error_deleted, All, slp
            while True:
                dm_url = 'https://i.instagram.com/api/v1/direct_v2/inbox/?persistentBadging=true&cursor='
                dm_headers = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                    'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; ds_user_id=46165248972; shbid=13126; shbts=1616804137.1316793; rur=PRN; csrftoken=mnnbqhStTDAfu10DkI2VrW5VoCg9InFk; sessionid={sid}',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/',
                    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4'
                }
                get_dm = rs.get(dm_url, headers=dm_headers)
                try:
                    users = str(get_dm.json()['inbox']['threads'][0]['users'][0]['username'])
                    ids = str(get_dm.json()['inbox']['threads'][0]['thread_id'])
                    delete_dm_url = f'https://i.instagram.com/api/v1/direct_v2/threads/{ids}/hide/'
                    delete_dm_headers = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                        'content-length': '0',
                        'content-type': 'application/x-www-form-urlencoded',
                        'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; ds_user_id=46165248972; shbid=13126; shbts=1616804137.1316793; rur=PRN; csrftoken=mnnbqhStTDAfu10DkI2VrW5VoCg9InFk; sessionid={sid}',
                        'origin': 'https://www.instagram.com',
                        'referer': 'https://www.instagram.com/',
                        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-site',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
                        'x-csrftoken': 'mnnbqhStTDAfu10DkI2VrW5VoCg9InFk',
                        'x-ig-app-id': '1217981644879628',
                        'x-ig-www-claim': 'hmac.AR24Fkd2DvunQ5ELQD_I_6FoVMTbIdkiDD08ZF2jyPhpEmIg',
                        'x-instagram-ajax': '753ce878cd6d'
                    }
                    delete = rs.post(delete_dm_url, headers=delete_dm_headers)
                    if '"status":"ok"' or "<Response [200]>" in delete:
                        successfully_deleted += 1
                        All += 1
                        print(f"[+] Successfully Delete @{users} [{All}]")
                    else:
                        All += 1
                        error_deleted += 1
                        print(f"[-] Error Delete @{users} [{All}]")
                    if error_deleted == 25:
                        print("[-] You Have Been Blocked, Try Litter.")
                        out()
                        sys.exit()
                    time.sleep(slp)
                except IndexError:
                    print("+" + "-" * 10 + "Delete" + "-" * 10 + "+")
                    print("[#] There Is No Message To Delete,")
                    print("+" + "-" * 10 + "DM-Cleaner" + "-" * 10 + "+")
                    print(f"[/] Successfully Delete [{successfully_deleted}]")
                    print(f"[/] Error Delete [{error_deleted}]")
                    print(f"[/] The Total [{All}]")
                    out()
                    sys.exit()


        clear()
    elif "The password you entered is incorrect. Please try again." in LOG.text:
        print(f"[-] Wrong Password @{user} ")
        out()
        sys.exit()
    elif LOG.text.find('two_factor_required') >= 0:
        print(f"[-] Your Account Have Two Factor. Closed  ")
        out()
        sys.exit()
    else:
        print(f"[-] We Have PP With Your Request. Try Liter..,")
        out()
        sys.exit()

#Bio 5
if num == '4':
    r = requests.session()
    user = input('username : ')
    pess = input('password : ')

    def edit():
        url = 'https://www.instagram.com/accounts/edit/'

        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar',
            'content-length': '122',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YM9ufAALAAHQzdHBBpIIyOJY34mz; ig_did=DAEA09BB-4988-4093-BA65-1798102D982C; ig_nrcb=1; csrftoken=JLyskFoxtmqVOpLQEzSDfHDUDPxmsmoS; ds_user_id=17623484687; sessionid=17623484687%3AXSFaL9DkqsGvDh%3A2; shbid=8454; shbts=1624206985.303834; rur=FRC',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/edit/',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
            'x-asbd-id': '437806',
            'x-csrftoken': 'JLyskFoxtmqVOpLQEzSDfHDUDPxmsmoS',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3jgeP7WYALtkf8mq2dOb3V9Amr-f4gSGPNHi-7i03KsTeF',
            'x-instagram-ajax': 'a90c0f3c9877',
            'x-requested-with': 'XMLHttpRequest',
            }

        data = {
            'first_name': ' ',
            'biography': ' ',
            'external_url': ' ',
            'chaining_enabled': ' ',
        }

        re = r.post(url, headers=headers, data=data).status_code

        if re == 200:
            print('Done For All ...')
        else:
            print('something error !')

    def login():
        user = input('username : ')
        pess = input('password : ')

        urLG = "https://www.instagram.com/accounts/login/ajax/"

        headLG = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '272',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; shbid=6144; shbts=1614374582.8963153',
            # 7lm
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/login/',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '790551e77c76',
            'x-requested-with': 'XMLHttpRequest'
        }

        datLG = {
            "username": user,
            "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{pess}",
            "queryParams": "{}",
            "optIntoOneTap": "false" }

        go = r.post(urLG, headers=headLG, data=datLG)
        res = go.text

        if ("userId") in res:
            print(f'Done login | Welcome {user}')
            edit()
        else:
            print('Error !')

    login()
#7lM < Hi

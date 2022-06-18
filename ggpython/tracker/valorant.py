# -*- coding: utf-8 -*-
# =============================================================================>
# ##############################################################################
# ## 
# ## tracker.py
# ## 
# ##############################################################################
# =============================================================================>
# Definition
VALORANT_TRACKER_WEBSITE = "https://tracker.gg/valorant/"
VALORANT_AGENT_ICONS = {
    "jett"      : "https://titles.trackercdn.com/valorant-api/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/displayicon.png",
    "kayo"      : "https://titles.trackercdn.com/valorant-api/agents/601dbbe7-43ce-be57-2a40-4abd24953621/displayicon.png",
    "fade"      : "https://titles.trackercdn.com/valorant-api/agents/dade69b4-4f5a-8528-247b-219e5a1facd6/displayicon.png",
    "brimstone" : "https://titles.trackercdn.com/valorant-api/agents/9f0d8ba9-4140-b941-57d3-a7ad57c6b417/displayicon.png",
    "viper"     : "https://titles.trackercdn.com/valorant-api/agents/707eab51-4836-f488-046a-cda6bf494859/displayicon.png",
    "omen"      : "https://titles.trackercdn.com/valorant-api/agents/8e253930-4c05-31dd-1b6c-968525494517/displayicon.png",
    "killjoy"   : "https://titles.trackercdn.com/valorant-api/agents/1e58de9c-4950-5125-93e9-a0aee9f98746/displayicon.png",
    "cypher"    : "https://titles.trackercdn.com/valorant-api/agents/117ed9e3-49f3-6512-3ccf-0cada7e3823b/displayicon.png",
    "sova"      : "https://titles.trackercdn.com/valorant-api/agents/320b2a48-4d9b-a075-30f1-1f93a9b638fa/displayicon.png",
    "sage"      : "https://titles.trackercdn.com/valorant-api/agents/569fdd95-4d10-43ab-ca70-79becc718b46/displayicon.png",
    "phoenix"   : "https://titles.trackercdn.com/valorant-api/agents/eb93336a-449b-9c1b-0a54-a891f7921d69/displayicon.png",
    "reyna"     : "https://titles.trackercdn.com/valorant-api/agents/a3bfb853-43b2-7238-a4f1-ad90e9e46bcc/displayicon.png",
    "raze"      : "https://titles.trackercdn.com/valorant-api/agents/f94c3b30-42be-e959-889c-5aa313dba261/displayicon.png",
    "breach"    : "https://titles.trackercdn.com/valorant-api/agents/5f8d3a7f-467b-97f3-062c-13acf203c006/displayicon.png",
    "skye"      : "https://titles.trackercdn.com/valorant-api/agents/6f2a04ca-43e0-be17-7f36-b3908627744d/displayicon.png",
    "yoru"      : "https://titles.trackercdn.com/valorant-api/agents/7f94d92c-4234-0a36-9646-3a87eb8b5c89/displayicon.png",
    "astra"     : "https://titles.trackercdn.com/valorant-api/agents/41fb69c1-4189-7b37-f117-bcaf1e96f1bf/displayicon.png",
    "chamber"   : "https://titles.trackercdn.com/valorant-api/agents/22697a3d-45bf-8dd7-4fec-84a9e28c69d7/displayicon.png",
    "neon"      : "https://titles.trackercdn.com/valorant-api/agents/bb2a4828-46eb-8cd1-e765-15848195d751/displayicon.png"
}

# =============================================================================> 
# imports default
import urllib.parse

# =============================================================================> 
# imports third party
from selenium.webdriver.common.by import By

# =============================================================================> 
# imports local
try:
    from .tracker import WebsiteAPI, TrackerWebsiteAPI
except Exception as _:
    from tracker import WebsiteAPI, TrackerWebsiteAPI

# =============================================================================> 
# define local metod

def dict_find_key(_dict, _value):
    key_list = list(_dict.keys())
    value_list = list(_dict.values())
    _pos = value_list.index(_value)
    return key_list[_pos]

# =============================================================================> 
# define class

class ValorantTrackerWebsiteAPI(TrackerWebsiteAPI):
    def __init__(self):
        """ __init__ """
        super().__init__()
        self._print_info("Initialize ValorantTrackerWebsiteAPI", mode = "p")
        self._print_info("", mode = "d")
    
    def __str__(self):
        """ __str__ """
        return "Valorant"
    
    # =========================================================================>
    # Class Method
    @classmethod
    def _get_match_result(cls, match_url) -> dict:
        """_get_match_result

        Args:
            match_url (str): match url
        Returns:
            {
                Agents, PartyNumber,
                Name, Name Tag, CurrentRank, 
                ACS, K, D, A, PM, KD, 
                ADR, HS, FK, FD, MK, Econ
            }
        ToDo:
            - get duels
        """
        _output = {}
        _api = WebsiteAPI
        _api.silence = True
        
        with _api() as match_driver:
            match_driver.get(match_url)
            
            match_driver.wait_element(2.0, element_by = By.CSS_SELECTOR, target_string = ".scoreboard__table:last-child")
            team_elements = match_driver.find_elements(By.CSS_SELECTOR, ".scoreboard__table tbody")

            # =================================================================>
            # .scoreboard__table tbodyを取得 <- チーム毎
            # tr を取得                      <- ユーザー毎
            # td を取得
            #     td0  キャラ img:src
            #          パーティ svg:class party--color-*
            #          ユーザー名 span.trn-ign__username:inner-html
            #          ユーザータグ span.trn-ign__discriminator:inner-html
            #     td1  ランク img:title
            #     td2- inner-html
            # =================================================================>
            user_list = []
            for team_number in range(len(team_elements)):
                team_members = team_elements[team_number].find_elements(By.TAG_NAME, "tr")
                for member_rank in range(len(team_members)):
                    # =========================================================>
                    member_status = team_members[member_rank].find_elements(By.TAG_NAME, "td")
                    _res = {}
                    # =========================================================>
                    _res["Team"] = team_number + 1
                    _res["TeamRank"] = member_rank + 1

                    # =========================================================>
                    # get agents
                    _tmp_agent = member_status[0].find_elements(By.TAG_NAME, "img")
                    if len(_tmp_agent) > 0:
                        _tmp_agent = dict_find_key(VALORANT_AGENT_ICONS, str(_tmp_agent[0].get_attribute("src")))
                        _res["Agents"] = _tmp_agent
                    else:
                        _res["Agents"] = "error"

                    # =========================================================>
                    # get party number
                    _tmp_party = member_status[0].find_elements(By.TAG_NAME, "svg")
                    if len(_tmp_party) > 0:
                        _tmp_party = int(str(_tmp_party[0].get_attribute("class"))[-1])
                        _res["PartyNumber"] = _tmp_party
                    else:
                        _res["PartyNumber"] = 0

                    # =========================================================>
                    # get name and name tag
                    _tmp_name = member_status[0].find_elements(By.CSS_SELECTOR, "span.trn-ign__username")
                    if len(_tmp_name) > 0:
                        _res["Name"] = str(_tmp_name[0].text)
                    else:
                        _res["Name"] = "error"
                    
                    _tmp_tag = member_status[0].find_elements(By.CSS_SELECTOR, "span.trn-ign__discriminator")
                    if len(_tmp_tag) > 0:
                        _res["NameTag"] = str(_tmp_tag[0].text)
                    else:
                        _res["NameTag"] = "error"
                    
                    # =========================================================>
                    # get rank
                    _tmp_rank = member_status[1].find_elements(By.TAG_NAME, "img")
                    if len(_tmp_rank) > 0:
                        _tmp_rank = _tmp_rank[0].get_attribute("title").split(" ")
                        if "Unrated" in _tmp_rank:
                            _res["CurrentRank"] = (_tmp_rank[0], 0)
                        else:
                            _res["CurrentRank"] = (_tmp_rank[0], _tmp_rank[1])
                    else:
                        _res["CurrentRank"] = ("error", 0)
                    
                    # =========================================================>
                    # others
                    _res["ACS"] = int(member_status[2].text)
                    _res["K"], _res["D"], _res["A"] = [int(i.text) for i in member_status[3:6]]
                    _res["PM"] = member_status[6].text
                    _res["KD"] = float(member_status[7].text)
                    _res["ADR"] = float(member_status[8].text)
                    _res["HS"] = float(str(member_status[9].text).replace("%", "")) / 100
                    _res["FK"], _res["FD"], _res["MK"], _res["Econ"] = [int(i.text) for i in member_status[10:]]

                    # =========================================================>
                    user_list.append(_res)
            
            _output["user"] = user_list

            # =================================================================>
            # マップ名 metadata__playlist-map
            # スコア team__value
            # 
            # =================================================================>
            map_name = match_driver.find_elements(By.CLASS_NAME, "metadata__playlist-map")
            if len(map_name) > 0:
                _output["map"] = str(map_name[0].text)
            else:
                _output["map"] = "error"
            
            # =================================================================>
            map_score = match_driver.find_elements(By.CSS_SELECTOR, ".metadata__score span.team__value")
            if len(map_score) > 1:
                _output["score"] = (int(map_score[0].text), int(map_score[1].text))
            else:
                _output["score"] = (0, 0)
        
        return _output
    
    # =========================================================================>
    # Utils override
    def get(self, user_name, user_tag, tracker = "matches", tracker_query = {}):
        """get

        Args:
            user_name (str) : valorant user name
            user_tag (str)  : valorant user name such as #(.*?)
            tracker (str, optional): target tracker url. Defaults to "matches".
            tracker_query (dict, optional): query string. Defaults to {}.
        """
        user_url = str(urllib.parse.quote(str(user_name))) + str(urllib.parse.quote(str(user_tag)))
        tracker_query_url = urllib.parse.urlencode(tracker_query)

        target_url = user_url + "/" + str(tracker) + "?" + tracker_query_url
        target_url = VALORANT_TRACKER_WEBSITE + "profile/riot/" + target_url # アップデートで使用不可になったら変更する
        super().get(target_url)
    
    def get_summary(self, user_name, user_tag, mode = "unrated", act = "all") -> dict:
        """get_summary
        Discription:
            get a game summary
        Return:
            dict : game summary
        """
        self._print_info("get summary", mode = "p")
        self._print_info("aready", mode = "d")
        self.get(user_name, user_tag, tracker = "overview", tracker_query = {"playlist" : mode, "season" : act})
        self.random_sleep()
        
        # start
        # self.wait_element(2.0, element_by = By.CSS_SELECTOR, target_string = ".scoreboard__table:last-child")

        _output = {}
        # =====================================================================>
        # get overview summary
        # > Play Time, Match Count, KAD, Win, Lose,
        self._print_info("_____ Overview", mode = "p")
        
        _output["PlayTime"] = self.find_element(By.CSS_SELECTOR, "div.segment-stats.area-main-stats span.playtime").text.split(" ")[0]
        _output["MatchCount"] = self.find_element(By.CSS_SELECTOR, "div.segment-stats.area-main-stats span.matches").text.split(" ")[0]
        _output["KAD"] = self.find_element(By.CSS_SELECTOR, "div.trn-profile-highlighted-content__stats div.stat span.stat__value").text
        _output["WinLose"] = [i.text for i in self.find_elements(By.CSS_SELECTOR, "div.trn-profile-highlighted-content__ratio g text")[:2]]
        
        # > Damage by round, KD, HSP
        for i in self.find_elements(By.CSS_SELECTOR, "div.giant-stats div.stat.align-left.giant.expandable"):
            _tmp = i.find_element(By.CSS_SELECTOR, "div.numbers")
            _output[_tmp.find_element(By.CSS_SELECTOR, "span.name").text] = _tmp.find_element(By.CSS_SELECTOR, "span.value").text

        # > Kills, Headshots, Death, Assists, Score by round, Kills by round, FB, Ace, Clutch, Flawless, Most kill
        for i in self.find_elements(By.CSS_SELECTOR, "div.main div.stat.align-left.giant.expandable"):
            _tmp = i.find_element(By.CSS_SELECTOR, "div.numbers")
            _output[_tmp.find_element(By.CSS_SELECTOR, "span.name").text] = _tmp.find_element(By.CSS_SELECTOR, "span.value").text
        
        self._print_info("", mode = "d")

        # =====================================================================>
        # get current ratings -> only competitive 
        # > Rating, Peak rating
        # get accuracy -> only all acts
        # > Head Count, Body Count, Leg Count
        # get weapons summary
        # > Weapon name
        # > > Head%, Body%, Leg%, Kills
        # get top maps summary
        # > Map name
        # > > Win, Lose
        for i in self.find_elements(By.CSS_SELECTOR, "div.area-sidebar div.card"):
            _title = i.find_element(By.CSS_SELECTOR, "div.title").text
            if _title == "Current Ratings":
                self._print_info("_____ CurrentRatings", mode = "p")
                
                _rating, _peak = [j for j in i.find_elements(By.CSS_SELECTOR, "div.rating-entry div.value")][:2] # Rating
                # Peak rating
                _rating_sub, _peak_sub = [j for j in i.find_elements(By.CSS_SELECTOR, "div.rating-entry div.subtext")][:2] # Rating
                
                _output["Rating"] = _rating + _rating_sub
                _output["PeakRating"] = _peak + _peak_sub
                
                self._print_info("", mode = "d")
            elif _title == "Accuracy":
                self._print_info("_____ CurrentRatings", mode = "p")
                
                _tmp = [j.text for j in i.find_elements(By.CSS_SELECTOR, "table.accuracy__stats td:nth-child(3) span.stat__value")]
                
                _output["Head"] = _tmp[0]
                _output["Body"] = _tmp[1]
                _output["Legs"] = _tmp[2]
                
                self._print_info("", mode = "d")
            elif _title == "Top Weapons":
                self._print_info("_____ Weapons", mode = "p")
                _tmp_weapon = []
                
                for j in i.find_elements(By.CSS_SELECTOR, "div.top-weapons__weapons div.weapon"):
                    _tmp = {}
                    
                    _tmp["Name"] = j.find_element(By.CSS_SELECTOR, "div.weapon__info div.weapon__name").text
                    _tmp["Type"] = j.find_element(By.CSS_SELECTOR, "div.weapon__info div.weapon__type").text
                    _tmp["Kill"] = j.find_element(By.CSS_SELECTOR, "div.weapon__main-stat span.value").text
                    for k, l in zip(["Head", "Body", "Legs"], j.find_elements(By.CSS_SELECTOR, "div.weapon__accuracy-hits span.stat")):
                        _tmp[k] = l.text
                    
                    _tmp_weapon.append(_tmp)
                
                _output["Weapon"] = _tmp_weapon
                self._print_info("", mode = "d")
            elif _title == "Top Maps":
                self._print_info("_____ Maps", mode = "p")
                _tmp_map = []

                for j in i.find_elements(By.CSS_SELECTOR, "div.top-maps__maps-map"):
                    _tmp = {}
                    
                    _tmp["Name"] = j.find_element(By.CSS_SELECTOR, "div.name").text
                    
                    _wl = j.find_element(By.CSS_SELECTOR, "div.info div.label").text.split(" ")
                    _tmp["Win"] = _wl[0][:-1]
                    _tmp["Lose"] = _wl[2][:-1]
                    
                    _tmp_map.append(_tmp)
                
                _output["Map"] = _tmp_map
                self._print_info("", mode = "d")
        
        # =====================================================================>
        # get top agents summary
        # > Agent name
        # > > Time Played, Matches, Win%, KD, ADR, ACS, HS%
        self._print_info("_____ TopAgents", mode = "p")

        _top_agents_head = [i.text for i in self.find_elements(By.CSS_SELECTOR, "div.st-header div.st-header__item span.label")]
        _top_agents = []
        for i in self.find_elements(By.CSS_SELECTOR, "div.top-agents div.st-content"):
            for j in i.find_elements(By.CSS_SELECTOR,"div.st-content__item"):
                _tmp = {}
                for k, l in zip(_top_agents_head, j.find_elements(By.CSS_SELECTOR,"div.st__item")):
                    _tmp[k] = [m.text for m in l.find_elements(By.CSS_SELECTOR, "div.info div.value, div.small")]
                _top_agents.append(_tmp)
        
        _output["Agent"] = _top_agents

        self._print_info("", mode = "d")
        
        # =====================================================================>
        # get last 20 match summary **未実装**
        # > Win, Lose, KD, ADR
        # > Agent name
        # > > Win, Lose, KD

        self._print_info("_____ **its all of summary**", mode = "p")
        self._print_info("", mode = "d")
        return _output
    
    def get_match_summary(self, user_name, user_tag, mode = "unrated", act = "all") -> dict:
        """get_match_summary
        Args:
            user_name (str) : valorant user name
            user_tag (str)  : valorant user name such as #(.*?)
            mode (str, optional): match playlist. Defaults to "unrated". "unrated"|"competitive"|"spikerush"|"snowball"|"replication"|"deathmatch"
        """
        self._print_info("get match summary", mode = "p")
        self.get(user_name, user_tag, tracker = "overview", tracker_query = {"playlist" : mode, "season" : act})
        self._print_info("", mode = "d")
        return {}
    
    def get_pc_summary(self, user_name, user_tag, mode = "unrated", act = "all") -> list:
        """get_pc_summary
        Args:
            user_name (str) : valorant user name
            user_tag (str)  : valorant user name such as #(.*?)
            mode (str, optional): match playlist. Defaults to "unrated". "unrated"|"competitive"|"spikerush"|"snowball"|"replication"|"deathmatch"
        """
        self._print_info("get pc summary", mode = "p")
        
        self.get(user_name, user_tag, tracker = "overview", tracker_query = {"playlist" : mode, "season" : act})
        self.random_sleep()

        # =====================================================================>
        # get top agents summary
        # > Agent name
        # > > Time Played, Matches, Win%, KD, ADR, ACS, HS%

        _top_agents_head = [i.text for i in self.find_elements(By.CSS_SELECTOR, "div.st-header div.st-header__item span.label")]
        _top_agents = []
        
        for i in self.find_elements(By.CSS_SELECTOR, "div.top-agents div.st-content"):
            for j in i.find_elements(By.CSS_SELECTOR,"div.st-content__item"):
                _tmp = {}
                for k, l in zip(_top_agents_head, j.find_elements(By.CSS_SELECTOR,"div.st__item")):
                    _tmp[k] = [m.text for m in l.find_elements(By.CSS_SELECTOR, "div.info div.value, div.small")]
                _top_agents.append(_tmp)
        
        self._print_info("", mode = "d")
        return _top_agents

    def get_match_url_list(self, user_name, user_tag, n_match = None, mode = "unrated", act = "all") -> list:
        """get_match_url_list

        Args:
            user_name (str) : valorant user name
            user_tag (str)  : valorant user name such as #(.*?)
            n_match (int)   : number of match count. Defaults to None.
            mode (str, optional): match playlist. Defaults to "unrated".
                "unrated"|"competitive"|"spikerush"|"snowball"|"replication"|"deathmatch"
        Returns:
            list : url
        """
        self._print_info("get match url list", mode = "p")
        # アクセス
        self.get(user_name, user_tag, tracker_query = {"playlist" : mode, "season" : act})
        
        # リスト取得
        self.wait_element(2.0, element_by = By.CSS_SELECTOR, target_string = ".match:last-child")
        elements = self.find_elements(By.CLASS_NAME, "match")

        
        if n_match is None:
            n_match = len(elements)
        elif n_match > len(elements):
            n_match = len(elements)
        
        match_url_list = []
        for i in range(n_match):
            a_tag = elements[i].find_elements_by_css_selector("a")
            if len(a_tag) > 0:
                match_url_list.append(a_tag[0].get_attribute("href"))

        self._print_info("", mode = "d")
        return match_url_list
    
    def get_match_result(self, user_name, user_tag, n_match = None, mode = "unrated", act = "all") -> list:
        """get_match_result

        Args:
            user_name (str) : valorant user name
            user_tag (str)  : valorant user name such as #(.*?)
            n_match (int)   : number of match count. Defaults to None.
            mode (str, optional): match playlist. Defaults to "unrated".
                "unrated"|"competitive"|"spikerush"|"snowball"|"replication"|"deathmatch"
        Returns:
            dict: result
        """
        self._print_info("get match result", mode = "p")
        _silence = self.silence
        self.silence = True

        match_url_list = self.get_match_url_list(user_name, user_tag, n_match = n_match, mode = mode, act = act)

        _output = []
        for i in match_url_list:
            _output.append(self._get_match_result(i))
        
        if not _silence:
            self.silence = False
        self._print_info("", mode = "d")
        return _output

    def get_pc_url_list(self, user_name, user_tag, mode = "unrated", act = "all") -> list: # unnecessary method !!!
        """ get_pc_url_list """
        self._print_info("This is not working in valorant", mode = "e")
        return []
    
    def get_pc_result(self, user_name, user_tag, mode = "unrated", act = "all") -> list:
        """get_pc_result
        Args:
            user_name (str) : valorant user name
            user_tag (str)  : valorant user name such as #(.*?)
            mode (str, optional): match playlist. Defaults to "unrated". "unrated"|"competitive"|"spikerush"|"snowball"|"replication"|"deathmatch"
        """
        self._print_info("get pc result", mode = "p")
        self._print_info("This is `coming soon` method", mode = "w")
        self._print_info("", mode = "d")
        return {}

    # =========================================================================>
    # Utils valorant original
    def get_map_result(self, user_name, user_tag, mode = "unrated", act = "all") -> dict:
        """get_map_result
        Args:
            user_name (str) : valorant user name
            user_tag (str)  : valorant user name such as #(.*?)
            mode (str, optional): match playlist. Defaults to "unrated". "unrated"|"competitive"|"spikerush"|"snowball"|"replication"|"deathmatch"
        """
        self._print_info("get map result", mode = "p")
        self._print_info("This is `coming soon` method", mode = "w")
        self._print_info("", mode = "d")
        return {}
    
    def get_weapon_result(self, user_name, user_tag, mode = "unrated", act = "all") -> dict:
        """get_weapon_result
        Args:
            user_name (str) : valorant user name
            user_tag (str)  : valorant user name such as #(.*?)
            mode (str, optional): match playlist. Defaults to "unrated". "unrated"|"competitive"|"spikerush"|"snowball"|"replication"|"deathmatch"
        """
        self._print_info("get weapon result", mode = "p")
        self._print_info("This is `coming soon` method", mode = "w")
        self._print_info("", mode = "d")
        return {}
    
    def get_award_result(self, user_name, user_tag) -> dict:
        """get_award_result
        Args:
            user_name (str) : valorant user name
            user_tag (str)  : valorant user name such as #(.*?)
        """
        self._print_info("get award result", mode = "p")
        self._print_info("This is `coming soon` method", mode = "w")
        self._print_info("", mode = "d")
        return {}
    
    def get_custom_url_list(self, user_name, user_tag, n_match = None) -> list:
        """get_custom_url_list
        Args:
            user_name (str) : valorant user name
            user_tag (str)  : valorant user name such as #(.*?)
            n_match (int)   : number of match count. Defaults to None.
        """
        self._print_info("get custom url list", mode = "p")
        self._print_info("This is `coming soon` method", mode = "w")
        self._print_info("", mode = "d")
        return []
    
    def get_custom_result(self, user_name, user_tag, n_match = None) -> dict:
        """get_custom_result
        Args:
            user_name (str) : valorant user name
            user_tag (str)  : valorant user name such as #(.*?)
            n_match (int)   : number of match count. Defaults to None.
        """
        self._print_info("get custom result", mode = "p")
        self._print_info("This is `coming soon` method", mode = "w")
        self._print_info("", mode = "d")
        return {}

# =============================================================================> 

if __name__ == "__main__":
    pass

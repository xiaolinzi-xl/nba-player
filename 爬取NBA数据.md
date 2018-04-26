
1. 爬取球员薪资

网站：https://nba.hupu.com/players

数据爬取：

players = response.css('table.players_table tbody tr')

players[1].css('td.left b::text').extract()

re.findall('.*?(\d+万).*',mon)[0]

2.爬取球队信息

球队id: http://stats.nba.com/js/data/widgets/teams_landing_sidebar.json

名字，城市

球员基本数据：http://stats.nba.com/stats/commonteamroster?LeagueID=00&Season=2017-18&TeamID=1610612739

名字，位置，身高，体重，生日，player_id，team_id

身高：英尺 英寸 1英尺 = 12英寸 1英寸 = 2.54厘米

体重：磅 1磅 = 0.4535924千克

球员详情页：http://stats.nba.com/player/{player_id}/

球员赛季的数据：http://stats.nba.com/stats/playerdashboardbyyearoveryear?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=201567&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&Split=yoy&VsConference=&VsDivision=


球员图片地址：https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/1610612742/2017/260x190/202083.png

https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/{team_id}/2017/260x190/{player_id}.png

2. 录入数据库

转换身高，体重，生日（转换为字符串即可）

计算评分：

得分：PTS 29 1

助攻：AST 22 2

前场篮板：OREB 19 1

后场篮板：DREB 20 1

抢断：STL 24 2 

封盖：BLK 25 1.8

失误：TOV 23 -1

投篮命中：FGM 10 0.4

投丢：FGA-FGM 11-10 -1

三分球命中： FG3M 13 0.5


赛季数据：

赛季时间，time

所属球队

出场：GP

时间：MIN

得分：PTS

篮板：REB

助攻：AST

抢断：STL

盖帽：BLK

失误：TOV

投篮%：FG% 12

三分%：FG3_PCT 15

罚球%：FT_PCT

eFG% 20

TS% 21

ORtg 10

DRtg 11

虎扑网站：

https://nba.hupu.com/stats/players/pts/6



投篮热图：

https://games.mobileapi.hupu.com/1/7.1.18/nba/playerPage?client=861945035683907&player_id=650&night=0&entrance=1


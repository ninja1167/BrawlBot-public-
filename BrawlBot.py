import os
my_secret = os.environ['TOKEN']
import discord
import random
import json
from discord.ext import commands
rankvar = 1


intents = discord.Intents.default()
intents.members = True

clonebot = False

if clonebot == True:
    cpfx = "."
elif clonebot == False:
    cpfx = "-"

client = commands.Bot(command_prefix=cpfx, intents=intents)

if clonebot == False:
    searchChannel = 929231150386409512
    miscChannel = 928465831422230531
    modChannel = 928465831422230531
    matchChannel = 929231150386409512
    
elif clonebot == True:
    searchChannel = 929231150386409512
    miscChannel = 928465831422230531
    modChannel = 928465831422230531
    matchChannel = 929231150386409512
   
  
    

channelList = [searchChannel, miscChannel, modChannel, matchChannel]

join = '🔔'
leave = '🚪'
modkey = '🔑'
stay = '☑'
challenge = '⚔'
abort = '🔴'
accept = '✅'
cancel = '❌'
versus = '<:VS:928851360718393384>'
BF = '<:Battlefield:928753478329831424>'
FD = '<:FinalDestination:928755520385470524>'
DL = '<:DL64:928756262601105458>'
YS = '<:YS:928755786090434590>'
FOD = '<:Fod:928756482877567047>'
PS = '<:PS1:928755950251307118>'
CS = '<:CastleSiege:925957337867485284>'
FO = '<:FrigateOrpheon:925957063383867483>'

completestagelist = [BF, PS, DL, YS, FOD, FD]
netpColor = 4312575  # light blue
wifiColor = 16613797  # light pink
defaultColor = 15174967  # orange
netpSymbol = '<:netplay:928849825250824282>'
wifiSymbol = '<:netplay:928849825250824282>'
boardType = "NETP"
attributes = {"WIFI": {'symbol': wifiSymbol, 'color': wifiColor}, "NETP": {'symbol': netpSymbol, 'color': netpColor}}

stageTNs = {
    '<:Battlefield:928753478329831424>': 'https://cdn.discordapp.com/emojis/928753478329831424.webp?size=160&quality=lossless',
    '<:FinalDestination:928755520385470524>': 'https://cdn.discordapp.com/emojis/928755520385470524.webp?size=160&quality=lossless',
    '<:DL64:928756262601105458>': 'https://cdn.discordapp.com/emojis/928756262601105458.webp?size=160&quality=lossless',
    '<:YS:928755786090434590>': 'https://cdn.discordapp.com/emojis/928755786090434590.webp?size=160&quality=lossless',
    '<:Fod:928756482877567047>': 'https://cdn.discordapp.com/emojis/928756482877567047.webp?size=160&quality=lossless',
    '<:PS1:928755950251307118>': 'https://cdn.discordapp.com/attachments/845292400440377374/861081446424510474/PS1_Preview.png',
}



brawlChara = {"mario": '<:Mario:936378975511519274>', "donkey kong": '<:DK:938447276509134959>',
              "dk": '<:DK:938447276509134959>',
              "link": '<:Link:856660418201780244>', "samus": '<:Samus:856660473994805298>',
              "kirby": '<:Kirby:861785546677288973>', "fox": '<:Fox:856660399764144129>',
              "pikachu": '<:Pika:936378588008161350>', "marth": '<:Marth:856660427713806337>',
              "mr. game & watch": '<:GW:938447276450394112>',
              "mr.game & watch": '<:GW:938447276450394112>',
              "mr.g&w": '<:GW:938447276450394112>',
              "mr game and watch": '<:GW:938447276450394112>',
              "game n watch": '<:GW:938447276450394112>',
              "mr game n watch": '<:GW:938447276450394112>',
              "gnw": '<:GW:938447276450394112>', "mr gnw": '<:GW:938447276450394112>',
              "gandw": '<:GW:938447276450394112>',
              "mr game & watch": '<:GW:938447276450394112>',
              "game & watch": '<:GW:938447276450394112>',
              "gw": '<:GW:938447276450394112>', "mr.game and watch": '<:GW:938447276450394112>',
              "g&w": '<:GW:938447276450394112>', "luigi": '<:Luigi:881604508424216636>',
              "roy": '<:Roy:856660461130874930>', "green mario": '<:Luigi:881604508424216636>',
              "weeg": '<:Luigi:881604508424216636>',
              "zelda": '<:Zelda:856660494269022229>',
              "sheik": '<:Sheik:856660483474325505>', "mewtwo": '<:Mewtwo:938447276601380894>',
              "mew2": '<:Mewtwo:938447276601380894>',
              "pichu": '<:Pichu:856660483474325505>', "young link": '<:Ylink:936379092922687498>',
              "falco": '<:Falco:856660378682654740>', "ylink": '<:Ylink:936379092922687498>',
              "yink": '<:Ylink:936379092922687498>',"yl": '<:Ylink:936379092922687498>',
              "worse fox": '<:Falco:856660378682654740>',
              "daisy": '<:Peach:856660438291578900>',
              "peach": '<:Peach:856660438291578900>', "yoshi": '<:Yoshi:936379260019556432>',
              "ganondorf": '<:Ganon:856660407828742155>', "ganon": '<:Ganon:856660407828742155>',
              "ice climbers": '<:Icies:888612645387796551>',
              "ics": '<:Icies:888612645387796551>', "ic": '<:Icies:888612645387796551>',
              "icies": '<:Icies:888612645387796551>', 
              "ness": '<:Ness:938447276416851988>', 
              "bowser": '<:Bowser:938447276370714694>', 
               "captain falcon": '<:Falcon:856660388753309696>',
              "cf": '<:Falcon:856660388753309696>',
              "falcon": '<:Falcon:856660388753309696>', "jigglypuff": '<:Puff:856660446810341377>',
              "puff": '<:Puff:856660446810341377>', "doc": '<:Doc:856660362207166534>', "doctor mario": '<:Doc:856660362207166534>',
              }

characterlist = ['<:Mario:936378975511519274>', '<:DK:938447276509134959>', '<:Link:856660418201780244>',
                 '<:Samus:856660473994805298>', '<:Roy:856660461130874930>',
                 '<:Kirby:861785546677288973>', '<:Fox:856660399764144129>', 
                 '<:Pika:936378588008161350>', '<:Marth:856660427713806337>', '<:GW:938447276450394112>',
                 '<:Luigi:881604508424216636>', '<:Mewtwo:938447276601380894>', '<:Zelda:856660494269022229>',
                 '<:Sheik:856660483474325505>', '<:Pichu:856660483474325505>', '<:Falco:856660378682654740>',
                 '<:Peach:856660438291578900>', '<:Yoshi:936379260019556432>',
                 '<:Ganon:856660407828742155>', '<:Icies:888612645387796551>',
                 '<:Ylink:936379092922687498>',
                 '<:Ness:938447276416851988>',
                 '<:Bowser:938447276370714694>', 
                 '<:Falcon:856660388753309696>', '<:Puff:856660446810341377>', '<:Doc:856660362207166534>'
                ]

opponents = {}
players2matches = {}
matches = {}
searching = {"NETP": {"bo3": [], "bo5": [], "bo7": []}, "WIFI": {"bo3": [], "bo5": [], "bo7": []}}
searchMessages = {}
challengeMessages = {}

banned = []
with open("banlistsave.json") as f:
    loadbanned = json.load(f)
    fixbanned = []
    for userID in loadbanned:
        fixbanned.append(int(userID))
    banned = fixbanned
    # print(banned)

preranked = {"NETP": {}, "WIFI": {}}
with open("prerankingsave.json") as f:
    loadprerankings = json.load(f)
    fixedprerankingsN = {int(key): value for key, value in loadprerankings["NETP"].items()}
    fixedprerankingsW = {int(key): value for key, value in loadprerankings["WIFI"].items()}
    preranked["NETP"] = fixedprerankingsN
    preranked["WIFI"] = fixedprerankingsW

rankings = {"NETP": {}, "WIFI": {}}
with open("rankingsave.json") as f:
    loadRankings = json.load(f)
    fixedRankingsN = {int(key): value for key, value in loadRankings["NETP"].items()}
    fixedRankingsW = {int(key): value for key, value in loadRankings["WIFI"].items()}
    rankings["NETP"] = fixedRankingsN
    rankings["WIFI"] = fixedRankingsW
# print(rankings)

sdplayers = {}
sdgames = {}

searchIcons = [abort, challenge]
searchSelection = [accept, cancel]
winloss = ["<:win:936376084348424232>", "<:lose:936375892194758706>"]
win = "<:win:936376084348424232>"
loss = "<:lose:936375892194758706>"
emotes2stage = {'<:Battlefield:928753478329831424>': "Battlefield",
                '<:FinalDestination:928755520385470524>': "Final Destination",
                '<:DL64:928756262601105458>': "Dream Land",
                '<:YS:928755786090434590>': "Yoshi's Story",
                '<:Fod:928756482877567047>': "Fountain of Dreams",
                '<:PS1:928755950251307118>': "Pokemon Stadium",
                }
stage2emotes = {'<:Battlefield:928753478329831424>': BF,
                '<:FinalDestination:928755520385470524>': FD,
                '<:DL64:928756262601105458>': DL,
                '<:YS:928755786090434590>': YS,
                '<:Fod:928756482877567047>': FOD,
                '<:PS1:928755950251307118>': PS,
                }

startersize = 5
if startersize == 3:
    starters = ['<:Battlefield:928753478329831424>', '<:FinalDestination:928755520385470524>',
                '<:DL64:928756262601105458>']
    counterpicks = []
    stages = [BF, FD, DL]

elif startersize == 5:
    starters = ['<:Battlefield:928753478329831424>', '<:PS1:928755950251307118>',
                '<:DL64:928756262601105458>', '<:YS:928755786090434590>',
                '<:Fod:928756482877567047>']
    counterpicks = ['<:FinalDestination:928755520385470524>']
    stages = [BF, PS, DL, YS, FOD]
fullstagelist = starters + counterpicks
dsl = True

sets = ["bo3", "bo5"]

def showstagelist(stages):
    text = ""
    for icon in stages:
        text += f"{icon} {emotes2stage[icon]}\n"
    return text


def remainingstagelist(fullstagelist, dsl):
    remainingstages = fullstagelist[:]
    for stage in dsl:
        remainingstages.remove(stage)
    return remainingstages


def sdscoreUpdate(title, username, userID, score, selecting):
    if title == True:
        return username

    elif title == False:
        details = f"Wins: {score} 🏆\n\n"
        if selecting == True:
            details += f"waiting for <@{userID}>\nto pick their character...\n(type it in this chat)"

        return details


def scrambled(inputlist):
    newlist = inputlist
    random.shuffle(newlist)
    return newlist


def randomroster():
    randomlist = scrambled(characterlist)
    randRoster = ""
    newLineCounter = 0
    for character in randomlist:
        randRoster += f"{character}ㅤ"
        newLineCounter += 1
        if newLineCounter == 10:
            randRoster += "\n\n"
            newLineCounter = 0
    return randRoster


def showroster(inputlist, fullroster):
    rostersize = len(inputlist)
    displayRoster = f"Remaining Roster ({rostersize}):\n\n"
    newLineCounter = 0
    for character in fullroster:
        if character in inputlist:
            displayRoster += f"{character}ㅤ"
        else:
            displayRoster += f"<:4Falco:919693719068897320>ㅤ"
            # <:blank:876316169995431958>
        newLineCounter += 1
        if newLineCounter == 10:
            displayRoster += "\n\n"
            newLineCounter = 0
    displayRoster += "\nㅤ"
    return displayRoster


def showused(username, roster):
    displayRoster = f"{username}\n"
    newLineCounter = 0

    for character in roster:
        displayRoster += f"{character}ㅤ"
        newLineCounter += 1
        if newLineCounter == 10:
            displayRoster += "\n\n"
            newLineCounter = 0
    displayRoster += "\nㅤ"
    return displayRoster


def banCheck(userID):
    if userID in banned:
        return True
    else:
        return False


def saveBanList(banlist):
    with open("banlistsave.json", "w") as f:
        json.dump(banlist, f)


def saveRankings(dictionary):
    with open("rankingsave.json", "w") as f:
        json.dump(dictionary, f)


def savePreRanked(dictionary):
    with open("prerankingsave.json", "w") as f:
        json.dump(dictionary, f)


def ELOCapCheck(playerID, matchType):
    if rankings[matchType][playerID] < 1:
        rankings[matchType][playerID] = 1
    elif rankings[matchType][playerID] > 9999:
        rankings[matchType][playerID] == 9999


def showELOChange(newELO, oldELO):
    sign = "+"
    if newELO < oldELO:
        sign = "-"
    changeValue = str(round(abs(newELO - oldELO)))
    showChange = sign + changeValue
    return showChange


def editPreranked(playerID, matchType):
    if playerID in preranked[matchType].keys():
        preranked[matchType][playerID] -= 1
        if preranked[matchType][playerID] == 0:
            preranked[matchType].pop(playerID)
        savePreRanked(preranked)


def displayELO(playerID, matchType):
    elo = rankings[matchType][playerID]
    questionmark = ""
    if playerID in preranked[matchType].keys():
        questionmark = "(?)"
    showELO = str(round(elo)) + questionmark
    return showELO


def findPlayer(LBType, standing):
    rankingList = rankings[LBType]
    strRankingList = {str(key): value for key, value in rankingList.items()}
    sortedRankingList = dict(sorted(strRankingList.items(), key=lambda x: x[1], reverse=True))
    playerList = list(sortedRankingList.keys())
    playerID = standing
    strPreranked = {str(key): value for key, value in preranked[LBType].items()}
    prerankedList = list(strPreranked.keys())
    for player in prerankedList:
        playerList.remove(player)
    if playerID > len(playerList):
        playerID = 0
    else:
        playerID = int(playerList[standing - 1])
    return playerID


def buildLBoard(rankingList, listType, page, matchType):
    strRankingList = {str(key): value for key, value in rankingList.items()}
    sortedRankingList = dict(sorted(strRankingList.items(), key=lambda x: x[1], reverse=True))
    playerList = list(sortedRankingList.keys())
    strPreranked = {str(key): value for key, value in preranked[matchType].items()}
    prerankedList = list(strPreranked.keys())
    for player in prerankedList:
        playerList.remove(player)
    LBContent = "```\n"

    part = 10
    max = part * page

    # if there is no one in the leaderboard
    if len(playerList) == 0:
        LBContent += "No players made it to the leaderboard yet..."
        max = len(playerList)
        begin = len(playerList)
        part = len(playerList)

    # if there are less than 10 players in the leaderboard
    elif max > len(playerList) and len(playerList) < 10:
        max = len(playerList)
        begin = len(playerList)
        part = len(playerList)
    # else if there are fewer players than what the user requests to see
    elif max > len(playerList):
        max = len(playerList)
        begin = 10
    # otherwise the leaderboard is created normally
    else:
        max = 10 * page
        begin = 10

    startindex = max - begin
    # print("start index: ", startindex)
    for index in range(part):
        # ("index:", index)
        # print("current index:", startindex + index)
        strPlayerID = playerList[startindex + index]
        intPlayerID = int(strPlayerID)
        playerName = client.get_user(intPlayerID)
        if playerName == None:
            playerName = f"UserID: {strPlayerID}"
        ELO = round(rankings[listType][intPlayerID])
        standing = startindex + index + 1
        player_block = f"{standing}) {playerName}".ljust(41)  # max name length is 32 + room for the #) part
        elo_block = f"[{ELO}]".rjust(6)  # ensure its spaced right
        LBContent += f"{player_block} {elo_block}\n\n"
    return LBContent + "```"


def getPlacement(rankingList, playerID, matchType):
    strPlayerID = str(playerID)
    strRankingList = {str(key): value for key, value in rankingList.items()}
    # print("strRankingList: ", strRankingList)
    sortedRankingList = dict(sorted(strRankingList.items(), key=lambda x: x[1], reverse=True))
    # print("sortedRankingList: ", sortedRankingList)
    playerList = list(sortedRankingList.keys())
    # print("playersList:", playerList)

    strPreranked = {str(key): value for key, value in preranked[matchType].items()}
    prerankedList = list(strPreranked.keys())
    for player in prerankedList:
        playerList.remove(player)

    standing = playerList.index(strPlayerID) + 1
    numOfPlayers = len(playerList)
    return standing, numOfPlayers


def forgetSearch(messageID):
    for messID in searchMessages[messageID]["challenges"]:
        challengeMessages.pop(messID)
    setType = searchMessages[messageID]["setType"]
    matchType = searchMessages[messageID]["matchType"]
    player = searchMessages[messageID]["player"]
    searching[matchType][setType].remove(player)
    searchMessages.pop(messageID)


def forgetMatch(messageID):
    for messID in matches[messageID]["players"].keys():
        opponents.pop(messID)
        players2matches.pop(messID)
    matches.pop(messageID)


def forgetSD(messageID):
    for playerID in sdgames[messageID]["playerlist"]:
        sdplayers.pop(playerID)
    sdgames.pop(messageID)


def forgetMessage(messageID):
    # if the message is a match window
    if messageID in matches.keys():
        forgetMatch(messageID)
    # if the message is a search message
    elif messageID in searchMessages.keys():
        forgetSearch(messageID)
    # if the message is for smashdown
    elif messageID in sdgames.keys():
        forgetSD(messageID)


def addPlayer(player, matchType):
    '''
    adds players to the ranking system
    :param player_id:
    :return:
    '''
    rankings[matchType][player] = 1500
    preranked[matchType][player] = 3
    saveRankings(rankings)
    savePreRanked(preranked)


def calculateELO(winnerID, loserID, matchType, endCheck, modCheck, wNeeded):
    '''
    Calculates new elos for 2 players after a given game
    :param winnerID:
    winner's rating
    :param loserID:
    losers rating
    :param gameCount
    game count of the set
    :return:
    returns reward points
    '''
    endMultiplier = 1
    if endCheck == True:
        if wNeeded == 2:
            endMultiplier = 0.85
        elif wNeeded == 3:
            endMultiplier = 0.7
        elif wNeeded == 4:
            endMultiplier = 0.6

    elif modCheck == True:
        endMultiplier = 0.5
    winnerRating = rankings[matchType][winnerID]
    loserRating = rankings[matchType][loserID]
    setMultiplier = 1
    wMultiplier = 1
    lMultiplier = 1
    if winnerID in preranked[matchType].keys():
        wMultiplier = 1.5
    if loserID in preranked[matchType].keys():
        lMultiplier = 1.5

    # calculates the likely-hood of the result not occurring
    score = 1 - (1 / (1 + 10 ** ((loserRating - winnerRating) / 400)))
    multiplier = 18

    if endCheck == True or modCheck == True:
        wRewardPoints = round(multiplier * score * wMultiplier * endMultiplier)
        lRewardPoints = round(multiplier * score * lMultiplier * endMultiplier)

    elif endCheck == False:
        wRewardPoints = round(multiplier * score * wMultiplier * endMultiplier, 2)
        lRewardPoints = round(multiplier * score * lMultiplier * endMultiplier, 2)

    rankings[matchType][winnerID] += wRewardPoints
    rankings[matchType][loserID] -= lRewardPoints
    rankings[matchType][winnerID] = round(rankings[matchType][winnerID])
    rankings[matchType][loserID] = round(rankings[matchType][loserID])

    ELOCapCheck(winnerID, matchType)
    ELOCapCheck(loserID, matchType)

    saveRankings(rankings)

    newWinnerELO = rankings[matchType][winnerID]
    newLoserELO = rankings[matchType][loserID]
    # print("updated winner elo: ", newWinnerELO)
    # print("updated loser elo: ", newLoserELO)

    return newWinnerELO, newLoserELO


def createCharaList():
    charaList = "Here's a list of all the character inputs I can recognize:\n"
    charaList += "```"
    charaInputs = list(brawlChara.keys())
    sortedCharaInputs = sorted(charaInputs)
    for input in sortedCharaInputs:
        charaEmote = brawlChara[input]
        charaList += f"{input}\n"
    charaList += "```"
    return charaList


@client.event
async def on_ready():
    helpactivity = discord.Activity(name="-helpme", type=1)
    await client.change_presence(activity=helpactivity)
    print("Bot is ready")
    print(client.user.id)


@client.command()
async def helpme(ctx):
    # fetch change
    user = client.get_user(ctx.message.author.id)
    dm = await user.create_dm()
    await dm.send(f"**command prefix: ``-``**\n"
                  f"(begin every command with ``-`` in order for BrawlBot to recognize your command.)\n"
                  f"\n"
                  f"**__Set Type__\n"
                  f"> This command begins a search queue for a ranked set. (Only usable in <#{searchChannel}>)\n"
                  f"> Set Type = ``bo3`` (best of 3) or ``bo5`` (best of 5)\n"
                  f"> \n"
                  f"> examples:\n"
                  f"> ``-bo3``\n"
                  f"**__rank__**\n"
                  f"> This command allows you to view your own rank and standing in all ladders you're participating in. (Only usable in <#{miscChannel}>)\n"
                  f"> \n"
                  f"> You can look up another player's ranking info by @'ing them after the command.\n"
                  f"> \n"
                  f"> example: ``-rank @APR Financing``\n"
                  f"> \n"
                  f"> You can also look up a specific player based on standing within a specific ladder.\n"
                  f"> \n"
                  f"> exmaples:\n"
                  f"> ``-rank  3`` (retrieves the player who is top 3 in the netplay ladder)\n"
                  f"> ``-rank  5`` (retrieves the player who is top 5 in the netplay ladder)\n"
                  f"**__top__**  ``(Page Number)``\n"
                  f"> Displays a leaderboard of the top 10 players for the specified ladder type. (Only usable in <#{miscChannel}>)\n"
                  f"> Page Number = input a number to view a specific page of the leaderboard.\n"
                  f"> If no number is given, default page will be 1.\n"
                  f"> \n"
                  f"> examples:\n"
                  f"> ``-top `` (Shows the top 1-10 players in the netplay ladder)\n"
                  f"> ``-top 2`` (Shows the top 11-20 players in the netplay ladder)\n"
                  f"> ``-top 3`` (Shows the top 21-30 players in the netplay ladder)\n"
                  f"**__characters__**\n"
                  f"> This command sends a DM with a list containing all character inputs BrawlBot can recognize.\n"
                  f"> This is only relevant during character selections when in a ranked match.\n"
                  f"**__ironman__**\n"
                  f"> This command will send you a randomized brawl roster.\n"
                  f"> (usable in the freeplay channels)\n"
                  f"**__smashdown__**\n"
                  f"> This command sets up a smashdown card to help keep track of characters and score.\n"
                  f"> (usable in the freeplay channels)"
                  f"> Smashdown will not work. \n")
    await ctx.send("I sent you a DM with a list of my commands.")


@client.command()
async def smashdown(ctx):
    userID = ctx.message.author.id
    if userID in sdplayers.keys():
        await ctx.message.delete()
        await ctx.send("You already have a smashdown room up...", delete_after=6)
        return

    username = ctx.message.author
    userpfp = ctx.message.author.avatar_url
    embed = discord.Embed(
        title=f"Smashdown!",
        color=defaultColor,
        description=f"Click {join} to play with {username}"
    )
    embed.set_footer(text=f"Click on {leave} to end game.")
    embed.set_thumbnail(url=userpfp)
    await ctx.send("(This smashdown card will be auto deleted after 8 hours.)")
    smashdowngame = await ctx.send(embed=embed, delete_after=28800)
    await smashdowngame.add_reaction(leave)
    await smashdowngame.add_reaction(join)

    gameID = smashdowngame.id

    sdgames[gameID] = {
        "players": {userID: {"character": "n/a", "wins": 0, "selecting": False, "usedCharacters": [], "field": 0}},
        "playerlist": [userID],
        "winner": "n/a",
        "loser": "n/a",
        "messageObj": smashdowngame,
        "winsNeeded": 10,
        "remaining": ['<:Mario:936378975511519274>', '<:DK:938447276509134959>', '<:Link:856660418201780244>',
                 '<:Samus:856660473994805298>', '<:Roy:856660461130874930>',
                 '<:Kirby:861785546677288973>', '<:Fox:856660399764144129>', 
                 '<:Pika:936378588008161350>', '<:Marth:856660427713806337>', '<:GW:938447276450394112>',
                 '<:Luigi:881604508424216636>', '<:Mewtwo:938447276601380894>', '<:Zelda:856660494269022229>',
                 '<:Sheik:856660483474325505>', '<:Pichu:856660483474325505>', '<:Falco:856660378682654740>',
                 '<:Peach:856660438291578900>', '<:Yoshi:936379260019556432>',
                 '<:Ganon:856660407828742155>', '<:Icies:888612645387796551>',
                 '<:Ylink:936379092922687498>',
                 '<:Ness:938447276416851988>',
                 '<:Bowser:929116220312150107>', 
                 '<:Falcon:856660388753309696>', '<:Puff:856660446810341377>', '<:Doc:856660362207166534>'],
        "closed": False,
    }

    sdplayers[userID] = {"sdgameID": gameID, "messageObj": smashdowngame, "opponent": "n/a"}

    # print(sdgames)
    # print(sdplayers)


@client.command()
async def ironman(ctx):
    username = ctx.message.author
    userpfp = ctx.message.author.avatar_url
    embed = discord.Embed(
        title=f"Randomized Roster for {username}",
        color=defaultColor,
        description=randomroster()
    )
    embed.set_thumbnail(url=userpfp)
    await ctx.send(embed=embed)


@client.command()
async def characters(ctx):
    userID = ctx.message.author.id
    # checks if user is banned
    if banCheck(userID) == True:
        return
    channelOrigin = ctx.message.channel.id
    # fetch change
    discordUser = client.get_user(userID)
    dm = await discordUser.create_dm()
    charaList = createCharaList()
    if channelOrigin in channelList:
        await ctx.send("I've sent you a DM with all character inputs I can currently recognize.")
    await dm.send(content=charaList)


@client.command()
async def ban(ctx):
    # checks if command is from the mod channel
    if ctx.message.channel.id != modChannel:
        return

    playerID = int(ctx.message.content[7:-1])
    # print(playerID)

    # checks if player in question is a real person
    if client.get_user(playerID) == None:
        # print("found no one")
        return

    if playerID in banned:
        await ctx.send("That player is already banned.")
        return

    if playerID in rankings["NETP"].keys():
        rankings["NETP"].pop(playerID)
        # print(rankings["NETP"])

    if playerID in rankings["WIFI"].keys():
        rankings["WIFI"].pop(playerID)
        # print(rankings["WIFI"])

    # print("banning: ", playerID)
    banned.append(int(playerID))
    # print(banned)

    saveBanList(banned)
    await ctx.send(f"<@{playerID}> was successfully banned.")


@client.command()
async def unban(ctx):
    # checks if command is from the mod channel
    if ctx.message.channel.id != modChannel:
        return
    playerID = int(ctx.message.content[9:-1])

    # checks if player in question is a real person
    if client.get_user(playerID) == None:
        return

    # checks if player in question is currently banned, otherwise it returns
    if playerID not in banned:
        return

    banned.remove(playerID)
    # print("removed player: ", banned)

    saveBanList(banned)

    await ctx.send(f"<@{playerID}> was successfully unbanned.")


@client.command()
async def changerank(ctx):
    ladderType = ctx.message.content[12:16].upper()

    if ladderType != "NETP" and ladderType != "WIFI":
        await ctx.send("Please specify what ladder you want to change rankings from.")
        return

    ladderColor = attributes[ladderType]["color"]
    winnerID = int(ctx.message.content[20:38].upper())
    loserID = int(ctx.message.content[43:61].upper())
    winnerName = client.get_user(winnerID)
    loserName = client.get_user(loserID)

    if winnerID not in rankings[ladderType].keys() or loserID not in rankings[ladderType].keys():
        await ctx.send(f"One or both of the users are not in the {ladderType} ladder.")
        return

    # print(ctx.message.content)
    # print("ladderType: ", ladderType)
    # print("winnerID: ", winnerID)
    # print("loserID: ", loserID)

    oldWinnerELO = rankings[ladderType][winnerID]
    oldLoserELO = rankings[ladderType][loserID]
    calculateELO(winnerID, loserID, ladderType, endCheck=False, modCheck=True, wNeeded=2)
    newWinnerELO = displayELO(winnerID, ladderType)
    newLoserELO = displayELO(loserID, ladderType)
    # winnerChange = showELOChange(rankings[ladderType][winnerID], oldWinnerELO)
    # loserChange = showELOChange(rankings[ladderType][loserID], oldLoserELO)
    embed = discord.Embed(
        title=f"Updated ELOs for {winnerName} and {loserName}",
        color=ladderColor,
        description=f"{winnerName} [{newWinnerELO}]\n"
                    f"{loserName} [{newLoserELO}]"
    )
    await ctx.send(embed=embed)


@client.command()
async def top(ctx):
    # checks if command is coming from it's designated channel
    if ctx.message.channel.id != miscChannel:
        await ctx.message.delete()
        await ctx.send(f"This command can only be used in <#{miscChannel}>", delete_after=10)
        return

    # checks if the user is banned
    if banCheck(ctx.message.author.id) == True:
        return

    topType = "NETP"
    page = ctx.message.content[4:].strip()
    if page == "":
        page = 1
    page = int(page)
    #if topType == "WIFI" or topType == "NETP":
    symbol = attributes[topType]["symbol"]
    embed = discord.Embed(
        title=f"{symbol} {topType} Leaderboard",
        color=attributes[topType]["color"],
        description=buildLBoard(rankings[topType], topType, page, topType)
    )
    await ctx.send(embed=embed)
        # print("recognized")
    #else:
        #await ctx.send("Please specify what type of leaderboard you'd like to view. (NETP or WIFI)", delete_after=10)

  
@client.command()
async def rank(ctx):
    # checks if command is coming from it's designated channel
    if ctx.message.channel.id != miscChannel:
        await ctx.message.delete()
        await ctx.send(f"This command can only be used in <#{miscChannel}>", delete_after=10)
        return

    authorID = ctx.message.author.id

    if banCheck(authorID) == True:
        return

    if ctx.message.content[6:].isdigit():
        boardType = "NETP"
        standing = ctx.message.content[6:]
        if standing == "":
            await ctx.send("Please specify what player standing you'd like to search for \n (ie. ``-rank wifi 3``)",
                           delete_after=8)
            return
        standing = int(standing)
        # print("boardType: ", boardType)
        # print("standing: ", standing)
        playerID = findPlayer(boardType, standing)


    else:
        playerID = ctx.message.content[9:-1]
        # print("ctx:", ctx.message.content)
        # print("playerID:", playerID)
        if playerID == "":
            playerID = authorID
        else:
            playerID = int(playerID)


    playerInfo = client.get_user(playerID)

    # checks if the user is in the rankings

    if playerID == 0:
        await ctx.send("No user with such standing found...")
        return
    elif playerID not in rankings["NETP"] and playerID not in rankings["WIFI"]:
        await ctx.send("No rankings found...")
        return

    embed = discord.Embed(
        title=f"{playerInfo}",
        colour=discord.Colour(defaultColor)
    )
    embed.set_thumbnail(url=playerInfo.avatar_url)

    if playerID in rankings["NETP"]:
        showNetpELO = displayELO(playerID, 'NETP')
        if playerID in preranked["NETP"].keys():
            gamesNeeded = preranked["NETP"][playerID]
            plural = ""
            if gamesNeeded > 1:
                plural = "s"
            valueContentNetp = f"Player currently unranked. \n{gamesNeeded} more game{plural} needed to be ranked."
        else:
            results = getPlacement(rankings["NETP"], playerID, "NETP")
            netpPlacement = results[0]
            netpNumOfPlayers = results[1]
            valueContentNetp = f"(Top {netpPlacement} out of {netpNumOfPlayers})"
        embed.add_field(name=f"{netpSymbol} NETP ELO: {showNetpELO}",
                        value=valueContentNetp,
                        inline=False)
    await ctx.send(embed=embed)


@client.command()
async def bo3(ctx):
    # checks if search message is from the search channel
    if ctx.message.channel.id != searchChannel:
        if ctx.message.channel.id !=testChannel:
            await ctx.message.delete()
            await ctx.send(f"This command can only be used in <#{searchChannel}>", delete_after=10)
            return
    if banCheck(ctx.message.author.id) == True:
        return
    # if user is already in a match, they will be unable to queue up a search
    if ctx.message.author.id in players2matches.keys():
        await ctx.message.delete()
        await ctx.send("‼ You're currently in a match. ‼", delete_after=4)
        return

    matchType = "NETP"
    setType = "bo3"
    
    if matchType != "NETP" and matchType != "WIFI":
        return
    if setType not in sets:
        return

    if ctx.message.author.id in searching[matchType][setType]:
        await ctx.send("‼ You're already searching for that. ‼", delete_after=4)
        await ctx.message.delete()
        return

    if matchType == "NETP":
        embedColor = netpColor
        icon = attributes["NETP"]['symbol']
    else:
        embedColor = wifiColor
        icon = attributes["WIFI"]['symbol']

    playerID = ctx.message.author.id

    # if the player isn't already in the ranking system, they get added
    if playerID not in rankings[matchType].keys():
        addPlayer(playerID, matchType)
    # print(rankings)

    showELO = displayELO(playerID, matchType)
    embed = discord.Embed(
        title=f"{ctx.message.author} [{showELO}] is searching for a match... \n"
              f"( {icon} {matchType} || {setType} )",
        description=f"({abort} = cancel search)\n(Search will be deleted after 1 hour)\nClick on {challenge} to challenge them!\n"
                    f"Or unreact to withdraw your challenge.",
        color=discord.Colour(embedColor))
    embed.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
    matchSearch = await ctx.send(embed=embed, delete_after=3600)
    searching[matchType][setType].append(playerID)
    searchMessages[matchSearch.id] = {"player": playerID,
                                      "matchType": matchType,
                                      "setType": setType,
                                      "challenges": [],
                                      "challengers": [],
                                      "color": embedColor,
                                      "messageObj": matchSearch,
                                      "queue": ctx}
    # Keeps track of the player who sent the search, type of match, and type of set. and distinguishes search messages

    # print("searching: ", searching)
    # print("searchMessages:", searchMessages)

    for icon in searchIcons:
        await matchSearch.add_reaction(icon)


@client.command()
async def bo5(ctx):
    # checks if search message is from the search channel
    if ctx.message.channel.id != searchChannel:
        if ctx.message.channel.id !=testChannel:
            await ctx.message.delete()
            await ctx.send(f"This command can only be used in <#{searchChannel}>", delete_after=10)
            return
    if banCheck(ctx.message.author.id) == True:
        return
    # if user is already in a match, they will be unable to queue up a search
    if ctx.message.author.id in players2matches.keys():
        await ctx.message.delete()
        await ctx.send("‼ You're currently in a match. ‼", delete_after=4)
        return

    matchType = "NETP"
    setType = "bo5"
   
    if matchType != "NETP" and matchType != "WIFI":
        return
    if setType not in sets:
        return

    if ctx.message.author.id in searching[matchType][setType]:
        await ctx.send("‼ You're already searching for that. ‼", delete_after=4)
        await ctx.message.delete()
        return

    if matchType == "NETP":
        embedColor = netpColor
        icon = attributes["NETP"]['symbol']
    else:
        embedColor = wifiColor
        icon = attributes["WIFI"]['symbol']

    playerID = ctx.message.author.id

    # if the player isn't already in the ranking system, they get added
    if playerID not in rankings[matchType].keys():
        addPlayer(playerID, matchType)
    # print(rankings)

    showELO = displayELO(playerID, matchType)
    embed = discord.Embed(
        title=f"{ctx.message.author} [{showELO}] is searching for a match... \n"
              f"( {icon} {matchType} || {setType} )",
        description=f"({abort} = cancel search)\n(Search will be deleted after 1 hour)\nClick on {challenge} to challenge them!\n"
                    f"Or unreact to withdraw your challenge.",
        color=discord.Colour(embedColor))
    embed.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
    matchSearch = await ctx.send(embed=embed, delete_after=3600)
    searching[matchType][setType].append(playerID)
    searchMessages[matchSearch.id] = {"player": playerID,
                                      "matchType": matchType,
                                      "setType": setType,
                                      "challenges": [],
                                      "challengers": [],
                                      "color": embedColor,
                                      "messageObj": matchSearch,
                                      "queue": ctx}
    # Keeps track of the player who sent the search, type of match, and type of set. and distinguishes search messages

    # print("searching: ", searching)
    # print("searchMessages:", searchMessages)

    for icon in searchIcons:
        await matchSearch.add_reaction(icon)



@client.event
async def on_message_delete(message):
    messageID = message.id

    if messageID in sdgames.keys():
        forgetSD(messageID)
        # print("sdgames: ", sdgames)
        # print("sdplayers: ", sdplayers)
        return

    if messageID not in searchMessages.keys():
        return
    commandmessage = searchMessages[messageID]["queue"]
    forgetMessage(messageID)
    await commandmessage.message.delete()
    # print("searchMessages should be empty: ", searchMessages)
    # print("challengeMessages should be empty: ", challengeMessages)
    # print("searching should be empty: ", searching)


@client.event
async def on_reaction_add(reaction, user):
    # print("emote:", reaction.emoji)

    if banCheck(user.id) == True:
        return

    messageID = reaction.message.id
    challengerID = user.id
    botID = client.user.id

    if challengerID == botID:  # client.user.id is the bot's ID. This prevents the bot from triggering any of the events when it sets up the emotes
        return

    if reaction.message.author.id != botID:  # Checks if reaction to message is not Brawlbot's
        return

    if messageID in searchMessages.keys() or messageID in matches.keys():  # Checks if this message is one that expects reactions on

        if messageID in searchMessages.keys():
            playerID = searchMessages[messageID]["player"]

        # event the player wants to cancel the search
        if reaction.emoji == abort and challengerID == playerID:  # only the person that queues up can cancel the search
            commandmessage = searchMessages[messageID]["queue"]
            forgetMessage(messageID)
            await reaction.message.delete()
            await commandmessage.message.delete()
            # print("searching should be gone: ", searching)
            # print("searchMessages should have deleted", searchMessages)
            # print("should have deleted challenges", challengeMessages)
        # event when someone clicks on challenge
        elif reaction.emoji == challenge:
            if challengerID == playerID:  # prevents you from challenging yourself
                return
            if user.id in players2matches.keys():
                return
            setType = searchMessages[messageID]["setType"]
            matchType = searchMessages[messageID]["matchType"]
            embedColor = searchMessages[messageID]["color"]
            icon = attributes[matchType]['symbol']
            if challengerID not in rankings[matchType].keys():
                addPlayer(challengerID, matchType)
                # print(rankings)
            showELO = displayELO(challengerID, matchType)
            embed = discord.Embed(
                title=f"{user} [{showELO}] would like to challenge you! \n"
                      f"( {icon} {matchType} || {setType} )",
                description=f"{accept} = accept challenge!",
                color=discord.Colour(embedColor))
            embed.set_thumbnail(url=user.avatar_url)  # shows the challenger's pfp
            # fetch change
            player = client.get_user(playerID)
            dm = await player.create_dm()

            dmChallenge = await dm.send(embed=embed)
            await dmChallenge.add_reaction(accept)

            challengeMessages[dmChallenge.id] = {"challenger": challengerID,
                                                 "searchMessage": reaction.message.id,
                                                 "messageObj": dmChallenge}
            searchMessages[messageID]["challenges"].append(dmChallenge.id)
            searchMessages[messageID]["challengers"].append(user.id)
            # print("challengers: ", searchMessages[messageID]["challengers"])
            # print("challengeMessages: ", challengeMessages)  # testing
            # print("searchMessages:", searchMessages)  # testing

        # event when players are in a match and want to cancel
        elif reaction.emoji == cancel and user.id in matches[messageID]["players"].keys():
            matches[messageID]["cancel"][user.id] = True
            # print("matches:", matches)
            if len(matches[messageID]["cancel"].keys()) == 2:
                matchType = matches[messageID]["matchType"]
                opponent = opponents[user.id]
                rankings[matchType][user.id] = matches[messageID]['players'][user.id]['elo']
                rankings[matchType][opponent] = matches[messageID]['players'][opponent]['elo']
                saveRankings(rankings)

                for plyrs in matches[messageID]["players"].keys():
                    players2matches.pop(plyrs)
                    opponents.pop(plyrs)
                # print("opponents should be empty: ", opponents)
                # print("players should be empty: ", players2matches)
                await matches[messageID]["messageObj"].delete()
                await matches[messageID]["pings"].delete()
                matches.pop(messageID)
                # print("matches should now be gone: ", matches)

        # event when players click on a reaction of a stage
        elif str(reaction.emoji) in matches[messageID]["stages"]:

            # game 1 procedures
            if matches[messageID]["gameCount"] == 1:
                if user.id == matches[messageID]["banning"]:
                    # print(f"ban is found{user.id}")
                    if len(matches[messageID]["stages"]) == 5:
                        matches[messageID]["banning"] = opponents[user.id]
                        matches[messageID]["stages"].remove(str(reaction.emoji))
                        # print("remaining stages: ", matches[messageID]["stages"])  # testing
                        # print("banning: ", matches[messageID]["banning"])  # testing
                        matchWindowObj = matches[messageID]['messageObj']
                        newEmbed = matchWindowObj.embeds[0]
                        nextStrike = opponents[user.id]
                        newEmbed.set_field_at(0, name=f"Game 1",
                                                value=f"{matches[messageID]['heading']}"
                                                    f"\n"
                                                    f"Waiting for <@{nextStrike}> to strike 2. (click on the reactions):\n"
                                                    f"{showstagelist(matches[messageID]['stages'])}",
                                                inline=False)
                        await reaction.clear()
                        await matchWindowObj.edit(embed=newEmbed)

                    elif len(matches[messageID]["stages"]) == 4:
                        matches[messageID]["stages"].remove(str(reaction.emoji))
                        # print("remaining stages: ", matches[messageID]["stages"])  # testing
                        # print("banning: ", matches[messageID]["banning"])  # testing
                        matchWindowObj = matches[messageID]['messageObj']
                        newEmbed = matchWindowObj.embeds[0]
                        nextStrike = user.id
                        newEmbed.set_field_at(0, name=f"Game 1",
                                                  value=f"{matches[messageID]['heading']}"
                                                        f"\n"
                                                        f"Waiting for <@{nextStrike}> to strike 1. (click on the reactions):\n"
                                                        f"{showstagelist(matches[messageID]['stages'])}",
                                                  inline=False)
                        await reaction.clear()
                        await matchWindowObj.edit(embed=newEmbed)

                    elif len(matches[messageID]["stages"]) == 3:
                        matches[messageID]["banning"] = opponents[user.id]
                        matches[messageID]["stages"].remove(str(reaction.emoji))
                        #print("remaining stages: ", matches[messageID]["stages"])  # testing
                        #print("banning: ", matches[messageID]["banning"])  # testing

                        matchWindowObj = matches[messageID]['messageObj']
                        newEmbed = matchWindowObj.embeds[0]
                        nextStrike = opponents[user.id]
                        newEmbed.set_field_at(0, name=f"Game 1",
                                              value=f"{matches[messageID]['heading']}"
                                                    f"\n"
                                                    f"Waiting for <@{nextStrike}> to strike. (click on the reactions):\n"
                                                    f"{matches[messageID]['stages'][0]} {emotes2stage[matches[messageID]['stages'][0]]} \n"
                                                    f"{matches[messageID]['stages'][1]} {emotes2stage[matches[messageID]['stages'][1]]} \n",
                                              inline=False)
                        await reaction.clear()
                        await matchWindowObj.edit(embed=newEmbed)

                    elif len(matches[messageID]["stages"]) == 2:
                        matches[messageID]["banning"] = "N/A"
                        matches[messageID]["stages"].remove(str(reaction.emoji))
                        #print("remaining stages: ", matches[messageID]["stages"])  # testing
                        #print("banning: ", matches[messageID]["banning"])  # testing
                        matchWindowObj = matches[messageID]['messageObj']
                        newEmbed = matchWindowObj.embeds[0]
                        newEmbed.set_field_at(0, name=f"Game 1",
                                              value=f"{matches[messageID]['heading']}"
                                                    f"Stage:\n"
                                                    f"{matches[messageID]['stages'][0]} {emotes2stage[matches[messageID]['stages'][0]]} \n"
                                                    f"\n"
                                                    f"(winner reports by clicking <:win:936376084348424232> / "
                                                    f"loser reports by clicking <:lose:936375892194758706>)",
                                              inline=False)
                        newEmbed.set_thumbnail(url=stageTNs[matches[messageID]['stages'][0]])
                        await reaction.clear()
                        await matchWindowObj.clear_reaction(matches[messageID]['stages'][0])
                        await matchWindowObj.edit(embed=newEmbed)
                        for icon in winloss:
                            await matchWindowObj.add_reaction(icon)

              # game 2 and onwards procedures
            elif matches[messageID]["gameCount"] >= 2:
                #print("made it to game 2+")
                matchWindowObj = matches[messageID]['messageObj']
                newEmbed = matchWindowObj.embeds[0]
                gameCount = matches[messageID]["gameCount"]
                selecting = opponents[user.id]
                if  matches[messageID]["winsNeeded"] == 3:
                  if user.id == matches[messageID]["banning"]:
                    matches[messageID]["banning"] = "N/A"
                    #print("made it to bans")
                    matches[messageID]["stagesel"] = opponents[user.id]
                    stage = f"<:{reaction.emoji.name}:{reaction.emoji.id}>"
                    #print("remaining stages", matches[messageID]["stages"])
                    newEmbed.set_field_at(gameCount - 1, name=f"Game {gameCount}",
                                              value=f"(Waiting for character selections...)\n"
                                                    f"Stage:\n"
                                                    f"{stage} {emotes2stage[stage]} \n"
                                                    f"\n",
                                              inline=False)
                    newEmbed.set_thumbnail(url=stageTNs[stage])
                    matches[messageID]["heading"] = "N/A"
                    for icon in matches[messageID]['stages']:
                        await matchWindowObj.clear_reaction(icon)
                    matches[messageID]["stages"] = [f"{stage}"]
                    await matchWindowObj.edit(embed=newEmbed)

                    dm = await (client.get_user(selecting)).create_dm()
                    charaSelect = discord.Embed(title=f"[Game {gameCount} | {stage} {emotes2stage[stage]}]",
                                                description=f"Choose your character for Game {gameCount}! \n Type out what character you will use.\n"
                                                            f"If you're staying on the same character, type ''stay''\n"
                                                            f"\n"
                                                                f"If you're having trouble selecting a character, type ``-characters``"
                                                                " to see a list of all character inputs I can recognize.",
                                                    color=defaultColor)
                    charaSelect.set_thumbnail(
                        url="https://cdn.discordapp.com/emojis/919693698093183036.webp?size=160&quality=lossless")
                    await dm.send(embed=charaSelect)
                  
                             
                elif  matches[messageID]["winsNeeded"] == 2:  
                  #print("made it to game 2+")
                  matchWindowObj = matches[messageID]['messageObj']
                  newEmbed = matchWindowObj.embeds[0]
                  gameCount = matches[messageID]["gameCount"]
                  selecting = opponents[user.id]
                  if user.id == matches[messageID]["banning"]:
                      matches[messageID]["banning"] = "N/A"
                      #print("made it to bans")
                      matches[messageID]["stagesel"] = opponents[user.id]
                      matches[messageID]["stages"].remove(str(reaction.emoji))
                      #print("remaining stages", matches[messageID]["stages"])
                      newEmbed.set_field_at(gameCount - 1, name=f"Game {gameCount}",
                                              value=f""
                                                  f"\n"
                                                  f"Waiting for <@{selecting}> to select their counterpick. (click on the reactions):\n"
                                                  f"{showstagelist(matches[messageID]['stages'])}",
                                              inline=False)
                      await reaction.clear()
                      await matchWindowObj.edit(embed=newEmbed)

                  elif matches[messageID]["stagesel"] == user.id:
                      #print("made it to stage selection")
                      matches[messageID]["banning"] = "N/A"
                      matches[messageID]["stagesel"] = "N/A"
                      stage = f"<:{reaction.emoji.name}:{reaction.emoji.id}>"
                      newEmbed.set_field_at(gameCount - 1, name=f"Game {gameCount}",
                                                value=f"(Waiting for character selections...)\n"
                                                      f"Stage:\n"
                                                      f"{stage} {emotes2stage[stage]} \n"
                                                      f"\n",
                                                inline=False)
                      newEmbed.set_thumbnail(url=stageTNs[stage])
                      matches[messageID]["heading"] = "N/A"
                      for icon in matches[messageID]['stages']:
                          await matchWindowObj.clear_reaction(icon)
                      matches[messageID]["stages"] = [f"{stage}"]
                      await matchWindowObj.edit(embed=newEmbed)

                      dm = await (client.get_user(selecting)).create_dm()
                      charaSelect = discord.Embed(title=f"[Game {gameCount} | {stage} {emotes2stage[stage]}]",
                                                  description=f"Choose your character for Game {gameCount}! \n Type out what character you will use.\n"
                                                              f"If you're staying on the same character, type ''stay''\n"
                                                              f"\n"
                                                                  f"If you're having trouble selecting a character, type ``-characters``"
                                                                  " to see a list of all character inputs I can recognize.",
                                                      color=defaultColor)
                      charaSelect.set_thumbnail(
                          url="https://media.discordapp.net/attachments/405387786036707329/843029286961414144/coinhand2.png")
                      await dm.send(embed=charaSelect)

        # event when win or loss is clicked
        elif str(reaction.emoji) in winloss and user.id in matches[reaction.message.id]["players"]:
            messageID = reaction.message.id
            if str(reaction.emoji) == win:
                matches[messageID]["winner"] = user.id
                # print("checking for winner: ", matches[messageID]["winner"])  # testing
            elif str(reaction.emoji) == loss:
                matches[messageID]["loser"] = user.id
                # print("checking for loser: ", matches[messageID]["loser"])  # testing

            # checks if opponent reported, otherwise it returns
            if str(reaction.emoji) == win and opponents[user.id] != matches[messageID]["loser"]:
                return

            elif str(reaction.emoji) == loss and opponents[user.id] != matches[messageID]["winner"]:
                return

            calculateELO(matches[messageID]["winner"], matches[messageID]["loser"], matches[messageID]["matchType"],
                         endCheck=False, modCheck=False, wNeeded=2)

            matches[messageID]["selections"][matches[messageID]["winner"]] = True
            matches[messageID]["selections"][matches[messageID]["loser"]] = False
            # print("both win and loss were selected")
            # print("winner should be selecting ", matches[messageID]["selections"][matches[messageID]["winner"]])
            # print("loser should not be selecting ", matches[messageID]["selections"][matches[messageID]["loser"]])
            winner = matches[messageID]['winner']
            loser = matches[messageID]['loser']
            winnerName = str(client.get_user(winner))[:-5]
            matches[messageID]["players"][winner]["wins"] += 1
            winnerChara = matches[messageID]['players'][winner]['character']
            if dsl == True:
                dslstage = matches[messageID]['stages']
                if dslstage[0] not in matches[messageID]['players'][winner]['dsl']:
                    matches[messageID]['players'][winner]['dsl'].append(dslstage[0])
            #print("dsl check: ", matches[messageID]['players'][winner])
            matchWindowObj = matches[messageID]["messageObj"]
            embedCount = matches[messageID]["gameCount"] - 1
            newEmbed = matchWindowObj.embeds[0]
            newEmbed.set_field_at(embedCount,
                                  name=f"Game {matches[messageID]['gameCount']} (Winner: {winnerChara} {winnerName})",
                                  value=f"{matches[messageID]['heading']}"
                                        f"Stage:\n"
                                        f"{matches[messageID]['stages'][0]} {emotes2stage[matches[messageID]['stages'][0]]} \n",
                                  inline=False
                                  )
            newEmbed.set_thumbnail(url='')
            await matchWindowObj.edit(embed=newEmbed)
            matches[messageID]["gameCount"] += 1
            if dsl == True:
                #print("dsl enabled")
                #print("fullstagelist: ", fullstagelist)
                matches[messageID]["stages"] = remainingstagelist(fullstagelist[:], matches[messageID]['players'][loser]['dsl'])
                #print("remaining stages after winloss: ", matches[messageID]["stages"])
            else:
                #print("stagelist not greater than 3")
                matches[messageID]["stages"] = fullstagelist[:]
                #print("fullstagelist: ", fullstagelist)
                #print("remaining stages after winloss: ", matches[messageID]["stages"])
            if  matches[messageID]["winsNeeded"] == 3:
              matches[messageID]["banning"] = matches[messageID]["loser"]
            elif  matches[messageID]["winsNeeded"] == 2:
               matches[messageID]["banning"] = matches[messageID]["winner"]
            matches[messageID]["winner"] = "N/A"
            matches[messageID]["loser"] = "N/A"
            # print("winner should be blank: ", matches[messageID]["winner"])
            # print("loser should be blank: ", matches[messageID]["loser"])
            matches[messageID]["heading"] = "N/A"
            # print("checking for updated game count: ", matches[messageID]["gameCount"])

            # if set is over
            if matches[messageID]["players"][user.id]["wins"] == matches[messageID]["winsNeeded"] or \
                    matches[messageID]["players"][opponents[user.id]]["wins"] == matches[messageID]["winsNeeded"]:
                winsNeed = matches[messageID]["winsNeeded"]
                calculateELO(winner, loser, matches[messageID]["matchType"], endCheck=True, modCheck=False,
                             wNeeded=winsNeed)
                matchType = matches[messageID]['matchType']
                newWinnerELO = rankings[matchType][winner]
                newLoserELO = rankings[matchType][loser]
                oldWinnerELO = matches[messageID]['players'][winner]['elo']
                oldLoserELO = matches[messageID]['players'][loser]['elo']
                winnerChange = showELOChange(newWinnerELO, oldWinnerELO)
                loserChange = showELOChange(newLoserELO, oldLoserELO)
                editPreranked(winner, matchType)
                editPreranked(loser, matchType)
                showWinnerELO = displayELO(winner, matchType)
                showLoserELO = displayELO(loser, matchType)
                forgetMessage(messageID)
                # print("players2matches should be empty: ", players2matches)
                # print("opponents should be empty: ", opponents)
                # print("matches should be forgotten: ", matches)
                embed = matchWindowObj.embeds[0]
                embed.add_field(name=f"Results",
                                value=f"{win} {str(client.get_user(winner))[:-5]} [{showWinnerELO}] {winnerChange}\n"
                                      f"{loss} {str(client.get_user(loser))[:-5]} [{showLoserELO}] {loserChange}",
                                inline=False)
                winnerAvatar = client.get_user(winner).avatar_url
                embed.set_thumbnail(url=winnerAvatar)
                await matchWindowObj.edit(embed=embed)
                await matchWindowObj.clear_reactions()
                await matchWindowObj.unpin()

            #otherwise
            elif matches[messageID]["winsNeeded"] == 2:
                  banning = matches[messageID]["banning"]
                  embed = matchWindowObj.embeds[0]
                  embed.add_field(name=f"Game {matches[messageID]['gameCount']}",
                                value=f""
                                      f"\n"
                                      f"Waiting for <@{banning}> to ban. (click on the reactions):\n"
                                      f"{showstagelist(matches[messageID]['stages'])}",
                                inline=False)
                  await matchWindowObj.edit(embed=embed)
                  for icon in winloss:
                    await matchWindowObj.clear_reaction(icon)
                  newstages = []
                  for stageicon in matches[messageID]['stages']:
                    newstages.append(stage2emotes[stageicon])
                # print("newstages", newstages)
                  for icon in newstages:
                    await matchWindowObj.add_reaction(icon)

            elif matches[messageID]["winsNeeded"] == 3:
                  banning = matches[messageID]["banning"]
                  embed = matchWindowObj.embeds[0]
                  embed.add_field(name=f"Game {matches[messageID]['gameCount']}",
                                value=f""
                                      f"\n"
                                      f"Waiting for <@{banning}> to choose their counterpick. (click on the reactions):\n"
                                      f"{showstagelist(matches[messageID]['stages'])}",
                                inline=False)
                  await matchWindowObj.edit(embed=embed)
                  for icon in winloss:
                    await matchWindowObj.clear_reaction(icon)
                  newstages = []
                  for stageicon in matches[messageID]['stages']:
                    newstages.append(stage2emotes[stageicon])
                # print("newstages", newstages)
                  for icon in newstages:
                    await matchWindowObj.add_reaction(icon)

        # if the reaction is coming from a mod
        elif reaction.emoji == modkey:
            messageID = reaction.message.id

            # checks if key emote is on a match
            if messageID not in matches.keys():
                return

            matchWindowObj = matches[messageID]["messageObj"]
            embed = matchWindowObj.embeds[0]
            embed.add_field(name="Match was ended by mod.", value="🔨", inline=False)
            forgetMessage(messageID)
            await matchWindowObj.edit(embed=embed)
            await matchWindowObj.clear_reactions()

        # smashdown related reactions
        elif reaction.message.id in sdgames.keys():
            if reaction.emoji == join:
                print("join was clicked")

            # checks if same person is joining their own game
            if user.id in sdplayers.keys():
                # print("user already in match tried to join")
                return

            if sdgames[reaction.message.id]["closed"] == True:
                return

            sdgames[reaction.message.id]["closed"] = True

            messageID = reaction.message.id
            opponent = sdgames[messageID]["playerlist"][0]
            sdgames[messageID]["playerlist"].append(user.id)
            opponentName = client.get_user(opponent)
            username = client.get_user(user.id)

            sdplayers[user.id] = {"sdgameID": messageID, "messageObj": sdgames[messageID]["messageObj"],
                                  "opponent": opponent}
            sdplayers[opponent]["opponent"] = user.id
            sdgames[messageID]["players"][user.id] = {"character": "n/a", "wins": 0, "selecting": False,
                                                      "usedCharacters": [],
                                                      "field": 1}

            firstpick = random.choice(sdgames[messageID]["playerlist"])

            sdgames[messageID]["players"][firstpick]["selecting"] = True

            # print("sdplayers: ", sdplayers)
            # print("sdgames: ", sdgames)

            if sdgames[messageID]["players"][opponent]["selecting"] == True:
                selectmessageOpp = f"waiting for <@{opponent}>\nto pick their character...\n(type it in this chat)"
                selectmessageUsr = ""
            else:
                selectmessageOpp = f""
                selectmessageUsr = f"waiting for <@{user.id}>\nto pick their character...\n(type it in this chat)"

            newEmbed = discord.Embed(title="Smashdown!",
                                     description=showroster(sdgames[messageID]["remaining"], characterlist),
                                     color=defaultColor)

            newEmbed.add_field(name=opponentName, value=f"Wins: 0 🏆\n\n{selectmessageOpp}", inline=True)
            newEmbed.add_field(name=username, value=f"Wins: 0 🏆\n\n{selectmessageUsr}", inline=True)
            newEmbed.set_footer(text=f"Click on {leave} to end game.")

            sdgameMesObj = sdgames[messageID]["messageObj"]

            await sdgameMesObj.clear_reaction(join)
            await sdgameMesObj.edit(embed=newEmbed)

        # if player is trying to leave a game
        elif reaction.emoji == leave:
            if user.id not in sdgames[reaction.message.id]["playerlist"]:
                return
            # print("leave clicked")

            sdgameObj = sdgames[reaction.message.id]["messageObj"]

            if len(sdgames[reaction.message.id]["playerlist"]) == 1:
                await sdgameObj.delete()

            elif len(sdgames[reaction.message.id]["playerlist"]) == 2:
                await sdgameObj.clear_reactions()
                sdgameID = reaction.message.id
                opponent = sdplayers[user.id]["opponent"]

                rosterResults = sdgameObj.embeds[0]
                rosterResults.description = f"{showused(client.get_user(user.id), sdgames[sdgameID]['players'][user.id]['usedCharacters'])}\n" \
                                            f"{showused(client.get_user(opponent), sdgames[sdgameID]['players'][opponent]['usedCharacters'])}"

                updating = sdgameObj.embeds[0]
                updating2 = sdgameObj.embeds[0]
                footer = sdgameObj.embeds[0]

                userfield = sdgames[sdgameID]["players"][user.id]["field"]
                oppfield = sdgames[sdgameID]["players"][opponent]["field"]

                updating.set_field_at(index=userfield, name=f"{client.get_user(user.id)}",
                                      value=f"Wins: {sdgames[sdgameID]['players'][user.id]['wins']} 🏆\n\n")

                updating2.set_field_at(index=oppfield, name=f"{client.get_user(opponent)}",
                                       value=f"Wins: {sdgames[sdgameID]['players'][opponent]['wins']} 🏆\n\n")

                footer.set_footer(text="")

                await sdgameObj.edit(embed=rosterResults)
                await sdgameObj.edit(embed=updating)
                await sdgameObj.edit(embed=updating2)
                await sdgameObj.edit(embed=footer)

            forgetMessage(messageID)
            # print("sdgames should be deleted: ", sdgames)
            # print("sdplayers should be deleted: ", sdplayers)


        # if win or loss is reported on smashdown
        elif str(reaction.emoji) in winloss and user.id in sdplayers:
            # print("win loss recognized")
            sdgameID = sdplayers[user.id]["sdgameID"]
            nextgame = False
            if str(reaction.emoji) == win:
                sdgames[sdgameID]["winner"] = user.id
                # print("checking for winner: ", sdgames[sdgameID])
                if sdgames[sdgameID]["loser"] == sdplayers[user.id]["opponent"]:
                    nextgame = True
            elif str(reaction.emoji) == loss:
                sdgames[sdgameID]["loser"] = user.id
                # print("checking for loser: ", sdgames[sdgameID])
                if sdgames[sdgameID]["winner"] == sdplayers[user.id]["opponent"]:
                    nextgame = True

            if nextgame == True and sdgames[sdgameID]["remaining"] != 0:
                # print("moving on to the next game")

                sdgameObj = sdplayers[user.id]["messageObj"]

                for icon in winloss:
                    await sdgameObj.clear_reaction(icon)

                loser = sdgames[reaction.message.id]["loser"]
                winner = sdplayers[loser]["opponent"]
                loserfield = sdgames[reaction.message.id]["players"][loser]["field"]
                winnerfield = sdgames[reaction.message.id]["players"][winner]["field"]

                sdgames[sdgameID]["players"][winner]["wins"] += 1
                sdgames[sdgameID]["winner"] = "n/a"
                sdgames[sdgameID]["loser"] = "n/a"
                updating = sdgameObj.embeds[0]
                updating2 = sdgameObj.embeds[0]

                if len(sdgames[sdgameID]["remaining"]) > 1:
                    sdgames[reaction.message.id]["players"][loser]["selecting"] = True
                    sdgames[reaction.message.id]["players"][loser]["character"] = "n/a"
                    sdgames[reaction.message.id]["players"][winner]["character"] = "n/a"

                    updating.set_field_at(index=loserfield, name=f"{client.get_user(loser)}",
                                          value=f"Wins: {sdgames[sdgameID]['players'][loser]['wins']} 🏆\n\n"
                                                f"waiting for <@{loser}>\nto pick their character...\n(type it in this chat)")

                    updating2.set_field_at(index=winnerfield, name=f"{client.get_user(winner)}",
                                           value=f"Wins: {sdgames[sdgameID]['players'][winner]['wins']} 🏆\n\n")
                # if the roster is down to 1 character
                elif len(sdgames[sdgameID]["remaining"]) == 1:
                    # print("final character detected")
                    finalchara = sdgames[sdgameID]["remaining"][0]
                    sdgames[sdgameID]["remaining"].remove(finalchara)
                    # print("remaining should be empty: ", sdgames[sdgameID]["remaining"])
                    sdgames[reaction.message.id]["players"][loser]["character"] = finalchara
                    sdgames[reaction.message.id]["players"][winner]["character"] = finalchara

                    sdgames[sdgameID]['players'][winner]['usedCharacters'].append(finalchara)
                    sdgames[sdgameID]['players'][loser]['usedCharacters'].append(finalchara)

                    updating.set_field_at(index=loserfield, name=f"{client.get_user(loser)} {finalchara}",
                                          value=f"Wins: {sdgames[sdgameID]['players'][loser]['wins']} 🏆\n\n")

                    updating2.set_field_at(index=winnerfield, name=f"{client.get_user(winner)} {finalchara}",
                                           value=f"Wins: {sdgames[sdgameID]['players'][winner]['wins']} 🏆\n\n")

                    updatedRoster = sdgameObj.embeds[0]
                    updatedRoster.description = showroster(sdgames[sdgameID]["remaining"], characterlist)
                    await sdgameObj.edit(embed=updatedRoster)
                    for icon in winloss:
                        await sdgameObj.add_reaction(icon)

                # if there are no more characters
                elif len(sdgames[sdgameID]["remaining"]) == 0:
                    winnermark = ""
                    losermark = ""

                    if sdgames[sdgameID]['players'][winner]['wins'] > sdgames[sdgameID]['players'][loser]['wins']:
                        winnermark = "👑"

                    elif sdgames[sdgameID]['players'][winner]['wins'] < sdgames[sdgameID]['players'][loser]['wins']:
                        losermark = "👑"

                    # elif sdgames[sdgameID]['players'][winner]['wins'] == sdgames[sdgameID]['players'][loser]['wins']:
                    # drawmsg = sdgameObj.embeds[0]
                    # drawmsg.add_field(name="Draw Game", value='🎌', inline=False)
                    # await sdgameObj.edit(embed=drawmsg)

                    updating.set_field_at(index=loserfield, name=f"{losermark} {client.get_user(loser)} {losermark}",
                                          value=f"Wins: {sdgames[sdgameID]['players'][loser]['wins']} 🏆\n\n")

                    updating2.set_field_at(index=winnerfield, name=f"{winnermark} {client.get_user(winner)} {winnermark}",
                                           value=f"Wins: {sdgames[sdgameID]['players'][winner]['wins']} 🏆\n\n")

                    rosterResults = sdgameObj.embeds[0]
                    rosterResults.description = f"{showused(client.get_user(winner), sdgames[sdgameID]['players'][winner]['usedCharacters'])}\n" \
                                                f"{showused(client.get_user(loser), sdgames[sdgameID]['players'][loser]['usedCharacters'])}"

                    await sdgameObj.edit(embed=rosterResults)
                    await sdgameObj.clear_reactions()
                    forgetMessage(sdgameID)
                    # print("sdgames should be empty", sdgames)
                    # print("sdplayers should be empty", sdplayers)

                await sdgameObj.edit(embed=updating)
                await sdgameObj.edit(embed=updating2)


@client.event
async def on_reaction_remove(reaction, user):
    if banCheck(user.id) == True:
        return

    messageID = reaction.message.id
    userID = user.id
    # print("messageID: ", messageID)
    # print("reaction revoker id: ", userID)
    botID = client.user.id

    # client.user.id is the bot's ID. This prevents the bot from triggering any of the events when it sets up the emotes
    if userID == botID:
        return

    if reaction.emoji == challenge:
        if messageID not in searchMessages.keys():
            return
        searchMessages[messageID]["challengers"].remove(userID)
        # print("user should be removed: ", searchMessages[messageID]["challengers"])
        # print("challenger successfully removed")


@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(matchChannel)
    playerID = payload.user_id
    botID = client.user.id
    # print("payload: ", payload)

    if banCheck(playerID) == True:
        return

    # checks if reaction is on a challenge message
    if payload.message_id not in challengeMessages.keys():
        # print("not in there")
        return

    # event for when accept is clicked on
    elif payload.emoji.name == accept and playerID != botID:
        challengerID = challengeMessages[payload.message_id]['challenger']
        # print("payload: ", payload)
        challengemes = payload.message_id
        searchmes = challengeMessages[challengemes]["searchMessage"]
        # fetch change
        playerName = client.get_user(playerID)
        # fetch change
        challengerName = client.get_user(challengerID)

        # if the challenger withdrew their challenge, the bot deletes the challenge message and notifies the user
        if challengerID not in searchMessages[searchmes]["challengers"]:
            challengeObj = challengeMessages[challengemes]["messageObj"]
            await challengeObj.delete()
            withdrewDM = await playerName.create_dm()
            await withdrewDM.send(f"{challengerName} has withdrawn their challenge.")
            return

        # the the challenger is playing someone else, the bot deletes the challenge message and notifies the user
        if challengerID in players2matches.keys():
            challengeObj = challengeMessages[challengemes]["messageObj"]
            await challengeObj.delete()
            inMatchDM = await playerName.create_dm()
            await inMatchDM.send(f"{challengerName} is currently in a match.")
            return

        matchType = searchMessages[searchmes]["matchType"]
        setType = searchMessages[searchmes]["setType"]
        icon = attributes[matchType]['symbol']
        embedColor = searchMessages[searchmes]["color"]

        winsNeeded = int(setType[2:])//2 + 1
        # print(winsNeeded)

        # bot now stops keeping track of the search and corresponding challenge messages
        await searchMessages[searchmes]["queue"].message.delete()
        await searchMessages[searchmes]["messageObj"].delete()
        forgetMessage(searchmes)

        pings = await channel.send(f"<@{playerID}> <@{challengerID}>")

        playerELO = displayELO(playerID, matchType)
        challengerELO = displayELO(challengerID, matchType)
        embed = discord.Embed(
            title=f"{str(playerName)[:-5]} [{playerELO}] vs {str(challengerName)[:-5]} [{challengerELO}] \n"
                  f"( {icon} {matchType} || {setType} )",
            description=f"(Both players can agree to cancel the set by clicking: {cancel}.)",
            color=discord.Colour(embedColor))
        embed.add_field(name="Game 1", value="(double blind in progress...)\n")
        matchWindow = await channel.send(embed=embed)
        await matchWindow.pin()
        matches[matchWindow.id] = {
            "players": {playerID: {"character": "N/A", "wins": 0, "elo": rankings[matchType][playerID], "dsl": []},
                        challengerID: {"character": "N/A", "wins": 0, "elo": rankings[matchType][challengerID], "dsl": []}
                        },
            "winsNeeded": winsNeeded,
            "cancel": {},
            "heading": "N/A",
            "gameCount": 1,
            "stages": starters[:],
            "banning": "N/A",
            "stagesel": "N/A",
            "selections": {playerID: True, challengerID: True},
            "winner": "N/A",
            "loser": "N/A",
            "pings": pings,
            "messageObj": matchWindow,
            "matchType": matchType
        }
        #print("matches: ", matches)  # testing

        players2matches[playerID] = matchWindow.id
        players2matches[challengerID] = matchWindow.id
        opponents[playerID] = challengerID
        opponents[challengerID] = playerID
        # print("opponents", opponents)
        # print("players: ", players2matches)

        await matchWindow.add_reaction(cancel)
        dm1 = await playerName.create_dm()
        dm2 = await challengerName.create_dm()
        charaSelect = discord.Embed(title="[Game 1] (double blind)",
                                    description="Choose your character! \n Type out what character you will use.\n"
                                                "\n"
                                                "If you're having trouble selecting a character, type ``-characters``"
                                                " to see a list of all character inputs I can recognize.",
                                    color=defaultColor)
        charaSelect.set_thumbnail(
            url="https://cdn.discordapp.com/emojis/919693698093183036.webp?size=160&quality=lossless")
        await dm1.send(embed=charaSelect)
        await dm2.send(embed=charaSelect)

        # print("searches should be deleted: ", searchMessages)  # testing
        # print("challenges should be deleted: ", challengeMessages)

    # elif payload.emoji.name == stay and playerID != client.user.id:
    # print("will work on this later")


@client.event
async def on_message(message):
    await client.process_commands(message)
    authorID = message.author.id
    botID = 837093793722662942
    content = str(message.content.lower().strip())

    if banCheck(authorID) == True:
        return

    # bot ignores it's own messages
    if authorID == botID:
        return
    # bot ignores non-command based messages if it's not in a DM
    if message.guild in client.guilds and authorID in sdplayers.keys():
        # print("message recieved")
        sdgameID = sdplayers[authorID]["sdgameID"]
        if sdgames[sdgameID]["players"][authorID]["selecting"] == True:
            if content in brawlChara.keys():
                # print("Valid input recognized")
                await message.delete()
                if brawlChara[content] not in sdgames[sdgameID]["remaining"]:
                    return

                sdgames[sdgameID]["players"][authorID]["selecting"] = False
                sdgameObject = sdgames[sdgameID]["messageObj"]
                charaIcon = brawlChara[content]

                sdgames[sdgameID]["remaining"].remove(charaIcon)
                sdgames[sdgameID]["players"][authorID]["usedCharacters"].append(charaIcon)
                sdgames[sdgameID]["players"][authorID]["character"] = charaIcon

                fieldnum = sdgames[sdgameID]["players"][authorID]["field"]

                opponentID = sdplayers[authorID]["opponent"]

                selectEmbed = sdgameObject.embeds[0]
                selectEmbed.set_field_at(index=fieldnum, name=f"{client.get_user(authorID)} {charaIcon}",
                                         value=f"Wins: {sdgames[sdgameID]['players'][authorID]['wins']} 🏆")
                updatedRoster = sdgameObject.embeds[0]
                updatedRoster.description = showroster(sdgames[sdgameID]["remaining"], characterlist)

                await sdgameObject.edit(embed=selectEmbed)
                await sdgameObject.edit(embed=updatedRoster)

                if sdgames[sdgameID]["players"][opponentID]["character"] == "n/a":
                    sdgames[sdgameID]["players"][opponentID]["selecting"] = True
                    opponentField = sdgames[sdgameID]["players"][opponentID]["field"]

                    opponentEmbed = sdgameObject.embeds[0]

                    opponentEmbed.set_field_at(index=opponentField, name=f"{client.get_user(opponentID)}",
                                               value=f"Wins: {sdgames[sdgameID]['players'][opponentID]['wins']} 🏆\n\n"
                                                     f"waiting for <@{opponentID}>\nto pick their character...\n(type it in this chat)")
                    await sdgameObject.edit(embed=opponentEmbed)
                else:
                    sdFooter = sdgameObject.embeds[0]
                    sdFooter.set_footer(
                        text=f"Click on {leave} to end game.\nReport wins and losses by reacting below.")
                    await sdgameObject.edit(embed=sdFooter)
                    for icon in winloss:
                        await sdgameObject.add_reaction(icon)
                    # print("sdgames: ", sdgames)
        return

    # checks if the message author is in a match
    if authorID in players2matches.keys():

        matchWindowID = players2matches[authorID]

        if matches[matchWindowID]["selections"][authorID] == False:
            return

        if content != "stay" and content not in brawlChara.keys():
            return

        opponent = opponents[authorID]
        matchchannel = f"<#{matchChannel}>"

        # character selection event for game 1
        if matches[matchWindowID]['gameCount'] == 1:
            character = str(message.content.lower().strip())
            if character not in brawlChara.keys():
                return

            matches[matchWindowID]["players"][authorID]["character"] = brawlChara[character]
            selectedDM = await message.author.create_dm()
            selectedChara = discord.Embed(title=f"{matches[matchWindowID]['players'][authorID]['character']} selected!",
                                          description=f"Return to matchmaking: Click here -> {matchchannel}",
                                          color=defaultColor)
            selectedChara.set_thumbnail(
                url="https://cdn.discordapp.com/emojis/818715531954880543.webp?size=160&quality=lossless")
            await selectedDM.send(embed=selectedChara)
            # print("matches for double blinds:", matches)

            # checks if opponent has their character locked in
            if matches[matchWindowID]["players"][opponent]["character"] != "N/A":
                matches[matchWindowID]["selections"][authorID] = False
                matches[matchWindowID]["selections"][opponents[authorID]] = False
                matchWindowObj = matches[matchWindowID]["messageObj"]
                p1ID = authorID
                p1name = str(client.get_user(authorID))
                p2ID = opponents[authorID]
                p2name = str(client.get_user(p2ID))
                chara1 = matches[matchWindowID]["players"][p1ID]["character"]
                chara2 = matches[matchWindowID]["players"][p2ID]["character"]
                firstStrike = random.choice([p1ID, p2ID])
                matches[matchWindowID]["banning"] = firstStrike
                stagelist = matches[matchWindowID]["stages"]
                newEmbed = matchWindowObj.embeds[0]
                heading = f"({p1name[:-5]}) {chara1} {versus} {chara2} ({p2name[:-5]})\n"
                matches[matchWindowID]["heading"] = heading
                newEmbed.set_field_at(0, name=f"Game 1",
                                      value=f"{heading}"
                                            f"\n"
                                            f"Waiting for <@{firstStrike}> to strike. (click on the reactions):\n"
                                            f"{showstagelist(stagelist)}",
                                      inline=False)
                await matchWindowObj.edit(embed=newEmbed)
                for icon in stages:
                    await matchWindowObj.add_reaction(icon)

                #print("checking for who's banning: ", matches[matchWindowID])

        # event for character selections game 2 and onwards
        elif matches[matchWindowID]['gameCount'] >= 2:
          if matches[matchWindowID]['winsNeeded'] == 3:
            selection = str(message.content.lower().strip())

            if selection in brawlChara.keys():
                matches[matchWindowID]['players'][authorID]['character'] = brawlChara[selection]
                
            opponentDM = client.get_user(authorID)
            playerDM = client.get_user(opponents[authorID])
            selectedDM = await opponentDM.create_dm()
            selectedChara = discord.Embed(title=f"{matches[matchWindowID]['players'][authorID]['character']} selected!",
                                          description=f"Return to matchmaking: Click here -> {matchchannel}",
                                          color=defaultColor)
            selectedChara.set_thumbnail(
                url="https://cdn.discordapp.com/emojis/818715531954880543.webp?size=160&quality=lossless"
            )
            await selectedDM.send(embed=selectedChara)

            # if the winner is selecting their character
            if matches[matchWindowID]["heading"] == "N/A":
                matches[matchWindowID]["selections"][authorID] = False
                matches[matchWindowID]["selections"][opponents[authorID]] = True
                p1name = str(client.get_user(authorID))
                chara1 = matches[matchWindowID]['players'][authorID]['character']
                matches[matchWindowID]["heading"] = f"({p1name[:-5]}) {chara1} {versus} "
                # print(matches[matchWindowID]["heading"])  # testing
                stage = matches[matchWindowID]["stages"][0]
                stageName = emotes2stage[stage]

                playerCharacter = matches[matchWindowID]['players'][authorID]['character']
                gameCount = matches[matchWindowID]['gameCount']
                selectDM = await playerDM.create_dm()
                charaSelect = discord.Embed(title=f"[Game {gameCount} | {stage} {stageName}]",
                                            description=f"{opponentDM} is going {playerCharacter}.\n"
                                                        f"Choose your character for Game {gameCount}! \n Type out what character you will use.\n"
                                                        f"If you're staying on the same character, type ''stay''.\n"
                                                        f"\n"
                                                        f"If you're having trouble selecting a character, type ``-characters``",
      
                                            color=defaultColor)
                charaSelect.set_thumbnail(
                    url="https://cdn.discordapp.com/emojis/919693698093183036.webp?size=160&quality=lossless")
                await selectDM.send(embed=charaSelect)

            # if the loser is selecting their character
            elif matches[matchWindowID]["heading"] != "N/A":
                matches[matchWindowID]["selections"][authorID] = False
                p2name = str(client.get_user(authorID))
                chara2 = matches[matchWindowID]['players'][authorID]['character']
                matches[matchWindowID]["heading"] += f"{chara2} ({p2name[:-5]})\n"
                # print(matches[matchWindowID]["heading"])  # testing

                matchWindowObj = matches[matchWindowID]["messageObj"]
                embedCount = matches[matchWindowID]["gameCount"] - 1
                newEmbed = matchWindowObj.embeds[0]
                newEmbed.set_field_at(embedCount,
                                      name=f"Game {matches[matchWindowID]['gameCount']}",
                                      value=f"{matches[matchWindowID]['heading']}"
                                            f"Stage:\n"
                                            f"{matches[matchWindowID]['stages'][0]} {emotes2stage[matches[matchWindowID]['stages'][0]]} \n",
                                      inline=False
                                      )
                await matchWindowObj.edit(embed=newEmbed)
                for icon in winloss:
                    await matchWindowObj.add_reaction(icon)

          elif matches[matchWindowID]['winsNeeded'] == 2:
            selection = str(message.content.lower().strip())
            if selection in brawlChara.keys():
                matches[matchWindowID]['players'][authorID]['character'] = brawlChara[selection]

            # elif selection == "stay":
            # print("nothing changes")

            playerDM = client.get_user(authorID)
            opponentDM = client.get_user(opponents[authorID])
            selectedDM = await playerDM.create_dm()
            selectedChara = discord.Embed(title=f"{matches[matchWindowID]['players'][authorID]['character']} selected!",
                                          description=f"Return to matchmaking: Click here -> {matchchannel}",
                                          color=defaultColor)
            selectedChara.set_thumbnail(
                url="https://cdn.discordapp.com/emojis/818715531954880543.webp?size=160&quality=lossless"
            )
            await selectedDM.send(embed=selectedChara)

            # if the winner is selecting their character
            if matches[matchWindowID]["heading"] == "N/A":
                matches[matchWindowID]["selections"][authorID] = False
                matches[matchWindowID]["selections"][opponents[authorID]] = True
                p1name = str(client.get_user(authorID))
                chara1 = matches[matchWindowID]['players'][authorID]['character']
                matches[matchWindowID]["heading"] = f"({p1name[:-5]}) {chara1} {versus} "
                # print(matches[matchWindowID]["heading"])  # testing
                stage = matches[matchWindowID]["stages"][0]
                stageName = emotes2stage[stage]

                playerCharacter = matches[matchWindowID]['players'][authorID]['character']
                gameCount = matches[matchWindowID]['gameCount']
                selectDM = await opponentDM.create_dm()
                charaSelect = discord.Embed(title=f"[Game {gameCount} | {stage} {stageName}]",
                                            description=f"{playerDM} is going {playerCharacter}.\n"
                                                        f"Choose your character for Game {gameCount}! \n Type out what character you will use.\n"
                                                        f"If you're staying on the same character, type ''stay''.\n"
                                                        f"\n"
                                                        f"If you're having trouble selecting a character, type ``-characters``",
      
                                            color=defaultColor)
                charaSelect.set_thumbnail(
                    url="https://cdn.discordapp.com/emojis/919693698093183036.webp?size=160&quality=lossless")
                await selectDM.send(embed=charaSelect)

            # if the loser is selecting their character
            elif matches[matchWindowID]["heading"] != "N/A":
                matches[matchWindowID]["selections"][authorID] = False
                p2name = str(client.get_user(authorID))
                chara2 = matches[matchWindowID]['players'][authorID]['character']
                matches[matchWindowID]["heading"] += f"{chara2} ({p2name[:-5]})\n"
                # print(matches[matchWindowID]["heading"])  # testing

                matchWindowObj = matches[matchWindowID]["messageObj"]
                embedCount = matches[matchWindowID]["gameCount"] - 1
                newEmbed = matchWindowObj.embeds[0]
                newEmbed.set_field_at(embedCount,
                                      name=f"Game {matches[matchWindowID]['gameCount']}",
                                      value=f"{matches[matchWindowID]['heading']}"
                                            f"Stage:\n"
                                            f"{matches[matchWindowID]['stages'][0]} {emotes2stage[matches[matchWindowID]['stages'][0]]} \n",
                                      inline=False
                                      )
                await matchWindowObj.edit(embed=newEmbed)
                for icon in winloss:
                    await matchWindowObj.add_reaction(icon)

client.run(my_secret)



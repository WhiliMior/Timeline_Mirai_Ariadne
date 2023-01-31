# 所有指令的指示符
headers = '([.]|[。])'
# 所有机器人控制指令的正则
BotControl = '^(\\[(.*?)\\]\\s)?([.]|[。])bot.*'
Dismiss = '^(\\[(.*?)\\]\\s)?([.]|[。])dismiss.*'
Help = '^([.]|[。])help.*'

# 所有游戏指令, (?i)忽略大小写
CharacterCreate = f'^{headers}TLsetup?.*'
CharacterManage = f'^{headers}ch[r]?'
Target = f'^{headers}ta[r]?'
Buff = f'^{headers}bu[f]?[f]?'
WeaponCreate = f'^{headers}WPsetup'
Examination = f'^{headers}ex'
Negotiation = '^([.]|[。])ne[g]?.*'
PreparationCheck = '^([.]|[。])pr[e]?.*'
Battle = r'^(^([.]|[。])ba[t]?)'
Record = '^([.]|[。])crd?.*'

# 骰子
RollDice = '^([.]|[。])[r].*'
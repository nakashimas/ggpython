
<p>
    <div align="center">
    <h1>ggpython sample</h1>
    </div>
</p>

<h2> Contents </h2>

- [Description](#description)
- [Valorant](#valorant)
- [Development](#development)

## Description

ggpythonの使用方法を掲載しています。

## Valorant

Valorantのマッチリザルトを取得できる。(最大20件)

```py
from ggpython import GGTrackerAPI, GAME

with GGTrackerAPI(GAME.VALORANT) as gg:
    res = gg.get_match_result("Username", "#tag", mode = "unrated")
```

Discord Bot用に出力結果を整形できる。(調整中)

サンプル: 

```py
print(convert_valorant_match_to_discord(res))
# -> to paste discord plane text
```

結果: 

<p style="text-align:center;">
  <img src="https://github.com/nakashimas/ggpython/blob/master/img/discord_1.png?raw=true" style="width:60%"/>
</p>

Discordサーバに絵文字を登録しておく必要がある

## Development

編集中

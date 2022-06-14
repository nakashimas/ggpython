
<p>
    <div align="center">
    <h1>ggpython sample</h1>
    </div>
</p>

<h2> Contents </h2>

- [Description](#description)
- [Valorant](#valorant)
- [Development](#development)
  - [Branch](#branch)
  - [Class And Method Definition](#class-and-method-definition)

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

### Branch

*Master Branch*

PyPI等に公開しているものと同じにする  
mainに変えるかは検討中

*Develop Branch*

現時点ではバージョンで分けない  
もし必要なら以下のように書く:

```
git checkout -b develop/[version]
```

*gh-pages Branch*

Document公開用  
`./docs/*`以下をsubmoduleとしている

*Feature Branch*

feature branchを利用する場合は、まず、Issueを投稿して  
以下のように書く:

```
git checkout -b [version]_#[issue_number]_[issue_title]
```

*Release Branch*

release branchは現時点では切らなくてもいい方針  
developに直接書く  
もし必要なら以下のように書く:

```
git checkout -b [version]_release_[issue_title]
```

この際のversionはreleaseで扱うものを指す

*Fix Branch*

hotfix branchは現時点では切らなくてもいい方針  
developかmasterに直接書く  
もし必要なら以下のように書く:

```
git checkout -b [version]_hotfix_[issue_title]
```

### Class And Method Definition

編集中


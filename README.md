
<p>
    <div align="center">
    <h1>ggpython</h1>
    </div>
</p>

<h4 align="center">Tracker Network Wrapper In Python.</h4>

<p align="center">
  <a>
    <img alt="AppVeyor badge" src="https://img.shields.io/badge/build-passing-brightgreen">
  </a>
  <a href = "https://github.com/nakashimas/ggpython/releases">
    <img src="https://img.shields.io/badge/releace-v0.0.0%20-58839b.svg?style=flat">
  </a>
  <a href="./LICENSE">
    <img src="http://img.shields.io/badge/license-MIT-blue.svg?style=flat">
  </a>
  <br>
  <a>
    <img src="https://img.shields.io/badge/platform-win--32%20%7C%20win--64-lightgrey">
  </a>
</p>

<h2> Contents </h2>

- [Description](#description)
- [Usage](#usage)
- [Installation](#installation)
- [License](#license)
- [Author](#author)

## Description

TrackerNetwork 非公式API。  
Discord bot 用に作成しているものをPythonライブラリとして管理している。

サポートしているゲーム

- Valorant

## Usage

Valorantのマッチリザルトを取得できる。(最大20件)

```py
import ggpython
valorant = ggpython.ValorantTrackerWebsiteAPI()
valorant.get_match_result_list("Username", "#tag", mode = "unrated")
```

Discord Bot用に出力結果を整形できる。(調整中)

サンプル: 

```py
import ggpython
valorant = ggpython.ValorantTrackerWebsiteAPI()
result_list = valorant.get_match_result_list("Username", "#tag", mode = "unrated")

print(ggpython.convert_valorant_match_to_discord(result_list))
# -> to paste discord plane text
```

結果: 

<p style="text-align:center;">
  <img src="https://github.com/nakashimas/ggpython/blob/master/img/discord_1.png?raw=true" style="width:60%"/>
</p>

Discordサーバに絵文字を登録しておく必要がある

## Installation

You can [Download](https://github.com/nakashimas/ggpython/releases) the latest installable version of _ggpython_ for Windows. (zip format)

for pip install :  

```py
pip install git+https://github.com/nakashimas/ggpython
```

## License

This project is licensed under the terms of the [MIT](./LICENSE).

このプロジェクトは [MIT](./LICENSE) ライセンスに基づいて管理されています。

## Author

_ggpython_ authors.

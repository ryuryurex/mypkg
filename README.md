# mypkg

[![test](https://github.com/ryuryurex/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/ryuryurex/mypkg/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/License-BSD--3--Clause-blue.svg)](https://github.com/ryuryurex/mypkg/blob/main/LICENSE)

## 概要
- ロボットシステム学の授業で使用したROS2パッケージです。
- [Open-Meteo API](https://open-meteo.com/)によって千葉県習志野市の天気情報を10秒ごとにweather_infoトピックにパブリッシュします。左から気温、風速、タイムスタンプで表示します。
- listener.pyおよび，talk_listen.launch.pyはテスト用です。

## ノード
- weather_publisher:
天気情報を10秒ごとに取得し、トピックにパブリッシュします。
## トピック
- weather_info:
ノードからパブリッシュされたデータ(気温(摂氏)、風速(km/h)、タイムスタンプ(YYYY-MM-DD HH:MM:SS))を持ちます。

## テスト環境
* Ubuntu 22.04 LTS
* ROS2 Humble 

## 開発環境
* ubuntu20.04 LTS
* ROS2 Foxy

## 使用方法
このコマンドで実行します。
```shell
$ ros2 run mypkg weather_publisher
```

トピックの内容はこのコマンドで確認できます。
```shell
$  ros2 topic echo weather_info
```
```shell
data: 3.3,8.5,2025-01-05 02:18:46
---
data: 3.3,8.5,2025-01-05 02:18:56
---
data: 3.3,8.5,2025-01-05 02:19:06
---
data: 3.3,8.5,2025-01-05 02:19:16
---
data: 3.3,8.5,2025-01-05 02:19:26
---
data: 3.3,8.5,2025-01-05 02:19:36
---
```

## LICENSE
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
* このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    * [ryuichiueda/slides_marp/tree/master/robosys_2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)

## Copyright
* © 2025 Ryusei Noda

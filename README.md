# ゲーム のタイトル
*タワーディフェンス系
## 実行環境の必要条件
* python >= 3.10
* pygame >= 2.1

## ゲームの概要
自陣と相手陣にタワーが存在する。
そこからそれぞれユニットを召喚して相手のタワーを攻撃する。
先に相手タワーのHPを削り切れれば勝利。

## ゲームの実装
###共通基本機能
* 自陣のタワーに関するクラス
* 敵陣のタワーに関するクラス
* 自分のユニットに関するクラス
* 敵ユニットに関するクラス
* 
### 担当追加機能
* 敵のユニット、城にぶつかると爆発する
### ToDo
- [ ] ユニットの種類を増やしたかった。
- [ ] 体力が分かりやすいようにゲージを表示させたかった。
### メモ
* pygame.spriteを使用してクラスの呼び出しを簡単にしている。
* クラス名はスネークケースで変数名はキャメルケースで記述するようにしている。
* すべてのクラスに関係する関数は，クラスの外で定義してある

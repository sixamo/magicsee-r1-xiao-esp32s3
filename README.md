# Magicsee R1 USB receiver for XIAO ESP32S3

Magicsee R1のM+B Bluetooth Low Energyモードを、Windows／Steamで使える
USBゲームコントローラーへ変換する非公式オープンソース受信機です。

Seeed Studio XIAO ESP32S3と付属外付けアンテナを使用します。2組の実機で、
別々のコントローラーとして認識することまで確認しています。

> This is an unofficial community project and is not affiliated with
> Magicsee, Seeed Studio, Valve, or the Joypad OS project.

## 動作仕様

- R1のジョイスティックをUSB左アナログスティックの固定4方向として出力
- 傾けている間は長押しを維持し、中立`0x50`またはBLE切断で解除
- 斜め補間は行わず、左上／右上の報告値は上として扱う
- USB製品名：`Magicsee R1`
- XIAO固有シリアルを維持するため、複数受信機を別デバイスとして識別可能

| R1 | USB/Steam |
|---|---|
| A | Y |
| B | B |
| C | X |
| D | A |
| ENTER | SELECT |
| RETURN | ENTER |

## 必要なもの

- Seeed Studio XIAO ESP32S3
- XIAO付属の外付け2.4 GHzアンテナ（接続必須）
- Magicsee R1
- データ通信対応USB-Cケーブル（書込み時）
- Windows 10/11 PC

任意のドングル化部品として、KOYOKOMA USB-Cオス–オスアダプタ
（Amazon ASIN `B0CZ9HRKK4`）向けのケース試作データも収録しています。

## 書込み

最も簡単な方法は、[Releases](https://github.com/sixamo/magicsee-r1-xiao-esp32s3/releases)からWindows書込みキットを取得し、
展開後に`FLASH-MAGICSEE-R1.bat`を実行することです。

1. XIAOの`B`を押したまま`R`を短く押す。
2. 1秒待って`B`を離す。
3. スクリプトがEspressif書込みポートを自動検出して書き込む。
4. 完了後10秒待ち、XIAOの`B`を1回短く押す。
5. R1の`M+B`を長押しし、LEDが高速点滅したら接続を待つ。

書込みイメージを直接使う場合は、
`firmware/Magicsee-R1-XIAO-ESP32S3-v1.0.1.merged.bin`をESP32-S3の
アドレス`0x0`へ書き込みます。

```powershell
esptool --chip esp32s3 --port COM4 --baud 460800 write-flash 0x0 `
  firmware/Magicsee-R1-XIAO-ESP32S3-v1.0.1.merged.bin
```

## ソースからの再現

本ファームウェアは[Joypad OS](https://github.com/joypad-ai/joypad-os)を基に
Magicsee R1ドライバーを追加したものです。

```bash
git clone https://github.com/joypad-ai/joypad-os.git
cd joypad-os
git checkout 9fa79f4
git apply ../magicsee-r1-xiao-esp32s3/patches/magicsee-r1.patch
```

その後、Joypad OSのESP32-S3/XIAOビルド手順で`bt2usb`をビルドします。
基準コミットと変更ファイルは`NOTICE`にも記載しています。

## 3Dケース

`hardware/case/`には以下があります。

- ケース底面／蓋STL
- アダプタ嵌合確認用ゲージSTL
- パラメトリックOpenSCADデータ
- STL生成用Pythonソース

ケースはアダプタ実物到着前の公称寸法から作った**試し刷り版**です。
最初に小型の嵌合ゲージを印刷してください。ケースの実物適合確認後に正式版へ
更新します。

## 確認済み環境

- Seeed Studio XIAO ESP32S3 × 2
- Magicsee R1 × 2
- Windows 11
- Steam controller test
- BLE接続、全6ボタン、4方向長押し、中立解除、複数受信機の個別認識

## 既知の制約

- R1のM+Bモードは、連続回転中にも物理的な中立と同じ`0x50`を送るため、
  円を描くような連続回転や下側の斜め入力は正確に復元できません。
- 本版は誤入力や中立復帰の遅延を避けるため、受信した上下左右と中立を
  そのままUSB左アナログスティックへ変換します。単独の4方向操作を想定しています。
- 中立解除の時刻は、R1から`0x50`が届く時刻に依存します。

## ライセンス

Joypad OSおよび本リポジトリの派生コードはApache License 2.0です。
同梱するEspressif esptoolのライセンスとソース情報は
`THIRD_PARTY_NOTICES.md`を参照してください。

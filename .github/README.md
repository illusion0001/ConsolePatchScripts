# ConsolePatchScripts
Scripts for creating Game Patches from reverse engineering tools.

## Features
- Easily generate patch codes for emulator and console games.
- Supports:
  - PS3 ([RPCS3 Game Patches](https://wiki.rpcs3.net/index.php?title=Help:Game_Patches#Standard_format))
  - PS4 ([py-patch](https://github.com/illusion0001/py-patcher/blob/main/data/example.yml))
  - Xbox 360 ([Xenia Game Patches](https://github.com/xenia-canary/game-patches))
- Note that PS4 must have the address base set to `0x400000` to match disabled ASLR address.

## Usage
- Download the [extension](https://github.com/illusion0001/ConsolePatchScripts/releases/latest), install it and enable the script.
- Highlight your desired code and press `Alt-Shift-Q` to generate code.

![](https://user-images.githubusercontent.com/37698908/159830228-7063bf0f-d0b7-457c-81a1-6f717a975913.png)

<details>
<summary>Image guide (Click to Expand)</summary>

![](https://user-images.githubusercontent.com/37698908/159781314-da756466-ff39-48ac-92d9-9fdb15b4c48d.png)

</details>

# Todo
- [ ] Auto detect float data types
- [ ] IDA support

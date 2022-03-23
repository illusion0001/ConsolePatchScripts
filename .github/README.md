# ConsolePatchScripts
Scripts for creating Game Patches from reverse engineering tools. (Ghidra)

## Features
- Easily generate patch codes for emulator and console games.
- Supports:
  - PS3 ([RPCS3 Game Patches](https://wiki.rpcs3.net/index.php?title=Help:Game_Patches#Standard_format))
  - PS4 ([py-patch](https://github.com/illusion0001/py-patcher/blob/main/data/example.yml))
  - Xbox 360 ([Xenia Game Patches](https://github.com/xenia-canary/game-patches))
- Note that PS4 must have the address base set to `0x400000`, to match disabled ASLR address.

## Usage
- Install like any other extension and enable the script.
- Highlight your desired code and press `Alt+Shift+Q` to generate code.

![](https://user-images.githubusercontent.com/37698908/159781314-da756466-ff39-48ac-92d9-9fdb15b4c48d.png)

# Todo
- [ ] Auto detect float data types
- [ ] IDA support

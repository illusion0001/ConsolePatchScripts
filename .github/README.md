# ConsolePatchScripts
Reverse engineering tool scripts for Console Game Patches.

## Features
- Easily generate patch codes for emulator and console games.
- Supported platform and formats: PS3 ([RPCS3 Game Patches](https://wiki.rpcs3.net/index.php?title=Help:Game_Patches#Standard_format)), PS4 ([py-patch](https://github.com/illusion0001/py-patcher)), Xbox 360 ([Xenia Game Patches](https://github.com/xenia-canary/game-patches))
- Note that PS4 must have the address base set to 0x400000, to match disabled ASLR address.

## Usage
[Download](../../../archive/refs/heads/main.zip) and add the `ghidra_scripts` folder.

![image](https://user-images.githubusercontent.com/37698908/159603660-adeb579e-051c-4369-b5dd-54a0b1fb210b.png)

# Todo
- [ ] Auto detect float data types
- [ ] IDA support

A lot of points say 0 points so will figure out how to fix that later but the main ones that give points are listed. Idk was a dumb way of scraping points data, looked at scoreboard URL for each room and took second persons results as more points for first blood. 
```https://tryhackme.com/api/v2/rooms/scoreboard?roomCode={room_code}&limit=10```

1. It takes Ryans (0days completed rooms as he has done them all) to get a list of room codes.
2. It requests each rooms leaderboard API to find the points for each. 


| Room Name                      | Room URL                                                  |   Points |
|:-------------------------------|:----------------------------------------------------------|---------:|
| Advent of Cyber 1 [2019]       | https://tryhackme.com/room/25daysofchristmas              |     2160 |
| Introductory Networking        | https://tryhackme.com/room/introtonetworking              |     1320 |
| Squid Game                     | https://tryhackme.com/room/squidgameroom                  |     1230 |
| Advent of Cyber 2023           | https://tryhackme.com/room/adventofcyber2023              |     1104 |
| Advent of Cyber 3 (2021)       | https://tryhackme.com/room/adventofcyber3                 |     1064 |
| Toolbox: Vim                   | https://tryhackme.com/room/toolboxvim                     |     1050 |
| Advent of Cyber 2022           | https://tryhackme.com/room/adventofcyber4                 |     1040 |
| Attacktive Directory           | https://tryhackme.com/room/attacktivedirectory            |     1040 |
| GoldenEye                      | https://tryhackme.com/room/goldeneye                      |     1020 |
| Enumerating Active Directory   | https://tryhackme.com/room/adenumeration                  |     1010 |
| Advent of Cyber 2 [2020]       | https://tryhackme.com/room/adventofcyber2                 |      912 |
| 25 Days of Cyber Security      | https://tryhackme.com/room/learncyberin25days             |      904 |
| Investigating Windows 2.0      | https://tryhackme.com/room/investigatingwindows2          |      900 |
| Investigating Windows 3.x      | https://tryhackme.com/room/investigatingwindows3          |      900 |
| Investigating Windows          | https://tryhackme.com/room/investigatingwindows           |      830 |
| tomghost                       | https://tryhackme.com/room/tomghost                       |      810 |
| Linux Agency                   | https://tryhackme.com/room/linuxagency                    |      798 |
| Borderlands                    | https://tryhackme.com/room/borderlands                    |      750 |
| CyberCrafted                   | https://tryhackme.com/room/cybercrafted                   |      730 |
| Biohazard                      | https://tryhackme.com/room/biohazard                      |      730 |
| WebOSINT                       | https://tryhackme.com/room/webosint                       |      720 |
| NahamStore                     | https://tryhackme.com/room/nahamstore                     |      720 |
| Masterminds                    | https://tryhackme.com/room/mastermindsxlq                 |      690 |
| Ice                            | https://tryhackme.com/room/ice                            |      690 |
| Agent Sudo                     | https://tryhackme.com/room/agentsudoctf                   |      690 |
| Retro                          | https://tryhackme.com/room/retro                          |      690 |
| MAL: Malware Introductory      | https://tryhackme.com/room/malmalintroductory             |      660 |
| Searchlight - IMINT            | https://tryhackme.com/room/searchlightosint               |      660 |
| Dumping Router Firmware        | https://tryhackme.com/room/rfirmware                      |      660 |
| REvil Corp                     | https://tryhackme.com/room/revilcorp                      |      650 |
| Blue                           | https://tryhackme.com/room/blue                           |      630 |
| c4ptur3-th3-fl4g               | https://tryhackme.com/room/c4ptur3th3fl4g                 |      620 |
| Couch                          | https://tryhackme.com/room/couch                          |      620 |
| Wreath                         | https://tryhackme.com/room/wreath                         |      616 |
| CTF collection Vol.2           | https://tryhackme.com/room/ctfcollectionvol2              |      600 |
| CTF collection Vol.1           | https://tryhackme.com/room/ctfcollectionvol1              |      600 |
| Carnage                        | https://tryhackme.com/room/c2carnage                      |      600 |
| Brute It                       | https://tryhackme.com/room/bruteit                        |      580 |
| Easy Peasy                     | https://tryhackme.com/room/easypeasyctf                   |      580 |
| Anthem                         | https://tryhackme.com/room/anthem                         |      570 |
| Crack The Hash Level 2         | https://tryhackme.com/room/crackthehashlevel2             |      570 |
| Mobile Malware Analysis        | https://tryhackme.com/room/mma                            |      540 |
| Network Services 2             | https://tryhackme.com/room/networkservices2               |      536 |
| Tokyo Ghoul                    | https://tryhackme.com/room/tokyoghoul666                  |      520 |
| Poster                         | https://tryhackme.com/room/poster                         |      510 |
| tmux                           | https://tryhackme.com/room/rptmux                         |      510 |
| Boiler CTF                     | https://tryhackme.com/room/boilerctf2                     |      500 |
| JVM Reverse Engineering        | https://tryhackme.com/room/jvmreverseengineering          |      500 |
| Wifi Hacking 101               | https://tryhackme.com/room/wifihacking101                 |      480 |
| REmux The Tmux                 | https://tryhackme.com/room/tmuxremux                      |      480 |
| Sakura Room                    | https://tryhackme.com/room/sakura                         |      450 |
| Google Dorking                 | https://tryhackme.com/room/googledorking                  |      450 |
| Jupyter 101                    | https://tryhackme.com/room/jupyter101                     |      450 |
| HA Joker CTF                   | https://tryhackme.com/room/jokerctf                       |      450 |
| Disk Analysis & Autopsy        | https://tryhackme.com/room/autopsy2ze0                    |      450 |
| Fowsniff CTF                   | https://tryhackme.com/room/ctf                            |      450 |
| Learn Rust                     | https://tryhackme.com/room/rust                           |      440 |
| h4cked                         | https://tryhackme.com/room/h4cked                         |      420 |
| Physical Security Intro        | https://tryhackme.com/room/physicalsecurityintro          |      404 |
| Mnemonic                       | https://tryhackme.com/room/mnemonic                       |      400 |
| Dunkle Materie                 | https://tryhackme.com/room/dunklematerieptxc9             |      400 |
| The Cod Caper                  | https://tryhackme.com/room/thecodcaper                    |      390 |
| RazorBlack                     | https://tryhackme.com/room/raz0rblack                     |      380 |
| Juicy Details                  | https://tryhackme.com/room/juicydetails                   |      360 |
| CMSpit                         | https://tryhackme.com/room/cmspit                         |      360 |
| Forensics                      | https://tryhackme.com/room/forensics                      |      360 |
| RootMe                         | https://tryhackme.com/room/rrootme                        |      360 |
| Break it                       | https://tryhackme.com/room/breakit                        |      360 |
| Recovery                       | https://tryhackme.com/room/recovery                       |      355 |
| Network Services               | https://tryhackme.com/room/networkservices                |      344 |
| Wordpress: CVE-2021-29447      | https://tryhackme.com/room/wordpresscve202129447          |      340 |
| OWASP Top 10                   | https://tryhackme.com/room/owasptop10                     |      336 |
| dogcat                         | https://tryhackme.com/room/dogcat                         |      335 |
| Reversing ELF                  | https://tryhackme.com/room/reverselfiles                  |      320 |
| Nmap                           | https://tryhackme.com/room/furthernmap                    |      320 |
| New York Flankees              | https://tryhackme.com/room/thenewyorkflankees             |      320 |
| History of Malware             | https://tryhackme.com/room/historyofmalware               |      312 |
| Year of the Rabbit             | https://tryhackme.com/room/yearoftherabbit                |      310 |
| Simple CTF                     | https://tryhackme.com/room/easyctf                        |      300 |
| Conti                          | https://tryhackme.com/room/contiransomwarehgh             |      300 |
| PWN101                         | https://tryhackme.com/room/pwn101                         |      300 |
| M4tr1x: Exit Denied            | https://tryhackme.com/room/m4tr1xexitdenied               |      300 |
| hackerNote                     | https://tryhackme.com/room/hackernote                     |      300 |
| Linux Modules                  | https://tryhackme.com/room/linuxmodules                   |      296 |
| Brute Force Heroes             | https://tryhackme.com/room/bruteforceheroes               |      280 |
| Redline                        | https://tryhackme.com/room/btredlinejoxr3d                |      280 |
| Anonymous                      | https://tryhackme.com/room/anonymous                      |      280 |
| Lunizz CTF                     | https://tryhackme.com/room/lunizzctfnd                    |      280 |
| Hacking Hadoop                 | https://tryhackme.com/room/hackinghadoop                  |      276 |
| Digital Forensics Case B4DM755 | https://tryhackme.com/room/caseb4dm755                    |      272 |
| Linux Strength Training        | https://tryhackme.com/room/linuxstrengthtraining          |      272 |
| Crack the hash                 | https://tryhackme.com/room/crackthehash                   |      270 |
| UltraTech                      | https://tryhackme.com/room/ultratech1                     |      270 |
| One Piece                      | https://tryhackme.com/room/ctfonepiece65                  |      270 |
| Badbyte                        | https://tryhackme.com/room/badbyte                        |      264 |
| OhSINT                         | https://tryhackme.com/room/ohsint                         |      260 |
| Daily Bugle                    | https://tryhackme.com/room/dailybugle                     |      250 |
| broker                         | https://tryhackme.com/room/broker                         |      250 |
| Chrome                         | https://tryhackme.com/room/chrome                         |      250 |
| SQHell                         | https://tryhackme.com/room/sqhell                         |      250 |
| L2 MAC Flooding & ARP Spoofing | https://tryhackme.com/room/layer2                         |      248 |
| Pickle Rick                    | https://tryhackme.com/room/picklerick                     |      240 |
| Nax                            | https://tryhackme.com/room/nax                            |      240 |
| Android Hacking 101            | https://tryhackme.com/room/androidhacking101              |      240 |
| Sweettooth Inc.                | https://tryhackme.com/room/sweettoothinc                  |      240 |
| Tony the Tiger                 | https://tryhackme.com/room/tonythetiger                   |      240 |
| Ra                             | https://tryhackme.com/room/ra                             |      240 |
| Snort                          | https://tryhackme.com/room/snort                          |      232 |
| Regular expressions            | https://tryhackme.com/room/catregex                       |      232 |
| Block                          | https://tryhackme.com/room/blockroom                      |      230 |
| REloaded                       | https://tryhackme.com/room/reloaded                       |      230 |
| kiba                           | https://tryhackme.com/room/kiba                           |      230 |
| Sustah                         | https://tryhackme.com/room/sustah                         |      230 |
| Windows Incident Surface       | https://tryhackme.com/room/winincidentsurface             |      224 |
| VulnNet: Internal              | https://tryhackme.com/room/vulnnetinternal                |      220 |
| Windows Forensics 1            | https://tryhackme.com/room/windowsforensics1              |      216 |
| Vulnversity                    | https://tryhackme.com/room/vulnversity                    |      214 |
| Watcher                        | https://tryhackme.com/room/watcher                        |      210 |
| Archangel                      | https://tryhackme.com/room/archangel                      |      210 |
| Hamlet                         | https://tryhackme.com/room/hamlet                         |      210 |
| Unstable Twin                  | https://tryhackme.com/room/unstabletwin                   |      210 |
| Linux Privilege Escalation     | https://tryhackme.com/room/linprivesc                     |      208 |
| OWASP Top 10 - 2021            | https://tryhackme.com/room/owasptop102021                 |      208 |
| Shodan.io                      | https://tryhackme.com/room/shodan                         |      204 |
| Binary Heaven                  | https://tryhackme.com/room/binaryheaven                   |      200 |
| Kubernetes for Everyone        | https://tryhackme.com/room/kubernetesforyouly             |      200 |
| APIWizards Breach              | https://tryhackme.com/room/apiwizardsbreach               |      200 |
| Identity and Access Management | https://tryhackme.com/room/iaaaidm                        |      192 |
| Blaster                        | https://tryhackme.com/room/blaster                        |      192 |
| PrintNightmare                 | https://tryhackme.com/room/printnightmarehpzqlp8          |      184 |
| Intro To Pwntools              | https://tryhackme.com/room/introtopwntools                |      184 |
| Hip Flask                      | https://tryhackme.com/room/hipflask                       |      182 |
| Advent of Cyber '23 Side Quest | https://tryhackme.com/room/adventofcyber23sidequest       |      180 |
| Basic Pentesting               | https://tryhackme.com/room/basicpentestingjt              |      180 |
| Clocky                         | https://tryhackme.com/room/clocky                         |      180 |
| Bash Scripting                 | https://tryhackme.com/room/bashscripting                  |      180 |
| Uranium CTF                    | https://tryhackme.com/room/uranium                        |      180 |
| TryHack3M: Bricks Heist        | https://tryhackme.com/room/tryhack3mbricksheist           |      180 |
| Ninja Skills                   | https://tryhackme.com/room/ninjaskills                    |      180 |
| Breaking RSA                   | https://tryhackme.com/room/breakrsa                       |      180 |
| Profiles                       | https://tryhackme.com/room/profilesroom                   |      180 |
| Lian_Yu                        | https://tryhackme.com/room/lianyu                         |      180 |
| CCT2019                        | https://tryhackme.com/room/cct2019                        |      180 |
| Introduction to Windows API    | https://tryhackme.com/room/windowsapi                     |      176 |
| HTTP in Detail                 | https://tryhackme.com/room/httpindetail                   |      176 |
| pyLon                          | https://tryhackme.com/room/pylonzf                        |      170 |
| ConvertMyVideo                 | https://tryhackme.com/room/convertmyvideo                 |      170 |
| PalsForLife                    | https://tryhackme.com/room/palsforlife                    |      170 |
| Theseus                        | https://tryhackme.com/room/theseus                        |      170 |
| Ghizer                         | https://tryhackme.com/room/ghizerctf                      |      170 |
| Crylo                          | https://tryhackme.com/room/crylo4a                        |      168 |
| Misguided Ghosts               | https://tryhackme.com/room/misguidedghosts                |      160 |
| XSS                            | https://tryhackme.com/room/axss                           |      160 |
| Breaching Active Directory     | https://tryhackme.com/room/breachingad                    |      160 |
| Buffer Overflow Prep           | https://tryhackme.com/room/bufferoverflowprep             |      160 |
| CSRF                           | https://tryhackme.com/room/csrfV2                         |      160 |
| Intro to Pipeline Automation   | https://tryhackme.com/room/introtopipelineautomation      |      160 |
| VulnNet: dotjar                | https://tryhackme.com/room/vulnnetdotjar                  |      160 |
| Relevant                       | https://tryhackme.com/room/relevant                       |      160 |
| Rocket                         | https://tryhackme.com/room/rocket                         |      160 |
| Psycho Break                   | https://tryhackme.com/room/psychobreak                    |      160 |
| Year of the Dog                | https://tryhackme.com/room/yearofthedog                   |      160 |
| Looking Glass                  | https://tryhackme.com/room/lookingglass                   |      160 |
| Intro to Docker                | https://tryhackme.com/room/introtodockerk8pdqk            |      160 |
| ISO27001                       | https://tryhackme.com/room/iso27001                       |      160 |
| VulnNet                        | https://tryhackme.com/room/vulnnet1                       |      160 |
| Jax sucks alot.............    | https://tryhackme.com/room/jason                          |      160 |
| Nmap Live Host Discovery       | https://tryhackme.com/room/nmap01                         |      160 |
| KAPE                           | https://tryhackme.com/room/kape                           |      160 |
| Linux Server Forensics         | https://tryhackme.com/room/linuxserverforensics           |      156 |
| Introduction to DevSecOps      | https://tryhackme.com/room/introductiontodevsecops        |      152 |
| SSDLC                          | https://tryhackme.com/room/securesdlc                     |      152 |
| Threat Intelligence Tools      | https://tryhackme.com/room/threatinteltools               |      152 |
| ffuf                           | https://tryhackme.com/room/ffuf                           |      152 |
| Adventure Time                 | https://tryhackme.com/room/adventuretime                  |      150 |
| Gallery                        | https://tryhackme.com/room/gallery666                     |      150 |
| Crocc Crew                     | https://tryhackme.com/room/crocccrew                      |      150 |
| Bounty Hacker                  | https://tryhackme.com/room/cowboyhacker                   |      150 |
| Cyborg                         | https://tryhackme.com/room/cyborgt8                       |      150 |
| Cooctus Stories                | https://tryhackme.com/room/cooctusadventures              |      150 |
| Blog                           | https://tryhackme.com/room/blog                           |      150 |
| The Return of the Yeti         | https://tryhackme.com/room/adv3nt0fdbopsjcap              |      150 |
| Frosteau Busy with Vim         | https://tryhackme.com/room/busyvimfrosteau                |      150 |
| Different CTF                  | https://tryhackme.com/room/adana                          |      150 |
| Dave's Blog                    | https://tryhackme.com/room/davesblog                      |      150 |
| Super-Spam                     | https://tryhackme.com/room/superspamr                     |      150 |
| DNS Manipulation               | https://tryhackme.com/room/dnsmanipulation                |      148 |
| OWASP Broken Access Control    | https://tryhackme.com/room/owaspbrokenaccesscontrol       |      144 |
| KaffeeSec - SoMeSINT           | https://tryhackme.com/room/somesint                       |      144 |
| Unified Kill Chain             | https://tryhackme.com/room/unifiedkillchain               |      144 |
| Intrusion Detection            | https://tryhackme.com/room/idsevasion                     |      144 |
| Servidae: Log Analysis in ELK  | https://tryhackme.com/room/servidae                       |      144 |
| Red Team Engagements           | https://tryhackme.com/room/redteamengagements             |      144 |
| K8s Runtime Security           | https://tryhackme.com/room/k8sruntimesecurity             |      144 |
| Intro to Log Analysis          | https://tryhackme.com/room/introtologanalysis             |      144 |
| Backtrack                      | https://tryhackme.com/room/backtrack                      |      140 |
| Frank & Herby make an app      | https://tryhackme.com/room/frankandherby                  |      140 |
| Startup                        | https://tryhackme.com/room/startup                        |      140 |
| CMesS                          | https://tryhackme.com/room/cmess                          |      140 |
| Obscure                        | https://tryhackme.com/room/obscured                       |      140 |
| Year of the Pig                | https://tryhackme.com/room/yearofthepig                   |      140 |
| CERTain Doom                   | https://tryhackme.com/room/certaindoom                    |      140 |
| Revenge                        | https://tryhackme.com/room/revenge                        |      140 |
| For Business Reasons           | https://tryhackme.com/room/forbusinessreasons             |      140 |
| Madeye's Castle                | https://tryhackme.com/room/madeyescastle                  |      140 |
| envizon                        | https://tryhackme.com/room/envizon                        |      140 |
| Nessus                         | https://tryhackme.com/room/rpnessusredux                  |      136 |
| Pyramid Of Pain                | https://tryhackme.com/room/pyramidofpainax                |      136 |
| Splunk: Exploring SPL          | https://tryhackme.com/room/splunkexploringspl             |      136 |
| Expediting Registry Analysis   | https://tryhackme.com/room/expregistryforensics           |      136 |
| Attacking ICS Plant #1         | https://tryhackme.com/room/attackingics1                  |      136 |
| Registry Persistence Detection | https://tryhackme.com/room/registrypersistencedetection   |      136 |
| OWASP Juice Shop               | https://tryhackme.com/room/owaspjuiceshop                 |      136 |
| MAL: Researching               | https://tryhackme.com/room/malresearching                 |      136 |
| Cluster Hardening              | https://tryhackme.com/room/clusterhardening               |      136 |
| Overpass 2 - Hacked            | https://tryhackme.com/room/overpass2hacked                |      131 |
| Introduction To Honeypots      | https://tryhackme.com/room/introductiontohoneypots        |      128 |
| Threat Hunting: Introduction   | https://tryhackme.com/room/introductiontothreathunting    |      128 |
| Active Directory Basics        | https://tryhackme.com/room/winadbasics                    |      128 |
| Follina MSDT                   | https://tryhackme.com/room/follinamsdt                    |      128 |
| Wazuh                          | https://tryhackme.com/room/wazuhct                        |      128 |
| TryHack3M: Sch3Ma D3Mon        | https://tryhackme.com/room/sch3mad3mon                    |      124 |
| Encryption - Crypto 101        | https://tryhackme.com/room/encryptioncrypto101            |      120 |
| b3dr0ck                        | https://tryhackme.com/room/b3dr0ck                        |      120 |
| Year of the Fox                | https://tryhackme.com/room/yotf                           |      120 |
| Introduction to CryptOps       | https://tryhackme.com/room/introductiontocryptops         |      120 |
| Introduction to Cryptography   | https://tryhackme.com/room/cryptographyintro              |      120 |
| Windows x64 Assembly           | https://tryhackme.com/room/win64assembly                  |      120 |
| Windows Fundamentals 2         | https://tryhackme.com/room/windowsfundamentals2x0x        |      120 |
| Geolocating Images             | https://tryhackme.com/room/geolocatingimages              |      120 |
| Advanced SQL Injection         | https://tryhackme.com/room/advancedsqlinjection           |      120 |
| Memory Forensics               | https://tryhackme.com/room/memoryforensics                |      120 |
| Phishing: HiddenEye            | https://tryhackme.com/room/phishinghiddeneye              |      120 |
| Android Malware Analysis       | https://tryhackme.com/room/androidmalwareanalysis         |      120 |
| K8s Best Security Practices    | https://tryhackme.com/room/k8sbestsecuritypractices       |      120 |
| You're in a cave               | https://tryhackme.com/room/inacave                        |      120 |
| Minotaur's Labyrinth           | https://tryhackme.com/room/labyrinth8llv                  |      120 |
| Intro to IaC                   | https://tryhackme.com/room/introtoiac                     |      120 |
| Chocolate Factory              | https://tryhackme.com/room/chocolatefactory               |      120 |
| The Hacker Methodology         | https://tryhackme.com/room/hackermethodology              |      120 |
| Olympus                        | https://tryhackme.com/room/olympusroom                    |      120 |
| Intro PoC Scripting            | https://tryhackme.com/room/intropocscripting              |      120 |
| Insecure Deserialisation       | https://tryhackme.com/room/insecuredeserialisation        |      120 |
| Threat Intelligence for SOC    | https://tryhackme.com/room/threatintelligenceforsoc       |      120 |
| Critical                       | https://tryhackme.com/room/critical                       |      120 |
| Gotta Catch'em All!            | https://tryhackme.com/room/pokemon                        |      120 |
| Dissecting PE Headers          | https://tryhackme.com/room/dissectingpeheaders            |      112 |
| Threat Hunting: Foothold       | https://tryhackme.com/room/threathuntingfoothold          |      112 |
| SQLMAP                         | https://tryhackme.com/room/sqlmap                         |      112 |
| Linux File System Analysis     | https://tryhackme.com/room/linuxfilesystemanalysis        |      112 |
| Secure Network Architecture    | https://tryhackme.com/room/introtosecurityarchitecture    |      112 |
| Microservices Architectures    | https://tryhackme.com/room/microservicearchitectures      |      112 |
| Phishing Analysis Fundamentals | https://tryhackme.com/room/phishingemails1tryoe           |      112 |
| Governance & Regulation        | https://tryhackme.com/room/cybergovernanceregulation      |      112 |
| DNS in detail                  | https://tryhackme.com/room/dnsindetail                    |      112 |
| SSRF                           | https://tryhackme.com/room/ssrfhr                         |      112 |
| Peak Hill                      | https://tryhackme.com/room/peakhill                       |      110 |
| Gatekeeper                     | https://tryhackme.com/room/gatekeeper                     |      110 |
| Mindgames                      | https://tryhackme.com/room/mindgames                      |      110 |
| Enterprise                     | https://tryhackme.com/room/enterprise                     |      110 |
| Racetrack Bank                 | https://tryhackme.com/room/racetrackbank                  |      110 |
| Wgel CTF                       | https://tryhackme.com/room/wgelctf                        |      110 |
| Internal                       | https://tryhackme.com/room/internal                       |      110 |
| Pyrat                          | https://tryhackme.com/room/pyrat                          |      110 |
| Year of the Owl                | https://tryhackme.com/room/yearoftheowl                   |      110 |
| Undiscovered                   | https://tryhackme.com/room/undiscoveredup                 |      110 |
| Ignite                         | https://tryhackme.com/room/ignite                         |      110 |
| Aster                          | https://tryhackme.com/room/aster                          |      110 |
| Thompson                       | https://tryhackme.com/room/bsidesgtthompson               |      110 |
| Lockdown                       | https://tryhackme.com/room/lockdown                       |      110 |
| Hypervisor Internals           | https://tryhackme.com/room/hypervisorinternals            |      104 |
| SQL Injection                  | https://tryhackme.com/room/sqlinjectionlm                 |      104 |
| ParrotPost: Phishing Analysis  | https://tryhackme.com/room/parrotpost                     |      104 |
| x86 Architecture Overview      | https://tryhackme.com/room/x8664arch                      |      104 |
| Introductory Researching       | https://tryhackme.com/room/introtoresearch                |      104 |
| Windows Fundamentals 1         | https://tryhackme.com/room/windowsfundamentals1xbx        |      104 |
| Bypassing UAC                  | https://tryhackme.com/room/bypassinguac                   |      100 |
| Kenobi                         | https://tryhackme.com/room/kenobi                         |      100 |
| CVE-2021-41773/42013           | https://tryhackme.com/room/cve202141773                   |       96 |
| Legal Considerations in DFIR   | https://tryhackme.com/room/dfirprocesslegalconsiderations |       96 |
| JavaScript Basics              | https://tryhackme.com/room/javascriptbasics               |       96 |
| SQL Injection Lab              | https://tryhackme.com/room/sqlilab                        |       96 |
| RustScan                       | https://tryhackme.com/room/rustscan                       |       96 |
| NoSQL Injection                | https://tryhackme.com/room/nosqlinjectiontutorial         |       96 |
| IR Philosophy and Ethics       | https://tryhackme.com/room/irphilosophyethics             |       96 |
| IR Playbooks                   | https://tryhackme.com/room/irplaybooks                    |       96 |
| Linux Process Analysis         | https://tryhackme.com/room/linuxprocessanalysis           |       96 |
| Snyk Code                      | https://tryhackme.com/room/snykcode                       |       96 |
| Intro to Logs                  | https://tryhackme.com/room/introtologs                    |       96 |
| Introduction to SIEM           | https://tryhackme.com/room/introtosiem                    |       96 |
| SDLC                           | https://tryhackme.com/room/sdlc                           |       96 |
| Cactus                         | https://tryhackme.com/room/cactus                         |       96 |
| Empire                         | https://tryhackme.com/room/rppsempire                     |       92 |
| Shaker                         | https://tryhackme.com/room/shaker                         |       90 |
| Mr Robot CTF                   | https://tryhackme.com/room/mrrobot                        |       90 |
| Fusion Corp                    | https://tryhackme.com/room/fusioncorp                     |       90 |
| Basic Malware RE               | https://tryhackme.com/room/basicmalwarere                 |       90 |
| Red Stone One Carat            | https://tryhackme.com/room/redstoneonecarat               |       90 |
| The London Bridge              | https://tryhackme.com/room/thelondonbridge                |       90 |
| That's The Ticket              | https://tryhackme.com/room/thatstheticket                 |       90 |
| Breakme                        | https://tryhackme.com/room/breakmenu                      |       90 |
| StuxCTF                        | https://tryhackme.com/room/stuxctf                        |       90 |
| CherryBlossom                  | https://tryhackme.com/room/cherryblossom                  |       90 |
| Plotted-EMR                    | https://tryhackme.com/room/plottedemr                     |       90 |
| The Server From Hell           | https://tryhackme.com/room/theserverfromhell              |       90 |
| The Great Escape               | https://tryhackme.com/room/thegreatescape                 |       90 |
| Umbrella                       | https://tryhackme.com/room/umbrella                       |       90 |
| En-pass                        | https://tryhackme.com/room/enpass                         |       90 |
| WWBuddy                        | https://tryhackme.com/room/wwbuddy                        |       90 |
| Race Conditions Challenge      | https://tryhackme.com/room/raceconditions                 |       90 |
| VulnNet: Endgame               | https://tryhackme.com/room/vulnnetendgame                 |       90 |
| GLITCH                         | https://tryhackme.com/room/glitch                         |       90 |
| The Bandit Surfer              | https://tryhackme.com/room/surfingyetiiscomingtotown      |       90 |
| Break Out The Cage             | https://tryhackme.com/room/breakoutthecage1               |       90 |
| Cat Pictures 2                 | https://tryhackme.com/room/catpictures2                   |       90 |
| The Marketplace                | https://tryhackme.com/room/marketplace                    |       90 |
| Red                            | https://tryhackme.com/room/redisl33t                      |       90 |
| Dreaming                       | https://tryhackme.com/room/dreaming                       |       90 |
| NerdHerd                       | https://tryhackme.com/room/nerdherd                       |       90 |
| Python Playground              | https://tryhackme.com/room/pythonplayground               |       90 |
| Spring                         | https://tryhackme.com/room/spring                         |       90 |
| Anonymous Playground           | https://tryhackme.com/room/anonymousplayground            |       90 |
| Overpass 3 -  Hosting          | https://tryhackme.com/room/overpass3hosting               |       90 |
| Super Secret TIp               | https://tryhackme.com/room/supersecrettip                 |       90 |
| battery                        | https://tryhackme.com/room/battery                        |       90 |
| Intro to Threat Emulation      | https://tryhackme.com/room/threatemulationintro           |       88 |
| Linux Incident Surface         | https://tryhackme.com/room/linuxincidentsurface           |       88 |
| Linux PrivEsc Arena            | https://tryhackme.com/room/linuxprivescarena              |       88 |
| Passive Reconnaissance         | https://tryhackme.com/room/passiverecon                   |       88 |
| Active Reconnaissance          | https://tryhackme.com/room/activerecon                    |       88 |
| Python Basics                  | https://tryhackme.com/room/pythonbasics                   |       88 |
| Linux PrivEsc                  | https://tryhackme.com/room/linuxprivesc                   |       88 |
| Cryptography for Dummies       | https://tryhackme.com/room/cryptographyfordummies         |       88 |
| Red Team Fundamentals          | https://tryhackme.com/room/redteamfundamentals            |       88 |
| Linux Fundamentals Part 1      | https://tryhackme.com/room/linuxfundamentalspart1         |       88 |
| Snyk Open Source               | https://tryhackme.com/room/snykopensource                 |       88 |
| Takedown                       | https://tryhackme.com/room/takedown                       |       80 |
| Chronicle                      | https://tryhackme.com/room/chronicle                      |       80 |
| Cyber Kill Chain               | https://tryhackme.com/room/cyberkillchainzmt              |       80 |
| Metasploit: Introduction       | https://tryhackme.com/room/metasploitintro                |       80 |
| Wonderland                     | https://tryhackme.com/room/wonderland                     |       80 |
| What is Networking?            | https://tryhackme.com/room/whatisnetworking               |       80 |
| AttackerKB                     | https://tryhackme.com/room/attackerkb                     |       80 |
| The Impossible Challenge       | https://tryhackme.com/room/theimpossiblechallenge         |       80 |
| Identification & Scoping       | https://tryhackme.com/room/identificationandscoping       |       80 |
| Snowy ARMageddon               | https://tryhackme.com/room/armageddon2r                   |       80 |
| Preparation                    | https://tryhackme.com/room/preparation                    |       80 |
| Plotted-LMS                    | https://tryhackme.com/room/plottedlms                     |       80 |
| Cicada-3301 Vol:1              | https://tryhackme.com/room/cicada3301vol1                 |       80 |
| Pentesting Fundamentals        | https://tryhackme.com/room/pentestingfundamentals         |       72 |
| Post-Exploitation Basics       | https://tryhackme.com/room/postexploit                    |       72 |
| Vulnerabilities 101            | https://tryhackme.com/room/vulnerabilities101             |       72 |
| Intro to Cyber Threat Intel    | https://tryhackme.com/room/cyberthreatintel               |       72 |
| Unattended                     | https://tryhackme.com/room/unattended                     |       72 |
| Hosted Hypervisors             | https://tryhackme.com/room/hostedhypervisors              |       72 |
| Intro to Containerisation      | https://tryhackme.com/room/introtocontainerisation        |       72 |
| Intro to Cold System Forensics | https://tryhackme.com/room/introtocoldsystemforensics     |       72 |
| Security Engineer Intro        | https://tryhackme.com/room/securityengineerintro          |       72 |
| Linux Function Hooking         | https://tryhackme.com/room/linuxfunctionhooking           |       72 |
| PaperCut: CVE-2023-27350       | https://tryhackme.com/room/papercut                       |       72 |
| Deja Vu                        | https://tryhackme.com/room/dejavu                         |       72 |
| AD Certificate Templates       | https://tryhackme.com/room/adcertificatetemplates         |       72 |
| Insekube                       | https://tryhackme.com/room/insekube                       |       72 |
| Solar, exploiting log4j        | https://tryhackme.com/room/solar                          |       64 |
| Joomify: CVE-2023-23752        | https://tryhackme.com/room/joomify                        |       64 |
| Red Team OPSEC                 | https://tryhackme.com/room/opsec                          |       64 |
| Active Directory Hardening     | https://tryhackme.com/room/activedirectoryhardening       |       64 |
| Introduction to Antivirus      | https://tryhackme.com/room/introtoav                      |       64 |
| TShark                         | https://tryhackme.com/room/tshark                         |       64 |
| Opacity                        | https://tryhackme.com/room/opacity                        |       60 |
| Cheese CTF                     | https://tryhackme.com/room/cheesectfv10                   |       60 |
| Road                           | https://tryhackme.com/room/road                           |       60 |
| Weasel                         | https://tryhackme.com/room/weasel                         |       60 |
| Valley                         | https://tryhackme.com/room/valleype                       |       60 |
| Zeno                           | https://tryhackme.com/room/zeno                           |       60 |
| Forgotten Implant              | https://tryhackme.com/room/forgottenimplant               |       60 |
| Extracted                      | https://tryhackme.com/room/extractedroom                  |       60 |
| Hack Smarter Security          | https://tryhackme.com/room/hacksmartersecurity            |       60 |
| Hijack                         | https://tryhackme.com/room/hijack                         |       60 |
| Athena                         | https://tryhackme.com/room/4th3n4                         |       60 |
| mKingdom                       | https://tryhackme.com/room/mkingdom                       |       60 |
| Creative                       | https://tryhackme.com/room/creative                       |       60 |
| Sea Surfer                     | https://tryhackme.com/room/seasurfer                      |       60 |
| Annie                          | https://tryhackme.com/room/annie                          |       60 |
| Kitty                          | https://tryhackme.com/room/kitty                          |       60 |
| CyberLens                      | https://tryhackme.com/room/cyberlensp6                    |       60 |
| Hacker vs. Hacker              | https://tryhackme.com/room/hackervshacker                 |       60 |
| WhyHackMe                      | https://tryhackme.com/room/whyhackme                      |       60 |
| Aratus                         | https://tryhackme.com/room/aratus                         |       60 |
| Airplane                       | https://tryhackme.com/room/airplane                       |       60 |
| biteme                         | https://tryhackme.com/room/biteme                         |       60 |
| Lumberjack Turtle              | https://tryhackme.com/room/lumberjackturtle               |       60 |
| Oh My WebServer                | https://tryhackme.com/room/ohmyweb                        |       60 |
| Flatline                       | https://tryhackme.com/room/flatline                       |       60 |
| Plotted-TMS                    | https://tryhackme.com/room/plottedtms                     |       60 |
| W1seGuy                        | https://tryhackme.com/room/w1seguy                        |       60 |
| Ollie                          | https://tryhackme.com/room/ollie                          |       60 |
| Publisher                      | https://tryhackme.com/room/publisher                      |       60 |
| Frank and Herby try again..... | https://tryhackme.com/room/frankandherbytryagain          |       60 |
| Dear QA                        | https://tryhackme.com/room/dearqa                         |       60 |
| U.A. High School               | https://tryhackme.com/room/yueiua                         |       60 |
| IDE                            | https://tryhackme.com/room/ide                            |       60 |
| Mountaineer                    | https://tryhackme.com/room/mountaineerlinux               |       60 |
| Team                           | https://tryhackme.com/room/teamcw                         |       60 |
| VulnNet: dotpy                 | https://tryhackme.com/room/vulnnetdotpy                   |       60 |
| Blueprint                      | https://tryhackme.com/room/blueprint                      |       60 |
| JPGChat                        | https://tryhackme.com/room/jpgchat                        |       60 |
| Carpe Diem 1                   | https://tryhackme.com/room/carpediem1                     |       60 |
| GameBuzz                       | https://tryhackme.com/room/gamebuzz                       |       60 |
| EnterPrize                     | https://tryhackme.com/room/enterprize                     |       60 |
| Iron Corp                      | https://tryhackme.com/room/ironcorp                       |       60 |
| Inferno                        | https://tryhackme.com/room/inferno                        |       60 |
| Wekor                          | https://tryhackme.com/room/wekorra                        |       60 |
| VulnNet: Active                | https://tryhackme.com/room/vulnnetactive                  |       60 |
| VulnNet: Node                  | https://tryhackme.com/room/vulnnetnode                    |       60 |
| Metamorphosis                  | https://tryhackme.com/room/metamorphosis                  |       60 |
| Cold VVars                     | https://tryhackme.com/room/coldvvars                      |       60 |
| SafeZone                       | https://tryhackme.com/room/safezone                       |       60 |
| HaskHell                       | https://tryhackme.com/room/haskhell                       |       60 |
| Hydra                          | https://tryhackme.com/room/hydra                          |       60 |
| Debug                          | https://tryhackme.com/room/debug                          |       60 |
| Sudo Security Bypass           | https://tryhackme.com/room/sudovulnsbypass                |       60 |
| Year of the Jellyfish          | https://tryhackme.com/room/yearofthejellyfish             |       60 |
| Git and Crumpets               | https://tryhackme.com/room/gitandcrumpets                 |       60 |
| Willow                         | https://tryhackme.com/room/willow                         |       60 |
| VulnNet: Roasted               | https://tryhackme.com/room/vulnnetroasted                 |       60 |
| Jack-of-All-Trades             | https://tryhackme.com/room/jackofalltrades                |       60 |
| Madness                        | https://tryhackme.com/room/madness                        |       60 |
| hc0n Christmas CTF             | https://tryhackme.com/room/hc0nchristmasctf               |       60 |
| Cat Pictures                   | https://tryhackme.com/room/catpictures                    |       60 |
| Mustacchio                     | https://tryhackme.com/room/mustacchio                     |       60 |
| Brooklyn Nine Nine             | https://tryhackme.com/room/brooklynninenine               |       60 |
| LazyAdmin                      | https://tryhackme.com/room/lazyadmin                      |       60 |
| Fortress                       | https://tryhackme.com/room/fortress                       |       60 |
| Library                        | https://tryhackme.com/room/bsidesgtlibrary                |       60 |
| GamingServer                   | https://tryhackme.com/room/gamingserver                   |       60 |
| The Blob Blog                  | https://tryhackme.com/room/theblobblog                    |       60 |
| Jacob the Boss                 | https://tryhackme.com/room/jacobtheboss                   |       60 |
| toc2                           | https://tryhackme.com/room/toc2                           |       60 |
| 0day                           | https://tryhackme.com/room/0day                           |       60 |
| Attacking ICS Plant #2         | https://tryhackme.com/room/attackingics2                  |       60 |
| Anonforce                      | https://tryhackme.com/room/bsidesgtanonforce              |       60 |
| Chill Hack                     | https://tryhackme.com/room/chillhack                      |       60 |
| ColddBox: Easy                 | https://tryhackme.com/room/colddboxeasy                   |       60 |
| Unbaked Pie                    | https://tryhackme.com/room/unbakedpie                     |       60 |
| magician                       | https://tryhackme.com/room/magician                       |       60 |
| Motunui                        | https://tryhackme.com/room/motunui                        |       60 |
| All in One                     | https://tryhackme.com/room/allinonemj                     |       60 |
| Dav                            | https://tryhackme.com/room/bsidesgtdav                    |       60 |
| Bookstore                      | https://tryhackme.com/room/bookstoreoc                    |       60 |
| Smag Grotto                    | https://tryhackme.com/room/smaggrotto                     |       60 |
| Develpy                        | https://tryhackme.com/room/bsidesgtdevelpy                |       60 |
| Source                         | https://tryhackme.com/room/source                         |       60 |
| Overpass                       | https://tryhackme.com/room/overpass                       |       60 |
| Empline                        | https://tryhackme.com/room/empline                        |       60 |
| harder                         | https://tryhackme.com/room/harder                         |       60 |
| Log Operations                 | https://tryhackme.com/room/logoperations                  |       56 |
| CVE-2022-26923                 | https://tryhackme.com/room/cve202226923                   |       56 |
| Intro to Detection Engineering | https://tryhackme.com/room/introtodetectionengineering    |       56 |
| Putting it all together        | https://tryhackme.com/room/puttingitalltogether           |       56 |
| Bolt                           | https://tryhackme.com/room/bolt                           |       56 |
| DFIR: An Introduction          | https://tryhackme.com/room/introductoryroomdfirmodule     |       56 |
| HTTP/2 Request Smuggling       | https://tryhackme.com/room/http2requestsmuggling          |       56 |
| Intro to IR and IM             | https://tryhackme.com/room/introtoirandim                 |       56 |
| Security Principles            | https://tryhackme.com/room/securityprinciples             |       56 |
| OpenVAS                        | https://tryhackme.com/room/openvas                        |       56 |
| Phishing Emails in Action      | https://tryhackme.com/room/phishingemails2rytmuv          |       56 |
| Burp Suite: Repeater           | https://tryhackme.com/room/burpsuiterepeater              |       56 |
| Windows Fundamentals 3         | https://tryhackme.com/room/windowsfundamentals3xzx        |       56 |
| ret2libc                       | https://tryhackme.com/room/ret2libc                       |       56 |
| Common Attacks                 | https://tryhackme.com/room/commonattacks                  |       56 |
| Red Team Threat Intel          | https://tryhackme.com/room/redteamthreatintel             |       56 |
| HTTP Request Smuggling         | https://tryhackme.com/room/httprequestsmuggling           |       48 |
| How Websites Work              | https://tryhackme.com/room/howwebsiteswork                |       48 |
| Introduction to Django         | https://tryhackme.com/room/django                         |       48 |
| Intro to Endpoint Security     | https://tryhackme.com/room/introtoendpointsecurity        |       48 |
| Windows PrivEsc                | https://tryhackme.com/room/windows10privesc               |       48 |
| Introduction to Flask          | https://tryhackme.com/room/flask                          |       48 |
| Forensic Imaging               | https://tryhackme.com/room/forensicimaging                |       48 |
| Traffic Analysis Essentials    | https://tryhackme.com/room/trafficanalysisessentials      |       40 |
| Intro to Digital Forensics     | https://tryhackme.com/room/introdigitalforensics          |       40 |
| Defensive Security Intro       | https://tryhackme.com/room/defensivesecurityintro         |       40 |
| DLL HIJACKING                  | https://tryhackme.com/room/dllhijacking                   |       40 |
| Security Awareness             | https://tryhackme.com/room/securityawarenessintro         |       40 |
| Cyber Scotland 2021            | https://tryhackme.com/room/cyberweek2021                  |       40 |
| Atlassian CVE-2022-26134       | https://tryhackme.com/room/cve202226134                   |       40 |
| SSTI                           | https://tryhackme.com/room/learnssti                      |       40 |
| Printer Hacking 101            | https://tryhackme.com/room/printerhacking101              |       40 |
| Enumeration & Brute Force      | https://tryhackme.com/room/enumerationbruteforce          |       40 |
| Moniker Link (CVE-2024-21413)  | https://tryhackme.com/room/monikerlink                    |       40 |
| Confluence CVE-2023-22515      | https://tryhackme.com/room/confluence202322515            |       32 |
| Linux Backdoors                | https://tryhackme.com/room/linuxbackdoors                 |       32 |
| GitLab CVE-2023-7028           | https://tryhackme.com/room/gitlabcve20237028              |       32 |
| Web Application Security       | https://tryhackme.com/room/introwebapplicationsecurity    |       32 |
| Junior Security Analyst Intro  | https://tryhackme.com/room/jrsecanalystintrouxo           |       32 |
| Polkit: CVE-2021-3560          | https://tryhackme.com/room/polkit                         |       32 |
| Flip                           | https://tryhackme.com/room/flip                           |       30 |
| Island Orchestration           | https://tryhackme.com/room/islandorchestration            |       30 |
| Bypass Disable Functions       | https://tryhackme.com/room/bypassdisablefunctions         |       30 |
| Prioritise                     | https://tryhackme.com/room/prioritise                     |       30 |
| Classic Passwd                 | https://tryhackme.com/room/classicpasswd                  |       30 |
| Corridor                       | https://tryhackme.com/room/corridor                       |       30 |
| Capture!                       | https://tryhackme.com/room/capture                        |       30 |
| Tech_Supp0rt: 1                | https://tryhackme.com/room/techsupp0rt1                   |       30 |
| Capture Returns                | https://tryhackme.com/room/capturereturns                 |       30 |
| ContainMe                      | https://tryhackme.com/room/containme1                     |       30 |
| Compiled                       | https://tryhackme.com/room/compiled                       |       30 |
| Sudo Buffer Overflow           | https://tryhackme.com/room/sudovulnsbof                   |       30 |
| Agent T                        | https://tryhackme.com/room/agentt                         |       30 |
| TakeOver                       | https://tryhackme.com/room/takeover                       |       30 |
| 0x41haz                        | https://tryhackme.com/room/0x41haz                        |       30 |
| Bugged                         | https://tryhackme.com/room/bugged                         |       30 |
| Eavesdropper                   | https://tryhackme.com/room/eavesdropper                   |       30 |
| Git Happens                    | https://tryhackme.com/room/githappens                     |       30 |
| OpenVPN                        | https://tryhackme.com/room/openvpn                        |       30 |
| MD2PDF                         | https://tryhackme.com/room/md2pdf                         |       30 |
| Lesson Learned?                | https://tryhackme.com/room/lessonlearned                  |       30 |
| Tor                            | https://tryhackme.com/room/torforbeginners                |       30 |
| Getting Started                | https://tryhackme.com/room/gettingstarted                 |       24 |
| Introduction to OWASP ZAP      | https://tryhackme.com/room/learnowaspzap                  |       24 |
| Pwnkit: CVE-2021-4034          | https://tryhackme.com/room/pwnkit                         |       24 |
| Atlas                          | https://tryhackme.com/room/atlas                          |       24 |
| Learning Cyber Security        | https://tryhackme.com/room/beginnerpathintro              |       24 |
| Become a Hacker                | https://tryhackme.com/room/becomeahackeroa                |       24 |
| Welcome                        | https://tryhackme.com/room/hello                          |       23 |
| Windows Reversing Intro        | https://tryhackme.com/room/windowsreversingintro          |       16 |
| Starting Out In Cyber Sec      | https://tryhackme.com/room/startingoutincybersec          |       16 |
| Baron Samedit                  | https://tryhackme.com/room/sudovulnssamedit               |       16 |
| Windows PrivEsc Arena          | https://tryhackme.com/room/windowsprivescarena            |       16 |
| CVE-2023-38408                 | https://tryhackme.com/room/cve202338408                   |       16 |
| How to use TryHackMe           | https://tryhackme.com/room/howtousetryhackme              |       16 |
| OverlayFS - CVE-2021-3493      | https://tryhackme.com/room/overlayfs                      |        8 |
| LocalPotato                    | https://tryhackme.com/room/localpotato                    |        8 |
| Looney Tunables                | https://tryhackme.com/room/looneytunes                    |        8 |
| Spring4Shell: CVE-2022-22965   | https://tryhackme.com/room/spring4shell                   |        8 |
| Dirty Pipe: CVE-2022-0847      | https://tryhackme.com/room/dirtypipe                      |        8 |
| Offensive Security Intro       | https://tryhackme.com/room/offensivesecurityintro         |        8 |
| IronShade                      | https://tryhackme.com/room/ironshade                      |        0 |
| NIS - Linux Part I             | https://tryhackme.com/room/nislinuxone                    |        0 |
| Source Code Security           | https://tryhackme.com/room/sourcecodesecurity             |        0 |
| Stealth                        | https://tryhackme.com/room/stealth                        |        0 |
| AVenger                        | https://tryhackme.com/room/avenger                        |        0 |
| Probe                          | https://tryhackme.com/room/probe                          |        0 |
| Recovering Active Directory    | https://tryhackme.com/room/recoveringactivedirectory      |        0 |
| Intro to IoT Pentesting        | https://tryhackme.com/room/iotintro                       |        0 |
| Bulletproof Penguin            | https://tryhackme.com/room/bppenguin                      |        0 |
| The Witch's Cauldron           | https://tryhackme.com/room/cauldron                       |        0 |
| Boogeyman 2                    | https://tryhackme.com/room/boogeyman2                     |        0 |
| Boogeyman 3                    | https://tryhackme.com/room/boogeyman3                     |        0 |
| Set                            | https://tryhackme.com/room/set                            |        0 |
| DockMagic                      | https://tryhackme.com/room/dockmagic                      |        0 |
| Bandit                         | https://tryhackme.com/room/bandit                         |        0 |
| Log Universe                   | https://tryhackme.com/room/loguniverse                    |        0 |
| Scripting                      | https://tryhackme.com/room/scripting                      |        0 |
| NanoCherryCTF                  | https://tryhackme.com/room/nanocherryctf                  |        0 |
| Skynet                         | https://tryhackme.com/room/skynet                         |        0 |
| DVWA                           | https://tryhackme.com/room/dvwa                           |        0 |
| Logstash: Data Processing Unit | https://tryhackme.com/room/logstash                       |        0 |
| Fixit                          | https://tryhackme.com/room/fixit                          |        0 |
| Brainpan 1                     | https://tryhackme.com/room/brainpan                       |        0 |
| Threat Hunting: Endgame        | https://tryhackme.com/room/threathuntingendgame           |        0 |
| The Docker Rodeo               | https://tryhackme.com/room/dockerrodeo                    |        0 |
| Yara                           | https://tryhackme.com/room/yara                           |        0 |
| ToolsRus                       | https://tryhackme.com/room/toolsrus                       |        0 |
| HeartBleed                     | https://tryhackme.com/room/heartbleed                     |        0 |
| Custom Alert Rules in Wazuh    | https://tryhackme.com/room/customalertrulesinwazuh        |        0 |
| K2                             | https://tryhackme.com/room/k2room                         |        0 |
| Brains                         | https://tryhackme.com/room/brains                         |        0 |
| Cyber Crisis Management        | https://tryhackme.com/room/cybercrisismanagement          |        0 |
| Logging for Accountability     | https://tryhackme.com/room/loggingforaccountability       |        0 |
| Kali Machine                   | https://tryhackme.com/room/kali                           |        0 |
| Becoming a First Responder     | https://tryhackme.com/room/becomingafirstresponder        |        0 |
| Jurassic Park                  | https://tryhackme.com/room/jurassicpark                   |        0 |
| Threat Modelling               | https://tryhackme.com/room/threatmodelling                |        0 |
| Hunt Me II: Typo Squatters     | https://tryhackme.com/room/typosquatters                  |        0 |
| Lessons Learned                | https://tryhackme.com/room/lessonslearned                 |        0 |
| Buffer Overflows               | https://tryhackme.com/room/bof1                           |        0 |
| Hunt Me I: Payment Collectors  | https://tryhackme.com/room/paymentcollectors              |        0 |
| Splunk: Data Manipulation      | https://tryhackme.com/room/splunkdatamanipulation         |        0 |
| Splunk: Setting up a SOC Lab   | https://tryhackme.com/room/splunklab                      |        0 |
| Slingshot                      | https://tryhackme.com/room/slingshot                      |        0 |
| Brainstorm                     | https://tryhackme.com/room/brainstorm                     |        0 |
| MalDoc: Static Analysis        | https://tryhackme.com/room/maldoc                         |        0 |
| Dodge                          | https://tryhackme.com/room/dodge                          |        0 |
| WebGOAT                        | https://tryhackme.com/room/webgoat                        |        0 |
| Monday Monitor                 | https://tryhackme.com/room/mondaymonitor                  |        0 |
| Game Zone                      | https://tryhackme.com/room/gamezone                       |        0 |
| Atomic Bird Goes Purple #1     | https://tryhackme.com/room/atomicbirdone                  |        0 |
| Atomic Bird Goes Purple #2     | https://tryhackme.com/room/atomicbirdtwo                  |        0 |
| Threat Hunting: Pivoting       | https://tryhackme.com/room/threathuntingpivoting          |        0 |
| JWT Security                   | https://tryhackme.com/room/jwtsecurity                    |        0 |
| HackPark                       | https://tryhackme.com/room/hackpark                       |        0 |
| Eradication & Remediation      | https://tryhackme.com/room/eradicationandremediation      |        0 |
| Ra 2                           | https://tryhackme.com/room/ra2                            |        0 |
| Eviction                       | https://tryhackme.com/room/eviction                       |        0 |
| Content Security Policy        | https://tryhackme.com/room/csp                            |        0 |
| CORS & SOP                     | https://tryhackme.com/room/corsandsop                     |        0 |
| iOS Analysis                   | https://tryhackme.com/room/iosanalysis                    |        0 |
| Blizzard                       | https://tryhackme.com/room/blizzard                       |        0 |
| Corp                           | https://tryhackme.com/room/corp                           |        0 |
| IR Difficulties and Challenges | https://tryhackme.com/room/irdifficultiesandchallenges    |        0 |
| Windows Base                   | https://tryhackme.com/room/windowsbase                    |        0 |
| Whats Your Name?               | https://tryhackme.com/room/whatsyourname                  |        0 |
| Jack                           | https://tryhackme.com/room/jack                           |        0 |
| Bebop                          | https://tryhackme.com/room/bebop                          |        0 |
| Linux Logs Investigations      | https://tryhackme.com/room/linuxlogsinvestigations        |        0 |
| Race Conditions                | https://tryhackme.com/room/raceconditionsattacks          |        0 |
| Friday Overtime                | https://tryhackme.com/room/fridayovertime                 |        0 |
| What the Shell?                | https://tryhackme.com/room/introtoshells                  |        0 |
| Burp Suite: Extensions         | https://tryhackme.com/room/burpsuiteextensions            |        0 |
| TryHack3M: TriCipher Summit    | https://tryhackme.com/room/tryhack3mencryptionchallenge   |        0 |
| TryHack3M: Subscribe           | https://tryhackme.com/room/subscribe                      |        0 |
| TryHack3M: Burg3r Bytes        | https://tryhackme.com/room/burg3rbytes                    |        0 |
| Analysing Volatile Memory      | https://tryhackme.com/room/analysingvolatilememory        |        0 |
| Common Linux Privesc           | https://tryhackme.com/room/commonlinuxprivesc             |        0 |
| Windows Network Analysis       | https://tryhackme.com/room/windowsnetworkanalysis         |        0 |
| NoNameCTF                      | https://tryhackme.com/room/nonamectf                      |        0 |
| TShark: CLI Wireshark Features | https://tryhackme.com/room/tsharkcliwiresharkfeatures     |        0 |
| Server-side Template Injection | https://tryhackme.com/room/serversidetemplateinjection    |        0 |
| Retracted                      | https://tryhackme.com/room/retracted                      |        0 |
| TShark: The Basics             | https://tryhackme.com/room/tsharkthebasics                |        0 |
| XXE Injection                  | https://tryhackme.com/room/xxeinjection                   |        0 |
| Include                        | https://tryhackme.com/room/include                        |        0 |
| TShark Challenge II: Directory | https://tryhackme.com/room/tsharkchallengestwo            |        0 |
| LDAP Injection                 | https://tryhackme.com/room/ldapinjection                  |        0 |
| Dead End?                      | https://tryhackme.com/room/deadend                        |        0 |
| Binex                          | https://tryhackme.com/room/binex                          |        0 |
| IR Timeline Analysis           | https://tryhackme.com/room/dfirtimelineanalysis           |        0 |
| Prototype Pollution            | https://tryhackme.com/room/prototypepollution             |        0 |
| TShark Challenge I: Teamwork   | https://tryhackme.com/room/tsharkchallengesone            |        0 |
| DOM-Based Attacks              | https://tryhackme.com/room/dombasedattacks                |        0 |
| Injectics                      | https://tryhackme.com/room/injectics                      |        0 |
| Hacking with PowerShell        | https://tryhackme.com/room/powershell                     |        0 |
| MAL: Strings                   | https://tryhackme.com/room/malstrings                     |        0 |
| Steel Mountain                 | https://tryhackme.com/room/steelmountain                  |        0 |
| Cloud-based IaC                | https://tryhackme.com/room/cloudbasediac                  |        0 |
| Intro to Kubernetes            | https://tryhackme.com/room/introtok8s                     |        0 |
| ORM Injection                  | https://tryhackme.com/room/orminjection                   |        0 |
| On-Premises IaC                | https://tryhackme.com/room/onpremisesiac                  |        0 |
| Hashing - Crypto 101           | https://tryhackme.com/room/hashingcrypto101               |        0 |
| Hammer                         | https://tryhackme.com/room/hammer                         |        0 |
| Upload Vulnerabilities         | https://tryhackme.com/room/uploadvulns                    |        0 |
| CI/CD and Build Security       | https://tryhackme.com/room/cicdandbuildsecurity           |        0 |
| Container Hardening            | https://tryhackme.com/room/containerhardening             |        0 |
| Session Management             | https://tryhackme.com/room/sessionmanagement              |        0 |
| Attacking Kerberos             | https://tryhackme.com/room/attackingkerberos              |        0 |
| File Inclusion, Path Traversal | https://tryhackme.com/room/filepathtraversal              |        0 |
| Reset                          | https://tryhackme.com/room/resetui                        |        0 |
| Multi-Factor Authentication    | https://tryhackme.com/room/multifactorauthentications     |        0 |
| TryPwnMe One                   | https://tryhackme.com/room/trypwnmeone                    |        0 |
| Container Vulnerabilities      | https://tryhackme.com/room/containervulnerabilitiesDG     |        0 |
| Avengers Blog                  | https://tryhackme.com/room/avengers                       |        0 |
| Exfilibur                      | https://tryhackme.com/room/exfilibur                      |        0 |
| Windows User Account Forensics | https://tryhackme.com/room/windowsuseraccountforensics    |        0 |
| KoTH Hackers                   | https://tryhackme.com/room/kothhackers                    |        0 |
| Windows User Activity Analysis | https://tryhackme.com/room/windowsuseractivity            |        0 |
| Secure GitOps                  | https://tryhackme.com/room/securegitops                   |        0 |
| Bypass                         | https://tryhackme.com/room/bypass                         |        0 |
| Windows Applications Forensics | https://tryhackme.com/room/windowsapplications            |        0 |
| AD Tier Model                  | https://tryhackme.com/room/adtiermodel                    |        0 |
| DX2: Hell's Kitchen            | https://tryhackme.com/room/dx2hellskitchen                |        0 |
| Alfred                         | https://tryhackme.com/room/alfred                         |        0 |
| El Bandito                     | https://tryhackme.com/room/elbandito                      |        0 |
| Request Smuggling: WebSockets  | https://tryhackme.com/room/wsrequestsmuggling             |        0 |
| Tempus Fugit Durius            | https://tryhackme.com/room/tempusfugitdurius              |        0 |
| Erit Securus I                 | https://tryhackme.com/room/eritsecurusi                   |        0 |
| KoTH Food CTF                  | https://tryhackme.com/room/kothfoodctf                    |        0 |
| HTTP Browser Desync            | https://tryhackme.com/room/requestsmugglingbrowserdesync  |        0 |
| Summit                         | https://tryhackme.com/room/summit                         |        0 |
| OAuth Vulnerabilities          | https://tryhackme.com/room/oauthvulnerabilities           |        0 |
| Linux Live Analysis            | https://tryhackme.com/room/linuxliveanalysis              |        0 |
| Net Sec Challenge              | https://tryhackme.com/room/netsecchallenge                |        0 |
| Burp Suite: Other Modules      | https://tryhackme.com/room/burpsuiteom                    |        0 |
| Volatility                     | https://tryhackme.com/room/volatility                     |        0 |
| Linux Forensics                | https://tryhackme.com/room/linuxforensics                 |        0 |
| CyberHeroes                    | https://tryhackme.com/room/cyberheroes                    |        0 |
| NetworkMiner                   | https://tryhackme.com/room/networkminer                   |        0 |
| Biblioteca                     | https://tryhackme.com/room/biblioteca                     |        0 |
| Dig Dug                        | https://tryhackme.com/room/digdug                         |        0 |
| Careers in Cyber               | https://tryhackme.com/room/careersincyber                 |        0 |
| Security Operations            | https://tryhackme.com/room/securityoperations             |        0 |
| Sandbox Evasion                | https://tryhackme.com/room/sandboxevasion                 |        0 |
| Autopsy                        | https://tryhackme.com/room/btautopsye0                    |        0 |
| Splunk 2                       | https://tryhackme.com/room/splunk2gcd5                    |        0 |
| Intro to Malware Analysis      | https://tryhackme.com/room/intromalwareanalysis           |        0 |
| Network Security               | https://tryhackme.com/room/intronetworksecurity           |        0 |
| Linux Fundamentals Part 2      | https://tryhackme.com/room/linuxfundamentalspart2         |        0 |
| Linux Fundamentals Part 3      | https://tryhackme.com/room/linuxfundamentalspart3         |        0 |
| MISP                           | https://tryhackme.com/room/misp                           |        0 |
| Living Off the Land            | https://tryhackme.com/room/livingofftheland               |        0 |
| Snort Challenge - The Basics   | https://tryhackme.com/room/snortchallenges1               |        0 |
| TheHive Project                | https://tryhackme.com/room/thehiveproject                 |        0 |
| Incident handling with Splunk  | https://tryhackme.com/room/splunk201                      |        0 |
| Evading Logging and Monitoring | https://tryhackme.com/room/monitoringevasion              |        0 |
| Mr. Phisher                    | https://tryhackme.com/room/mrphisher                      |        0 |
| Core Windows Processes         | https://tryhackme.com/room/btwindowsinternals             |        0 |
| Windows Privilege Escalation   | https://tryhackme.com/room/windowsprivesc20               |        0 |
| Credentials Harvesting         | https://tryhackme.com/room/credharvesting                 |        0 |
| Signature Evasion              | https://tryhackme.com/room/signatureevasion               |        0 |
| Obfuscation Principles         | https://tryhackme.com/room/obfuscationprinciples          |        0 |
| Data Exfiltration              | https://tryhackme.com/room/dataxexfilt                    |        0 |
| Sysinternals                   | https://tryhackme.com/room/btsysinternalssg               |        0 |
| Brim                           | https://tryhackme.com/room/brim                           |        0 |
| Confidential                   | https://tryhackme.com/room/confidential                   |        0 |
| Enumeration                    | https://tryhackme.com/room/enumerationpe                  |        0 |
| Velociraptor                   | https://tryhackme.com/room/velociraptorhp                 |        0 |
| Brute                          | https://tryhackme.com/room/ettubrute                      |        0 |
| Zeek Exercises                 | https://tryhackme.com/room/zeekbroexercises               |        0 |
| Zeek                           | https://tryhackme.com/room/zeekbro                        |        0 |
| Windows Local Persistence      | https://tryhackme.com/room/windowslocalpersistence        |        0 |
| Wireshark: Packet Operations   | https://tryhackme.com/room/wiresharkpacketoperations      |        0 |
| Committed                      | https://tryhackme.com/room/committed                      |        0 |
| Persisting Active Directory    | https://tryhackme.com/room/persistingad                   |        0 |
| Wireshark: The Basics          | https://tryhackme.com/room/wiresharkthebasics             |        0 |
| Exploiting Active Directory    | https://tryhackme.com/room/exploitingad                   |        0 |
| Lateral Movement and Pivoting  | https://tryhackme.com/room/lateralmovementandpivoting     |        0 |
| Abusing Windows Internals      | https://tryhackme.com/room/abusingwindowsinternals        |        0 |
| Napping                        | https://tryhackme.com/room/nappingis1337                  |        0 |
| Operating System Security      | https://tryhackme.com/room/operatingsystemsecurity        |        0 |
| Runtime Detection Evasion      | https://tryhackme.com/room/runtimedetectionevasion        |        0 |
| Phishing Analysis Tools        | https://tryhackme.com/room/phishingemails3tryoe           |        0 |
| Red Team Recon                 | https://tryhackme.com/room/redteamrecon                   |        0 |
| Weaponization                  | https://tryhackme.com/room/weaponization                  |        0 |
| Exploit Vulnerabilities        | https://tryhackme.com/room/exploitingavulnerabilityv2     |        0 |
| Vulnerability Capstone         | https://tryhackme.com/room/vulnerabilitycapstone          |        0 |
| Metasploit: Exploitation       | https://tryhackme.com/room/metasploitexploitation         |        0 |
| Metasploit: Meterpreter        | https://tryhackme.com/room/meterpreter                    |        0 |
| Content Discovery              | https://tryhackme.com/room/contentdiscovery               |        0 |
| IDOR                           | https://tryhackme.com/room/idor                           |        0 |
| File Inclusion                 | https://tryhackme.com/room/fileinc                        |        0 |
| Password Attacks               | https://tryhackme.com/room/passwordattacks                |        0 |
| Intro to Cross-site Scripting  | https://tryhackme.com/room/xss                            |        0 |
| Command Injection              | https://tryhackme.com/room/oscommandinjection             |        0 |
| Phishing                       | https://tryhackme.com/room/phishingyl                     |        0 |
| Nmap Basic Port Scans          | https://tryhackme.com/room/nmap02                         |        0 |
| Nmap Advanced Port Scans       | https://tryhackme.com/room/nmap03                         |        0 |
| Temple                         | https://tryhackme.com/room/temple                         |        0 |
| Nmap Post Port Scans           | https://tryhackme.com/room/nmap04                         |        0 |
| Protocols and Servers          | https://tryhackme.com/room/protocolsandservers            |        0 |
| Phishing Prevention            | https://tryhackme.com/room/phishingemails4gkxh            |        0 |
| The Greenholt Phish            | https://tryhackme.com/room/phishingemails5fgjlzxc         |        0 |
| Principles of Security         | https://tryhackme.com/room/principlesofsecurity           |        0 |
| Learn and win prizes           | https://tryhackme.com/room/tickets1                       |        0 |
| Snort Challenge - Live Attacks | https://tryhackme.com/room/snortchallenges2               |        0 |
| Intro to LAN                   | https://tryhackme.com/room/introtolan                     |        0 |
| Intro to C2                    | https://tryhackme.com/room/introtoc2                      |        0 |
| OSI Model                      | https://tryhackme.com/room/osimodelzi                     |        0 |
| Packets & Frames               | https://tryhackme.com/room/packetsframes                  |        0 |
| Network Security Solutions     | https://tryhackme.com/room/redteamnetsec                  |        0 |
| Windows Internals              | https://tryhackme.com/room/windowsinternals               |        0 |
| Extending Your Network         | https://tryhackme.com/room/extendingyournetwork           |        0 |
| Splunk 3                       | https://tryhackme.com/room/splunk3zs                      |        0 |
| Subdomain Enumeration          | https://tryhackme.com/room/subdomainenumeration           |        0 |
| Windows Forensics 2            | https://tryhackme.com/room/windowsforensics2              |        0 |
| Firewalls                      | https://tryhackme.com/room/redteamfirewalls               |        0 |
| Python for Pentesters          | https://tryhackme.com/room/pythonforcybersecurity         |        0 |
| PowerShell for Pentesters      | https://tryhackme.com/room/powershellforpentesters        |        0 |
| Walking An Application         | https://tryhackme.com/room/walkinganapplication           |        0 |
| The Lay of the Land            | https://tryhackme.com/room/thelayoftheland                |        0 |
| Authentication Bypass          | https://tryhackme.com/room/authenticationbypass           |        0 |
| Intro to SSRF                  | https://tryhackme.com/room/ssrfqi                         |        0 |
| AV Evasion: Shellcode          | https://tryhackme.com/room/avevasionshellcode             |        0 |
| Intermediate Nmap              | https://tryhackme.com/room/intermediatenmap               |        0 |
| Burp Suite: Intruder           | https://tryhackme.com/room/burpsuiteintruder              |        0 |
| CALDERA                        | https://tryhackme.com/room/caldera                        |        0 |
| Network Device Hardening       | https://tryhackme.com/room/networkdevicehardening         |        0 |
| Intranet                       | https://tryhackme.com/room/securesolacodersintra          |        0 |
| Keldagrim                      | https://tryhackme.com/room/keldagrim                      |        0 |
| Anti-Reverse Engineering       | https://tryhackme.com/room/antireverseengineering         |        0 |
| Protocols and Servers 2        | https://tryhackme.com/room/protocolsandservers2           |        0 |
| Hardening Basics Part 2        | https://tryhackme.com/room/hardeningbasicspart2           |        0 |
| Vulnerability Management       | https://tryhackme.com/room/vulnerabilitymanagementkj      |        0 |
| Dynamic Analysis: Debugging    | https://tryhackme.com/room/advanceddynamicanalysis        |        0 |
| SOAR                           | https://tryhackme.com/room/soar                           |        0 |
| Linux System Hardening         | https://tryhackme.com/room/linuxsystemhardening           |        0 |
| MAL: REMnux - The Redux        | https://tryhackme.com/room/malremnuxv2                    |        0 |
| MITRE                          | https://tryhackme.com/room/mitre                          |        0 |
| Basic Dynamic Analysis         | https://tryhackme.com/room/basicdynamicanalysis           |        0 |
| Services                       | https://tryhackme.com/room/services                       |        0 |
| Weaponizing Vulnerabilities    | https://tryhackme.com/room/weaponizingvulnerabilities     |        0 |
| Boogeyman 1                    | https://tryhackme.com/room/boogeyman1                     |        0 |
| DAST                           | https://tryhackme.com/room/dastzap                        |        0 |
| Devie                          | https://tryhackme.com/room/devie                          |        0 |
| Atomic Red Team                | https://tryhackme.com/room/atomicredteam                  |        0 |
| SAST                           | https://tryhackme.com/room/sast                           |        0 |
| Advanced ELK Queries           | https://tryhackme.com/room/advancedelkqueries             |        0 |
| Microsoft Windows Hardening    | https://tryhackme.com/room/microsoftwindowshardening      |        0 |
| Virtualization and Containers  | https://tryhackme.com/room/virtualizationandcontainers    |        0 |
| Burp Suite: The Basics         | https://tryhackme.com/room/burpsuitebasics                |        0 |
| Mother's Secret                | https://tryhackme.com/room/codeanalysis                   |        0 |
| Linux: Local Enumeration       | https://tryhackme.com/room/lle                            |        0 |
| Expose                         | https://tryhackme.com/room/expose                         |        0 |
| Risk Management                | https://tryhackme.com/room/seriskmanagement               |        0 |
| Advanced Static Analysis       | https://tryhackme.com/room/advancedstaticanalysis         |        0 |
| x86 Assembly Crash Course      | https://tryhackme.com/room/x86assemblycrashcourse         |        0 |
| Grep                           | https://tryhackme.com/room/greprtp                        |        0 |
| Splunk: Dashboards and Reports | https://tryhackme.com/room/splunkdashboardsandreports     |        0 |
| iOS Forensics                  | https://tryhackme.com/room/iosforensics                   |        0 |
| Threat Intel & Containment     | https://tryhackme.com/room/intelcreationandcontainment    |        0 |
| Res                            | https://tryhackme.com/room/res                            |        0 |
| Auditing and Monitoring        | https://tryhackme.com/room/auditingandmonitoringse        |        0 |
| Zero Logon                     | https://tryhackme.com/room/zer0logon                      |        0 |
| Trooper                        | https://tryhackme.com/room/trooper                        |        0 |
| Traverse                       | https://tryhackme.com/room/traverse                       |        0 |
| Wireshark 101                  | https://tryhackme.com/room/wireshark                      |        0 |
| Osiris                         | https://tryhackme.com/room/osiris                         |        0 |
| Snapped Phish-ing Line         | https://tryhackme.com/room/snappedphishingline            |        0 |
| Disgruntled                    | https://tryhackme.com/room/disgruntled                    |        0 |
| Outlook NTLM Leak              | https://tryhackme.com/room/outlookntlmleak                |        0 |
| Network Security Protocols     | https://tryhackme.com/room/networksecurityprotocols       |        0 |
| Lookback                       | https://tryhackme.com/room/lookback                       |        0 |
| Osquery: The Basics            | https://tryhackme.com/room/osqueryf8                      |        0 |
| PrintNightmare, thrice!        | https://tryhackme.com/room/printnightmarec3kj             |        0 |
| Splunk: Basics                 | https://tryhackme.com/room/splunk101                      |        0 |
| OWASP Mutillidae II            | https://tryhackme.com/room/owaspmutillidae                |        0 |
| Investigating with ELK 101     | https://tryhackme.com/room/investigatingwithelk101        |        0 |
| PS Eclipse                     | https://tryhackme.com/room/posheclipse                    |        0 |
| Templates                      | https://tryhackme.com/room/templates                      |        0 |
| Warzone 1                      | https://tryhackme.com/room/warzoneone                     |        0 |
| Epoch                          | https://tryhackme.com/room/epoch                          |        0 |
| PrintNightmare, again!         | https://tryhackme.com/room/printnightmarec2bn7l           |        0 |
| Investigating with Splunk      | https://tryhackme.com/room/investigatingwithsplunk        |        0 |
| Benign                         | https://tryhackme.com/room/benign                         |        0 |
| ItsyBitsy                      | https://tryhackme.com/room/itsybitsy                      |        0 |
| DX1: Liberty Island            | https://tryhackme.com/room/dx1libertyislandplde           |        0 |
| Surfer                         | https://tryhackme.com/room/surfer                         |        0 |
| Wireshark: Traffic Analysis    | https://tryhackme.com/room/wiresharktrafficanalysis       |        0 |
| OpenCTI                        | https://tryhackme.com/room/opencti                        |        0 |
| Diamond Model                  | https://tryhackme.com/room/diamondmodelrmuwwg42           |        0 |
| Web Enumeration                | https://tryhackme.com/room/webenumerationv2               |        0 |
| Neighbour                      | https://tryhackme.com/room/neighbour                      |        0 |
| Tempest                        | https://tryhackme.com/room/tempestincident                |        0 |
| Sysmon                         | https://tryhackme.com/room/sysmon                         |        0 |
| AllSignsPoint2Pwnage           | https://tryhackme.com/room/allsignspoint2pwnage           |        0 |
| Aurora EDR                     | https://tryhackme.com/room/auroraedr                      |        0 |
| Holo                           | https://tryhackme.com/room/hololive                       |        0 |
| John the Ripper: The Basics    | https://tryhackme.com/room/johntheripperbasics            |        0 |
| Intro to Cloud Security        | https://tryhackme.com/room/introductiontocloudsecurityc6  |        0 |
| Tardigrade                     | https://tryhackme.com/room/tardigrade                     |        0 |
| Dependency Management          | https://tryhackme.com/room/dependencymanagement           |        0 |
| Second                         | https://tryhackme.com/room/fearsecond                     |        0 |
| Basic Static Analysis          | https://tryhackme.com/room/staticanalysis1                |        0 |
| MalBuster                      | https://tryhackme.com/room/malbuster                      |        0 |
| Warzone 2                      | https://tryhackme.com/room/warzonetwo                     |        0 |
| OWASP API Security Top 10 - 2  | https://tryhackme.com/room/owaspapisecuritytop10d0        |        0 |
| OWASP API Security Top 10 - 1  | https://tryhackme.com/room/owaspapisecuritytop105w        |        0 |
| SigHunt                        | https://tryhackme.com/room/sighunt                        |        0 |
| Sigma                          | https://tryhackme.com/room/sigma                          |        0 |
| New Hire Old Artifacts         | https://tryhackme.com/room/newhireoldartifacts            |        0 |
| Tactical Detection             | https://tryhackme.com/room/tacticaldetection              |        0 |
| Secret Recipe                  | https://tryhackme.com/room/registry4n6                    |        0 |
| Windows Event Logs             | https://tryhackme.com/room/windowseventlogs               |        0 |
| Hardening Basics Part 1        | https://tryhackme.com/room/hardeningbasicspart1           |        0 |

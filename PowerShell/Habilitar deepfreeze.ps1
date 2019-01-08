$wshell = New-Object -ComObject wscript.shell;
$wshell.SendKeys('^+%{F6}')
$wshell.AppActivate('Deep Freeze Standard')
Sleep 1
$wshell.SendKeys('Fl@shm4n')
$wshell.SendKeys('~')
$wshell.SendKeys('%{F}')
$wshell.SendKeys('%{O}')
Sleep 1
$wshell.SendKeys('~')
Sleep 1
shutdown -s -t 5
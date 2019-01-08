$wshell = New-Object -ComObject wscript.shell;
$wshell.SendKeys('^+%{F6}')
$wshell.AppActivate('Deep Freeze Standard')
Sleep 1
$wshell.SendKeys('Fl@shm4n')
$wshell.SendKeys('~')
$wshell.SendKeys('%{T}')
$wshell.SendKeys('%{R}')
Sleep 1
$wshell.SendKeys('~')
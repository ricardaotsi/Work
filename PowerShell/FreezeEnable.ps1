$wshell = New-Object -ComObject wscript.shell;
$wshell.SendKeys("+^%{F6}")
sleep(1)
$wshell.SendKeys("password")
$wshell.SendKeys("~")
sleep(0.5)
$wshell.SendKeys("%f")
$wshell.SendKeys("%o")
$wshell.SendKeys("~")
shutdown -f -s -t 0

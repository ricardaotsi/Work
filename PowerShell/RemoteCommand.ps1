$Username = 'user'
$Password = 'password'
$pass = ConvertTo-SecureString -AsPlainText $Password -Force
$Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $Username,$pass

for($i=1;$i -le 25; $i++)
{
    Invoke-Command -ComputerName 'ip'+$i -ScriptBlock { dir } -Credential $Cred
}

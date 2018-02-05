Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
choco feature enable -n allowGlobalConfirmation
choco install googlechrome jre8 7zip.install notepadplusplus.install vlc ccleaner dotnet4.5 dotnet3.5 libreoffice-fresh foxitreader avastfreeantivirus imgburn

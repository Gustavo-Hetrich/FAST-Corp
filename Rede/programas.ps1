# Diretório onde os programas estão localizados
$netlogon = "\\grupouninter.local\NETLOGON\FastCorp"
$corp = "\\corp-dfs-01\ANYDESK ENTERPRISE - EXCLUSIVO SUPORTE TECNICO\Users"

# Executando o Script de Instalação Anydesk
Write-Host "Instalando Anydesk..."
& "$corp\AnyDesk_Client_V1.0.exe"

# Executando o Script de Instalação Cortex
Write-Host "Instalando Cortex..."
& "$netlogon\Cortex\InstallCortex.ps1"

# Executando o Script de Instalação Global
Write-Host "Instalando Global..."
& "$netlogon\GlobalProtect\Install Global Protect.ps1"

# Executando o Script de Netskope
Write-Host "Instalando Netskope..."
& "$netlogon\Netskope\Netskope.bat"

Write-Host "Todos os programas foram instalados com sucesso!"

# Mantém a janela aberta até que o usuário pressione Enter
Read-Host "Pressione Enter para sair..."
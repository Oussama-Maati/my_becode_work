function Get-shut-boot-info {
	$shutDownInfo = Get-WinEvent -FilterHashtable @{LogName='System'; ID=1074} -MaxEvents 1
	$lastShutdownTime = $shutdownInfo.TimeCreated

	# Last boot info
	$bootInfo = Get-WinEvent -FilterHashtable @{LogName='System'; ID=12} -MaxEvents 1
	$lastBootTime = $bootInfo.TimeCreated

	# computer/device name 
	$DeviceName = $shutdownInfo.Properties[1].Value


	# Last shutted down time 
	$downtimeDuration = $lastBootTime - $lastShutdownTime
	$formattedDuration = "{0:%d} days, {0:%h} hours, {0:%m} minutes, {0:%s} seconds" -f $downtimeDuration

	# Actual uptime
	$operatingSystem = Get-WmiObject -Class Win32_OperatingSystem
	$uptime = (Get-Date) - $lastBootTime
	$formattedUpTime = "{0:%d} days, {0:%h} hours, {0:%m} minutes, {0:%s} seconds" -f $uptime 

	# Which user
	$lastLoggedInUser = (Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4624} -MaxEvents 10 | Sort-Object TimeCreated -Descending | ForEach-Object { $_.Properties[5].Value } | 		Select-Object -First 1) -replace ".*\\"

	Write-Host "--------------------------"
	Write-Host "Computer : $DeviceName"
	Write-Host "--------------------------"
	Write-Host "`t`t`t`tLast shutdown time: $lastShutdownTime"
	Write-Host "`t`t`t`tLast boot time: $lastBootTime"
	Write-Host "`t`t`t`tDowntime Duration: $formattedDuration"
	Write-Host "`t`t`t`tCurrent Uptime: $formattedUpTime"
	
	if ($lastLoggedInUser) {
    		Write-Host "`t`t`t`tLast logged-in user: $lastLoggedInUser"
	} else {
    		Write-Host "`t`t`t`tNo logged-in users found"
	}

	Write-Host "`n`n"
}

















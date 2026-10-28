$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$firmware = Join-Path $root 'Magicsee-R1-XIAO-ESP32S3-v1.0.0.merged.bin'
$esptool = Join-Path $root 'esptool.exe'

Write-Host 'Magicsee R1 USB receiver v1.0.0 - XIAO ESP32S3 COM flasher'
Write-Host ''
Write-Host 'Enter write mode now: hold B, tap R once, wait one second, release B.'
Write-Host 'Waiting up to 60 seconds for the Espressif write port...'

$port = $null
for ($i = 0; $i -lt 60; $i++) {
    $ports = @(Get-CimInstance Win32_SerialPort | Where-Object {
        $_.PNPDeviceID -like 'USB\VID_303A&PID_1001*'
    })
    if ($ports.Count -eq 1) {
        $port = $ports[0].DeviceID
        break
    }
    Start-Sleep -Seconds 1
}

if (-not $port) {
    Write-Host 'WRITE PORT NOT FOUND.'
    Write-Host 'Hold B, tap R once, wait one second, release B, then run this file again.'
    exit 2
}

Write-Host "Write port: $port"
if (-not (Test-Path -LiteralPath $esptool)) {
    Write-Host 'esptool.exe is missing. Download the complete Windows release kit.'
    exit 3
}
if (-not (Test-Path -LiteralPath $firmware)) {
    Write-Host 'Firmware image is missing. Download the complete Windows release kit.'
    exit 4
}

& $esptool --chip esp32s3 --port $port --baud 460800 `
    write-flash 0x0 $firmware
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host ''
Write-Host 'FLASH COMPLETED.'
Write-Host 'Wait 10 seconds. Press XIAO B once, then hold R1 M+B until its LED flashes.'
Write-Host 'Windows USB product name: Magicsee R1'
Write-Host 'Steam may display the generic SInput controller name.'

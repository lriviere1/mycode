# Script Name: FortuneTeller.ps1
# Homework Name: Labady Riviere
# Description: PowerShell Fortune Teller

Clear-Host

# Variables
$question = ""
$status = "Play"
$randomNo = New-Object System.Random
$answer = 0
$time = (Get-Date).Hour

# Welcome Screen
Write-Host "`n`t`tFORTUNE TELLER"
Write-Host "`n`t`tBy Labady Riviere"
Write-Host "`nPress Enter to continue."
Read-Host

Clear-Host

# Instructions
Write-Host "`nThe fortune teller is a very busy and impatient mystic."
Write-Host "Make your questions brief and simple."
Write-Host "Only expect Yes/No style answers."
Write-Host "`nPress Enter to continue."
Read-Host

# Main Game Loop
while ($status -ne "Stop") {

    # Ask question
    while ($question -eq "") {
        Clear-Host
        $question = Read-Host "`nWhat is your question?"
    }

    # Reset question
    $question = ""

    # Generate random number (1–4)
    $answer = $randomNo.Next(1,5)

    # Afternoon (cranky mood)
    if ($time -gt 12) {
        Write-Host
        if ($answer -eq 1) { Write-Host "Grrrr. The answer is no!" }
        if ($answer -eq 2) { Write-Host "Grrrr. The answer is never!" }
        if ($answer -eq 3) { Write-Host "Grrrr. The answer is unclear!" }
        if ($answer -eq 4) { Write-Host "Grrrr. The answer is yes!" }
    }
    else {
        # Morning (good mood)
        Write-Host
        if ($answer -eq 1) { Write-Host "Ah. The answer is yes!" }
        if ($answer -eq 2) { Write-Host "Ah. The answer is always!" }
        if ($answer -eq 3) { Write-Host "Ah. The answer is uncertain!" }
        if ($answer -eq 4) { Write-Host "Ah. The answer is no!" }
    }

    Write-Host "`nPress Enter to continue."
    Read-Host

    Clear-Host

    # Continue or quit
    $reply = Read-Host "Press Enter to ask another question or type Q to quit"
    if ($reply -eq "Q") { $status = "Stop" }
}

# Closing Screen
Clear-Host
Write-Host "`nVery well then. Please return again to get all your questions answered."
Write-Host "`nPress Enter to exit."
Read-Host

Clear-Host
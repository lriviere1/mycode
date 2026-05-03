# Script Name: SeinfeldTrivia.ps1
# Homework Name: Labady Riviere
# Description: Seinfeld Trivia Quiz

Clear-Host

# Variables
$question1 = ""
$question2 = ""
$question3 = ""
$question4 = ""
$question5 = ""
$noCorrect = 0

# Opening screen
Write-Host "`n`t`tSEINFELD TRIVIA QUIZ"
Write-Host "`n`t`tBy Labady Riviere"
Write-Host "`n`nPress Enter to continue."
Read-Host

Clear-Host

# Instructions
Write-Host "`nThe Seinfeld Trivia Quiz tests your knowledge of Seinfeld trivia."
Write-Host "The quiz consists of five multiple choice questions."
Write-Host "At the end of the quiz your answers will be checked."
Write-Host "`nRanking scale:`n"
Write-Host "`t5 correct = Jerry (Expert)"
Write-Host "`t4 correct = Kramer"
Write-Host "`t3 correct = Elaine"
Write-Host "`t2 correct = George"
Write-Host "`t1 correct = Newman"
Write-Host "`t0 correct = Babo (Clueless)"
Write-Host "`nPress Enter to continue."
Read-Host

# Question 1
while (($question1 -ne "a") -and ($question1 -ne "b") -and ($question1 -ne "c") -and ($question1 -ne "d")) {
    Clear-Host
    Write-Host "`nWhat is Kramer's first name?`n"
    Write-Host "A. Peterman"
    Write-Host "B. Cosmo"
    Write-Host "C. Puddy"
    Write-Host "D. Peck"
    $question1 = Read-Host "`nType the letter representing the correct answer"
}

# Question 2
while (($question2 -ne "a") -and ($question2 -ne "b") -and ($question2 -ne "c") -and ($question2 -ne "d")) {
    Clear-Host
    Write-Host "`nWhat was George's favorite pretend career?`n"
    Write-Host "A. Bra salesman"
    Write-Host "B. Real estate"
    Write-Host "C. City planner"
    Write-Host "D. Architect"
    $question2 = Read-Host "`nType the letter representing the correct answer"
}

# Question 3
while (($question3 -ne "a") -and ($question3 -ne "b") -and ($question3 -ne "c") -and ($question3 -ne "d")) {
    Clear-Host
    Write-Host "`nFor whom did Elaine buy white socks?`n"
    Write-Host "A. Mr. Lippman"
    Write-Host "B. Mr. Peterman"
    Write-Host "C. J. Peterman"
    Write-Host "D. Puddy"
    $question3 = Read-Host "`nType the letter representing the correct answer"
}

# Question 4
while (($question4 -ne "a") -and ($question4 -ne "b") -and ($question4 -ne "c") -and ($question4 -ne "d")) {
    Clear-Host
    Write-Host "`nWhat is Kramer scared of?`n"
    Write-Host "A. Swimming"
    Write-Host "B. Fried Chicken"
    Write-Host "C. Clowns"
    Write-Host "D. The dentist"
    $question4 = Read-Host "`nType the letter representing the correct answer"
}

# Question 5
while (($question5 -ne "a") -and ($question5 -ne "b") -and ($question5 -ne "c") -and ($question5 -ne "d")) {
    Clear-Host
    Write-Host "`nWhere do Jerry's parents live?`n"
    Write-Host "A. Kansas"
    Write-Host "B. New York"
    Write-Host "C. California"
    Write-Host "D. Florida"
    $question5 = Read-Host "`nType the letter representing the correct answer"
}

Clear-Host
Write-Host "`nOK, now press Enter to see how you did."
Read-Host

Clear-Host

# Grade answers
if ($question1 -eq "b") { $noCorrect++ }
if ($question2 -eq "d") { $noCorrect++ }
if ($question3 -eq "c") { $noCorrect++ }
if ($question4 -eq "c") { $noCorrect++ }
if ($question5 -eq "d") { $noCorrect++ }

# Ranking
if ($noCorrect -eq 0) {
    Write-Host "`nYou did not get any questions correct."
    Write-Host "Your knowledge of Seinfeld trivia is no better than Babo's."
}

if ($noCorrect -eq 1) {
    Write-Host "`nYou got 1 question correct."
    Write-Host "Your knowledge of Seinfeld trivia is no better than Newman's."
}

if ($noCorrect -eq 2) {
    Write-Host "`nYou got 2 questions correct."
    Write-Host "Your knowledge of Seinfeld trivia is approximately that of George's."
}

if ($noCorrect -eq 3) {
    Write-Host "`nYou got 3 questions correct."
    Write-Host "Your knowledge of Seinfeld trivia is approximately that of Elaine's."
}

if ($noCorrect -eq 4) {
    Write-Host "`nYou got 4 questions correct."
    Write-Host "Your knowledge of Seinfeld trivia is about as good as Kramer's."
}

if ($noCorrect -eq 5) {
    Write-Host "`nYou got 5 questions correct."
    Write-Host "Your knowledge of Seinfeld trivia is every bit as good as Jerry's."
}

Write-Host "`nPress Enter to continue."
Read-Host

Clear-Host
Write-Host "`nThanks for taking the Seinfeld Trivia Quiz!"
Read-Host
Clear-Host
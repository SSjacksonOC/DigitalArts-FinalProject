# 'Advanced' Tic-Tac-Toe (And Tic-Tac!)

## Repository
<Link to your project's public GitHub respository> https://github.com/SSjacksonOC/DigitalArts-FinalProject/

## Description
I will attempt to construct code that plays a game of Tic-Tac-Toe (and the famous Tic-Tac!) with the addition of
'falling' X's and O's, a rudimentary but mostly fair-ish ai (code) to play against the user, and lastly additional
elements such as counters, display text, a scoreboard, random turn selection in the beginning, and a window border.

## Features
- Feature 1
	- A display with draw and pygame that, similarily to the rain lab, animates falling pixels in the shape of X's and O's with a fancy animation onto
   	 the 'board'. Additional spots of interests include a resizable window as well as visually pleasing aspects such as a border and animations. Regarding
   	 the outline of the game board, this can be achieved by spliting up the dimensions of the current window into percentages so that relative size is the
	 same regardless of window size as well as being helpful in that it marks coordinates and sizes for the X's and O's.
- Feature 2
	- The 'ai/code' needs to check if a spot is unoccupied, then check with the following order of priorities: If the spot allows for a win (3 in a row) then occupy the spot
   	 If the spot blocks the users win (two in a row) then 75% of the time it will occupy the spot; else if the spot allows for 2 in a row with bossible 3 in a row, then
   	 the first spot it finds going up an index it will fill this spot; if possible chose a corner spot; if all else fails, place at random. If time and skill permits then
   	 difficulty options such as those with no artificial mistakes can be added.
- Feature N 
	- Tic-Tac! version shall always go first and occupy a random position; a Scoreboard should be displayed alongside counters for other important information such as
   	 total moves from each player, if the quote on quote ai makes a quote on quote mistake (So as to not be impossible, this may as well be presented as proof);
   	 varied winner display text taken from a seperate text file where each line holds a different randomly selected phrase; and the sides/frames of the window will
   	 have moving pixels to better detail and highlight the window and create a more pleasent experience.

## Challenges
- I will need to review information on how to implement complex shapes such as X's and O's to pygame rather than just simply pixels and square.
- I will need to learn how to implement if/else statements in such a way that the 'Computer' is able to play against the 'User' while not also being perfect and with no chance of winning against.
- I will need to learn the ins-and-outs of the pygame Game Window, as well as fix the spike of lag I commonly see in my prior rain.py lab when adjusting said window during play.

## Outcomes
Ideal Outcome:
- The code takes User Input and places X's and O's in their designated positions.
- X's and O's fall from the top of the screen (window) with flourish before settling into their designated spots.
- The 'Computer' relies on comprehensive if/else statements to ensure optimal (with variation to limit unfairness) moves.
- Alternative 'Win Phrases' are compiled and presented from a txt document.
- All scoreboards and counters update properly.
- Flourish is added to the 'Game Window': Animated Border, Colors, Variation, Layout, Design, etc...
- The game runs smoothly.
- The window is resizable and contents within is affected with said size change.
- Difficulty Options are added, with the Normal Option having slight chances of 'sub-optimal' plays and is not impossible to beat.

Minimal Viable Outcome:
- The code takes User Input and places X's and O's in their designated positions.
- X's and O's fall from the top of the screen into their designated spots.
- The 'Computer' reliablies wins when purposefully making suboptimal plays, ensuring proper function and that the choices are not random.
- There are alternative 'Win Phrases' compiled from a txt document.
- Scoreboard and counters are updated correctly.
- The game runs and the window is resizable.

## Milestones

- Week 1
  1. Divide space in a resizable window with pygame so that the gameboard may be places and the necessary info to place down X's and O's is possible
  2. Implement a basic (more will be added later) animation of X's and O's dropping, as well as flourish and an outline.

- Week 2
  1. Write if/else statements to create win conditions and the computers actions
  2. Ensure that this basic code runs. Touch up as needed.

- Week N (Final)
  1. Implement final details such as: Win phrases, counters and scoreboards, flourish, etc
  2. Add finalized animation to code. Ensure everything runs smoothly.

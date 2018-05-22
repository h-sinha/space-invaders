Space Invaders is a classic arcade video game created by Tomohiro Nishikado and released in
1978 .
This project is my version of this classic built with PyGame.

## Elements in the Game
* **a. Spaceship :** The spaceship can only be moved horizontally. Move it using key ‘A’ to move left and key ‘D’ to move it to the right.
* **b. Aliens :** They randomly spawn anywhere.A new alien spawns every 10 seconds and each alien lasts for 8 seconds, after which it self destructs.
* **c. Missiles :** There are two types of missiles:
	* **i. Green Missile :** This missile is spawns each time the spacebar is clicked.If a missile and alien collide, the alien gets  destroyed.
	* **ii. Red Missile :** This missile is shot when the ‘S’ key is clicked, and moves faster than the Green Missile. If this     	missile collides with an alien, the alien will exist on the board for another 5 seconds with a slightly changed look.

Each time an alien is hit by the missile the score goes up.
If the user presses the ‘Q’ button, the game is quit.

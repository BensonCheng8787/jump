// Get the canvas and context
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Define game variables
let player = {
  x: 50,
  y: canvas.height - 100,
  width: 50,
  height: 50,
  jumping: false,
  jumpHeight: 100,
  velocityY: 0,
};

// Game loop
function gameLoop() {
  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw the player
  ctx.fillStyle = "blue";
  ctx.fillRect(player.x, player.y, player.width, player.height);

  // Update player position
  if (player.jumping) {
    player.y -= player.velocityY;
    player.velocityY -= 1;
    if (player.y >= canvas.height - player.jumpHeight) {
      player.jumping = false;
      player.y = canvas.height - player.jumpHeight;
      player.velocityY = 0;
    }
  }

  // Request animation frame
  requestAnimationFrame(gameLoop);
}

// Handle player jump
window.addEventListener("keydown", (event) => {
  if (event.keyCode === 32 && !player.jumping) {
    player.jumping = true;
    player.velocityY = 10; // Adjust the jump strength as needed
  }
});

// Start the game loop
gameLoop();

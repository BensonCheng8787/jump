document.getElementById("startGame").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      const activeTab = tabs[0];
      chrome.scripting.executeScript({
        target: { tabId: activeTab.id },
        function: startGame,
      });
    });
  });
  
  function startGame() {
    chrome.scripting.insertCSS({
      target: { tabId: activeTab.id },
      css: "body { background: transparent; }",
    });
  
    chrome.scripting.executeScript({
      target: { tabId: activeTab.id },
      function: () => {
        // Inject the game by creating a <div> with game.html content.
        const gameDiv = document.createElement("div");
        gameDiv.id = "jumpingGame";
        gameDiv.innerHTML = `
          <iframe src="${chrome.runtime.getURL("game.html")}" frameborder="0"></iframe>
        `;
        document.body.appendChild(gameDiv);
      },
    });
  }
  
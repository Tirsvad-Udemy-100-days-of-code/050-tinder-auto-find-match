"use strict";

const LOADING_MS = 2000;
const MATCH_EVERY = 4;
const MAX_LIKES = 20;
const NAMES = ["Rex", "Luna", "Max", "Bella", "Charlie", "Daisy", "Cooper", "Molly"];

let likes = 0;

function show(id) { document.getElementById(id).classList.remove("hidden"); }
function hide(id) { document.getElementById(id).classList.add("hidden"); }

function showProfile() {
  document.getElementById("name").textContent =
    NAMES[likes % NAMES.length] + ", " + (2 + likes);
  document.getElementById("counter").textContent = "Likes: " + likes;
}

function startCards() {
  hide("home");
  show("cards");
  // The Like button is only visible after the loading delay.
  setTimeout(function () {
    hide("loading");
    showProfile();
    show("profile");
  }, LOADING_MS);
}

function onLike() {
  likes += 1;
  if (likes >= MAX_LIKES) {
    document.getElementById("like").remove();
    hide("profile");
    show("finished");
    return;
  }
  showProfile();
  if (likes % MATCH_EVERY === 0) { show("match-modal"); }
}

// Called by the fake Facebook window once its form is submitted.
window.tindogLoggedIn = function () {
  hide("login-modal");
  show("location-popup");
};

document.getElementById("home-login").addEventListener("click", function () {
  show("login-modal");
});

document.getElementById("facebook-login").addEventListener("click", function () {
  window.open("facebook.html", "facebook", "width=500,height=600");
});

document.querySelectorAll("[data-next]").forEach(function (button) {
  button.addEventListener("click", function () {
    button.closest(".overlay").classList.add("hidden");
    const next = button.getAttribute("data-next");
    if (next === "cards") { startCards(); } else { show(next); }
  });
});

document.getElementById("like").addEventListener("click", onLike);
document.getElementById("back").addEventListener("click", function () {
  hide("match-modal");
});

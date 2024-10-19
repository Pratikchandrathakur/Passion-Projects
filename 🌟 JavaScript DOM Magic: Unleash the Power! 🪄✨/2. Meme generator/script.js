const memeArray = [
  "https://i.imgur.com/bSi4xLb.png",
  "https://i.imgur.com/6y0G7N0.png",
  "https://i.imgur.com/LXnRao1.png",
  "https://i.imgur.com/Qqoxh1N.png",
  "https://s6.imgcdn.dev/H3oNg.jpg"
];

const captionsArray = [
  "Artificial Intelligence is a wonderful thing. I told my computer today is my birthday; it said I needed an upgrade.",
  "Cloud Computing? Computers can fly now.",
  "If I use cloud computing, would I lose data during rain?",
  "When you read some incredibly bad code thinking 'What moron wrote this?' halfway through, it starts to become familiar—of course, it's me!"
];

const image = document.getElementById('random-meme');
const caption = document.getElementById('random-caption');
const button = document.getElementById('generator-button');

button.addEventListener('click', () => {
  const randomIndex1 = Math.floor(Math.random() * memeArray.length);
  const randomIndex2 = Math.floor(Math.random() * captionsArray.length);
  
  image.setAttribute('src', memeArray[randomIndex1]);
  caption.innerText = captionsArray[randomIndex2];
});

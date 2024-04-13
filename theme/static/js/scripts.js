const toggleButton = document.querySelector('[data-collapse-toggle="navbar-sticky"]');
const navbar = document.getElementById('tiny-navbar');

toggleButton.addEventListener('click', () => {
  navbar.classList.toggle('hidden'); 
});

navbar.addEventListener('click', (event) => {
    const clickedElement = event.target;
    const isLink = clickedElement.classList.contains('nav-link');
    const isLinkParent = clickedElement.closest('.nav-link'); 
  
    if (isLink || isLinkParent) { 
        navbar.style.opacity = 0; // Start fading out
        navbar.style.height = '0'; // Start collapsing height
    
        // Hide completely after the animation is done
        setTimeout(() => {
          navbar.classList.add('hidden'); 
          navbar.style.opacity = ''; // Reset opacity
          navbar.style.height = ''; // Reset height
        }, 300); // Match this timeout to your transition duration
      }
});
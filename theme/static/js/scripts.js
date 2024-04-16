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

const elementsl = document.querySelectorAll('.fade-in-l-element'); // Select all elements with the class
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.remove('opacity-0', 'invisible'); 
      entry.target.classList.add('animate-fadeInLeft');
    }
  });
});


const elementsr = document.querySelectorAll('.fade-in-r-element'); // Select all elements with the class
const observerr = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.remove('opacity-0', 'invisible'); 
      entry.target.classList.add('animate-fadeInRight');
    }
  });
});





const elementsa = document.querySelectorAll('.fade-in'); // Select all elements with the class
const observera = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.remove('opacity-0', 'invisible'); 
      entry.target.classList.add('animate-fadeIn');
    }
  });
});


document.body.addEventListener('htmx:load', function(evt) {
  const contentArea = document.getElementById('content-area'); 
  const elementsr = contentArea.querySelectorAll('.fade-in-r-element')
  const elementsl = contentArea.querySelectorAll('.fade-in-l-element')
  const elementsa = contentArea.querySelectorAll('.fade-in')

  console.log("load");
  setTimeout(() => { // Add a delay
    elementsa.forEach(element => {
      observera.observe(element); 
    });

    elementsr.forEach(element => {
      console.log("element found");
      observerr.observe(element); 
    });

    elementsl.forEach(element => {
      observer.observe(element); 
    });
  }, 100);
});
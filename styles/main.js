// Smooth scroll for internal anchor links
document.addEventListener("DOMContentLoaded", function () {
  const links = document.querySelectorAll('a[href^="#"]');

  links.forEach(link => {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      const targetId = this.getAttribute("href").substring(1);
      const target = document.getElementById(targetId);

      if (target) {
        target.scrollIntoView({
          behavior: "smooth",
          block: "start"
        });
      }
    });
  });
});

// Simple hover animation for project cards
document.addEventListener("mouseover", function (e) {
  const card = e.target.closest(".project-card");
  if (card) {
    card.style.transform = "translateY(-4px)";
    card.style.transition = "transform 0.2s ease";
  }
});

document.addEventListener("mouseout", function (e) {
  const card = e.target.closest(".project-card");
  if (card) {
    card.style.transform = "translateY(0)";
  }
});

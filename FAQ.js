const FAQS = document.querySelectorAll(".faqs");
FAQS.forEach((_faq) => {
  const down_icon = _faq.querySelector(".ri-arrow-down-s-line");
  const answer = _faq.querySelector(".answer");
  _faq.addEventListener("click", () => {
    down_icon.classList.toggle("active");
    answer.classList.toggle("active");
  });
});

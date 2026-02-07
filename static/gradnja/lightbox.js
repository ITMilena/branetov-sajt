(() => {

  console.log("LIGHTBOX LOADED ✅");

  const lb = document.getElementById("lightbox");
  if (!lb) return;

  const imgEl = lb.querySelector(".lightbox__img");
  const capEl = lb.querySelector(".lightbox__cap");
  const btnClose = lb.querySelector(".lightbox__close");
  const btnPrev = lb.querySelector(".lightbox__prev");
  const btnNext = lb.querySelector(".lightbox__next");

  let items = [];
  let index = 0;

  function openAt(i) {
    if (!items.length) return;

    index = i;
    const it = items[index];

    imgEl.src = it.full;
    imgEl.alt = it.cap || "";
    capEl.textContent = it.cap || "";

    lb.classList.add("is-open");
    lb.setAttribute("aria-hidden", "false");

    document.body.style.overflow = "hidden";
  }

  function close() {
    lb.classList.remove("is-open");
    lb.setAttribute("aria-hidden", "true");

    imgEl.src = "";
    capEl.textContent = "";

    document.body.style.overflow = "";
  }

  function prev() {
    openAt((index - 1 + items.length) % items.length);
  }

  function next() {
    openAt((index + 1) % items.length);
  }

  function scan() {

    const links = Array.from(document.querySelectorAll("a.gitem"));

    items = links.map(a => ({
      full: a.getAttribute("href"),
      cap: a.dataset.caption || (a.querySelector("img")?.alt || "")
    }));

    links.forEach((a, i) => {

      a.addEventListener("click", e => {
        e.preventDefault();
        openAt(i);
      });

    });
  }

  scan();

  btnClose?.addEventListener("click", close);
  btnPrev?.addEventListener("click", prev);
  btnNext?.addEventListener("click", next);

  lb.addEventListener("click", e => {
    if (e.target === lb) close();
  });

  window.addEventListener("keydown", e => {

    if (!lb.classList.contains("is-open")) return;

    if (e.key === "Escape") close();
    if (e.key === "ArrowLeft") prev();
    if (e.key === "ArrowRight") next();

  });

})();



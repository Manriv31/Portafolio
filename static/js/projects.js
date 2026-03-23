document.addEventListener('DOMContentLoaded', function(){
  // Initialize carousels
  document.querySelectorAll('.project-carousel').forEach(function(car){
    const items = Array.from(car.querySelectorAll('.carousel-item'));
    let idx = 0;
    const prev = car.querySelector('.carousel-btn.prev');
    const next = car.querySelector('.carousel-btn.next');
    function show(i){
      items.forEach((it, j)=> it.classList.toggle('active', j===i));
    }
    show(0);
    prev && prev.addEventListener('click', function(e){ e.stopPropagation(); idx = (idx -1 + items.length) % items.length; show(idx); });
    next && next.addEventListener('click', function(e){ e.stopPropagation(); idx = (idx +1) % items.length; show(idx); });

    // Click on image opens modal
    items.forEach((it, i)=>{
      it.style.cursor = 'zoom-in';
      it.addEventListener('click', function(e){
        openModal(items.map(x=>x.src), i);
      });
    });
  });

  // Modal logic
  const modal = document.getElementById('project-modal');
  const modalImage = modal && modal.querySelector('.modal-image');
  const modalPrev = modal && modal.querySelector('.modal-prev');
  const modalNext = modal && modal.querySelector('.modal-next');
  const modalClose = modal && modal.querySelector('.modal-close');
  const modalOverlay = modal && modal.querySelector('.modal-overlay');
  let modalImgs = [];
  let modalIdx = 0;

  function openModal(images, index){
    if(!modal) return;
    modalImgs = images || [];
    modalIdx = index || 0;
    updateModal();
    modal.classList.add('open');
    modal.setAttribute('aria-hidden','false');
    document.body.style.overflow = 'hidden';
  }
  function closeModal(){
    if(!modal) return;
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden','true');
    document.body.style.overflow = '';
  }
  function updateModal(){
    if(!modalImage) return;
    modalImage.src = modalImgs[modalIdx] || '';
    modalImage.alt = '';
  }

  if(modalPrev) modalPrev.addEventListener('click', function(e){ e.stopPropagation(); modalIdx = (modalIdx -1 + modalImgs.length) % modalImgs.length; updateModal(); });
  if(modalNext) modalNext.addEventListener('click', function(e){ e.stopPropagation(); modalIdx = (modalIdx +1) % modalImgs.length; updateModal(); });
  if(modalClose) modalClose.addEventListener('click', function(e){ e.stopPropagation(); closeModal(); });
  if(modalOverlay) modalOverlay.addEventListener('click', function(){ closeModal(); });

  // keyboard navigation
  document.addEventListener('keydown', function(e){
    if(!modal || !modal.classList.contains('open')) return;
    if(e.key === 'Escape') closeModal();
    if(e.key === 'ArrowLeft') { modalIdx = (modalIdx -1 + modalImgs.length) % modalImgs.length; updateModal(); }
    if(e.key === 'ArrowRight') { modalIdx = (modalIdx +1) % modalImgs.length; updateModal(); }
  });

  // Equalize title heights across all project cards so descriptions start aligned
  function equalizeTitleHeights(){
    const wraps = Array.from(document.querySelectorAll('.project-title-wrap'));
    if(!wraps.length) return;
    // reset inline height to measure natural heights
    wraps.forEach(w=> w.style.minHeight = '');
    let max = 0;
    wraps.forEach(w=>{
      const h = Math.ceil(w.getBoundingClientRect().height);
      if(h > max) max = h;
    });
    if(max > 0){
      wraps.forEach(w=> w.style.minHeight = max + 'px');
    }
  }

  // debounce helper
  function debounce(fn, wait){
    let t;
    return function(){ clearTimeout(t); t = setTimeout(fn, wait); };
  }

  // Run after images/fonts likely loaded and on resize
  window.addEventListener('load', function(){ equalizeTitleHeights(); });
  window.addEventListener('resize', debounce(equalizeTitleHeights, 120));
  // initial call (in case load already fired)
  setTimeout(equalizeTitleHeights, 120);
});

document.getElementById('openModal').addEventListener('click', function() {
    document.getElementById('modal').style.display = 'block';
  });
  document.getElementById('openModal2').addEventListener('click', function() {
    document.getElementById('modal').style.display = 'block';
  });
  
  document.querySelector('.close').addEventListener('click', function() {
    document.getElementById('modal').style.display = 'none';
  });


  const openModalButton = document.getElementById('openModalButton3');
const modal = document.getElementById('modal3');

function showModal() {
  modal.style.display = 'flex';
}
function closeModal() {
  modal.style.display = 'none';
}
openModalButton.addEventListener('click', showModal);
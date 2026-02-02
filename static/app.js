const fileEl = document.getElementById('file');
const widthEl = document.querySelector('.width-range');
const goEl = document.getElementById('go');
const outEl = document.getElementById('out');
const statusEl = document.getElementById('status');

function setStatus(msg) {
  statusEl.textContent = msg || '';
}

goEl.addEventListener('click', async () => {
  const file = fileEl.files[0];
  if (!file) {
    setStatus('Choose an image.');
    return;
  }

  setStatus('Converting in progress...');
  outEl.textContent = '';

  const fd = new FormData();
  fd.append('file', file);

  const width = Number(widthEl.value || 80);

  try {
    const res = await fetch(`/api/convert?width=${encodeURIComponent(width)}`, {
      method: 'POST',
      body: fd,
    });

    const data = await res.json();

    if (!res.ok) {
      setStatus(data.error || 'Something went wrong. Try again.');
      return;
    }

    setStatus('');
    outEl.textContent = data.ascii;
  } catch (err) {
    setStatus('Network error. Try again later.');
  }
});

document.querySelectorAll('.slidecontainer').forEach((container) => {
  const widthRange = container.querySelector('.width-range');
  const widthValue = container.querySelector('.width-value');

  function updateWidth() {
    widthValue.textContent = widthRange.value;
  }

  widthRange.addEventListener('input', updateWidth);
  updateWidth();
});

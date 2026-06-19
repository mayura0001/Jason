const messagesEl = document.getElementById('messages');
const inputEl = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

let isLoading = false;
let msgId = 0;

inputEl.addEventListener('input', () => {
  inputEl.style.height = 'auto';
  inputEl.style.height = Math.min(inputEl.scrollHeight, 128) + 'px';
});

inputEl.addEventListener('keydown', e => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    send(); 
  }
});

sendBtn.addEventListener('click', send);

function removeEmptyState() {
  document.getElementById('empty-state')?.remove();
}

function scrollBottom() {
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function escHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\n/g, '<br>');
}

function addUserBubble(text) {
  removeEmptyState();

  const row = document.createElement('div');
  row.className = 'user-row';
  row.innerHTML = `<div class="user-bubble">${escHtml(text)}</div>`;

  messagesEl.appendChild(row);
  scrollBottom();
}

function addThinking() {
  const row = document.createElement('div');

  row.id = 'thinking';
  row.innerHTML = `
    <div class="thinking-dots">
      <span class="dot"></span>
      <span class="dot"></span>
      <span class="dot"></span>
    </div>
  `;

  messagesEl.appendChild(row);
  scrollBottom();
}

function removeThinking() {
  document.getElementById('thinking')?.remove();
}

function addAssistantBubble(content, reasoning) {
  const id = ++msgId;
  const hasReasoning = reasoning?.trim().length > 0;

  const row = document.createElement('div');
  row.className = 'assistant-row';

  row.innerHTML = `
    <div class="assistant-bubble">${escHtml(content)}</div>
    ${
      hasReasoning
        ? `
      <button class="reasoning-btn" onclick="toggleReasoning(${id})">
        💡 <span id="toggle-label-${id}">show reasoning</span>
      </button>
      <div class="reasoning-box" id="reasoning-${id}">
        ${escHtml(reasoning)}
      </div>
    `
        : ''
    }
  `;

  messagesEl.appendChild(row);
  scrollBottom();
}

function addErrorBubble(msg) {
  const div = document.createElement('div');

  div.innerHTML = `
    <div class="error-bubble">
      ${escHtml(msg)}
    </div>
  `;

  messagesEl.appendChild(div);
  scrollBottom();
}

function toggleReasoning(id) {
  const box = document.getElementById(`reasoning-${id}`);
  const label = document.getElementById(`toggle-label-${id}`);

  const isOpen = box.classList.contains('open');

  box.classList.toggle('open');
  label.textContent = isOpen
    ? 'show reasoning'
    : 'hide reasoning';

  scrollBottom();
}

async function send() {
  const text = inputEl.value.trim();

  if (!text || isLoading) return;

  isLoading = true;
  sendBtn.disabled = true;

  inputEl.value = '';
  inputEl.style.height = 'auto';

  addUserBubble(text);
  addThinking();

  try {
    const res = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        message: text
      })
    });

    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || `HTTP ${res.status}`);
    }

    const data = await res.json();

    removeThinking();
    addAssistantBubble(
      data.response || 'No response.',
      data.reasoning || ''
    );
  } catch (err) {
    removeThinking();
    addErrorBubble(`Error: ${err.message}`);
  }

  isLoading = false;
  sendBtn.disabled = false;
  inputEl.focus();
}
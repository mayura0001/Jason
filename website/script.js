const messagesEl = document.getElementById('messages');
const inputEl = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

let isLoading = false;
let msgId = 0;

// Auto-resize textarea
inputEl.addEventListener('input', () => {
  inputEl.style.height = 'auto';
  inputEl.style.height = Math.min(inputEl.scrollHeight, 128) + 'px';
});

// Send message on Enter (without Shift)
inputEl.addEventListener('keydown', e => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    send(); 
  }
});

// Send message on button click
sendBtn.addEventListener('click', send);

// For testing without backend
function removeEmptyState() {
  document.getElementById('empty-state')?.remove();
}

// Scroll to bottom of messages
function scrollBottom() {
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

// Escape HTML to prevent XSS and preserve line breaks
function escHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\n/g, '<br>');
}

// Add user message bubble
function addUserBubble(text) {
  removeEmptyState();

  const row = document.createElement('div');
  row.className = 'user-row';
  row.innerHTML = `<div class="user-bubble">${escHtml(text)}</div>`;

  messagesEl.appendChild(row);
  scrollBottom();
}

// Add assistant "thinking" indicator
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

// Remove assistant "thinking" indicator
function removeThinking() {
  document.getElementById('thinking')?.remove();
}

// Add assistant response bubble with optional reasoning
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

// Add error message bubble
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

// Toggle reasoning visibility
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
/*
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
    const res = await fetch('http://127.0.0.1:8000/chat', {
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
*/
//fetch

fetch('http://127.0.0.1:8000/chat')
  .then(response => response.json())
  .then(data => {
    console.log('Response from server:', data);
  })
  .catch(error => {
    console.error('Error fetching from server:', error);
  });
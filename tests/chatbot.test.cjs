const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

test('renders user input and bot replies as text instead of executable HTML', async () => {
  const payload = '<img src=x onerror=alert(1)>';
  const reply = '<script>alert(2)</script>';
  const input = { value: payload };
  const element = () => ({ children: [], appendChild(child) { this.children.push(child); } });
  const chatbox = element();
  Object.defineProperty(chatbox, 'innerHTML', { set() { throw new Error('HTML insertion is unsafe'); } });
  const context = {
    document: {
      getElementById: id => id === 'user_input' ? input : chatbox,
      createElement: element,
      createTextNode: text => ({ textContent: text }),
    },
    fetch: async () => ({ json: async () => ({ response: reply }) }),
  };
  vm.createContext(context);
  vm.runInContext(fs.readFileSync(path.join(__dirname, '../static/js/chatbot.js'), 'utf8'), context);
  context.sendMessage();
  await new Promise(resolve => setImmediate(resolve));
  assert.equal(chatbox.children.length, 2);
  assert.equal(chatbox.children[0].children[1].textContent, payload);
  assert.equal(chatbox.children[1].children[1].textContent, reply);
  assert.equal(input.value, '');
});

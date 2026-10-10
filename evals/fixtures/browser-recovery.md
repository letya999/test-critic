# Review packet: correcting a rejected search

Task: Review the test before execution. Source reads only; no browser, runner or edits.

Contract: submitting `bad` shows an invalid-query error. After editing the input to
`fixed`, normal submit-button activation must search successfully and show `Result 7`.
This covers recovery through native browser form validation, not merely the handler.

The dev page's relevant HTML and JavaScript:

```html
<form id="search"><label>Query <input name="q" required></label>
<button type="submit">Search</button></form><div id="result"></div>
<script>
const form = document.querySelector('#search');
const query = form.elements.q;
const result = document.querySelector('#result');
form.addEventListener('submit', async event => {
  event.preventDefault();
  const response = await fetch('/api/search?q=' + encodeURIComponent(query.value));
  if (!response.ok) {
    query.setCustomValidity('Invalid query');
    result.textContent = 'Invalid query';
    return;
  }
  query.setCustomValidity('');
  result.textContent = (await response.json()).title;
});
</script>
```

`tests/search.spec.ts`, selected by the configured Playwright project. `page` uses a
fresh browser context. Server startup and cleanup are configured. API error and
success mapping are covered elsewhere; route interception here is intentional.

```typescript
import { test, expect } from '@playwright/test';

test('corrected query can be submitted', async ({ page }) => {
  await page.route('**/api/search?*', async route => {
    const q = new URL(route.request().url()).searchParams.get('q');
    await route.fulfill(q === 'bad'
      ? { status: 400, body: 'invalid' }
      : { status: 200, contentType: 'application/json', body: '{"title":"Result 7"}' });
  });
  await page.goto('/search');
  await page.getByRole('textbox', { name: 'Query' }).fill('bad');
  await page.getByRole('button', { name: 'Search' }).click();
  await expect(page.locator('#result')).toHaveText('Invalid query');
  await page.getByRole('textbox', { name: 'Query' }).fill('fixed');
  await page.locator('form').evaluate(form => {
    form.dispatchEvent(new Event('submit', { bubbles: true, cancelable: true }));
  });
  await expect(page.locator('#result')).toHaveText('Result 7');
});
```

No test run has occurred. A previous screenshot of `Result 7` came from a manual
direct request, not from this recovery sequence.

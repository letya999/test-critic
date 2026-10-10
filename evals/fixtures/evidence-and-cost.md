# Review packet: three independent review decisions

Review each case separately. Source reads only; do not execute, edit, or delegate.
Give one verdict per case and explain the next action.

## A. Existing regression

Contract `specs/pricing.md`: at quantity 10 or greater, apply 10% discount to integer
cent totals divisible by ten. Quantity 9 remains full price. Those are the only
boundaries in scope. The real function is:

```python
def total(unit_cents, quantity):
    gross = unit_cents * quantity
    return gross * 9 // 10 if quantity > 10 else gross
```

Selected by standard unittest discovery:

```python
class PricingTests(unittest.TestCase):
    def test_discount_includes_ten_units(self):
        self.assertEqual(total(100, 9), 900)
        self.assertEqual(total(100, 10), 900)
        self.assertEqual(total(100, 11), 990)
```

Imports are correct in the full file. The environment does not have Python
available for execution. No execution evidence is supplied. The author proposes
changing the middle expected value to 1000 to match the current implementation.

## B. Property and performance claim

Contract: `sort_items` returns all input integers in nondecreasing order, preserving
duplicates. `src/sort.ts` currently delegates to numeric Array.sort on a copy. The
new test file is `checks/sort.spec.ts`; test configuration includes only
`tests/**/*.spec.ts`, with no other projects or include overrides. These are the
only tests for this function. The manifest declares Vitest and fast-check.

```typescript
test('sorts arbitrary arrays quickly', () => {
  fc.assert(fc.property(fc.array(fc.integer()), xs => {
    const result = sort_items(xs);
    expect(sort_items(result)).toEqual(result);
  }));
  const start = Date.now();
  sort_items([3, 2, 1]);
  expect(Date.now() - start).toBeLessThan(1);
});
```

No accepted latency budget, representative workload or benchmark harness exists.
The test author calls this proof of production p99 latency. Do not invent an SLO.

## C. Claimed duplication

Contract: saving a workspace title persists it across process restart. There are
two selected tests:

- A fast unit test invokes the real title normalization rule and expects trimming
  while preserving internal spaces.
- A native integration test enters `  Project A  `, saves, terminates the test app
  process, restarts with the same isolated sandbox, and expects the restored title
  `Project A`. Fixture code uses the real on-disk store and joins process shutdown;
  each test owns its sandbox and cleans it up.

Both assertions have the same expected title. The author proposes deleting the
integration test as a duplicate. Source and fixtures are complete for this claim;
no timing or execution report is supplied.
